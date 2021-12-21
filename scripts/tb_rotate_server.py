#! /usr/bin/env python

import rospy
import actionlib # used to import actionlib library for implementing simple action

import behaviourtree_tutorial.msg # the line imports the msgs genereated by the action specification
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32
from math import pi



# rostopic pub /turtle1/cmd_vel geometry_msgs/Twist "linear: 
#   x: 0.0
#   y: 0.0
#   z: 0.0
# angular:
#   x: 0.0
#   y: 0.0
#   z: 0.05" -r 10 


class tb_rotate_ActionServer():

	def __init__(self,name):
		# create msgs used to publish feedback/result
		self._feedback = behaviourtree_tutorial.msg.tb_rotateFeedback()
		self._result = behaviourtree_tutorial.msg.tb_rotateResult()

		self.action_name = name
		self.action_server = actionlib.SimpleActionServer(self.action_name,
															behaviourtree_tutorial.msg.tb_rotateAction,
															execute_cb = self.server_callback, 
															auto_start= False)
		# here we define a SimpleActionServer
		# its arguments include- actionnamespace, action type, a callback
		# alsways define auto_start flag as false, because by default it is true.
		# ref to - https://answers.ros.org/question/107126/actionlib-auto_start-parameter/ to get more details
		self.action_server.start()
		# as the name suggests, this starts the action server

		## NEED SOME SUBSCRIBERS FOR THE ODOM TOPIC
		sub_OdomTopic = "/turtle1/pose"
		pub_velTopic = "/turtle1/cmd_vel"
		rospy.Subscriber(sub_Odomtopic, Pose, self.pose_Callback)

		## NEED SOME PUBLISHER FOR THE CMD VEL
        self.vel_publisher = rospy.Publisher(pub_velTopic, Twist , queue_size =1)

		self.yaw = Float32()
		self.init_yaw = Float32()
		self.initlization = False

		self.goal = pi / 2 # abhi sirf x direction mein move krega, par baadmein 
		# aur functionalities add krdena mai!
		self.vel_msg = Twist()

	def pose_Callback(self,msg):
		# Initializing the intial value of bot
		if not self.initlization:
			self.init_yaw = msg.theta
			self.initlization = True
		# updating the feedback values
		self.yaw = msg.theta


	def server_callback(self, goal):
		# helper variables
		r = rospy.Rate(10)
		success = True

		self._feedback.percentage_completed = 0.0
		self._feedback.angle_rotated = 0.0 # does not considers previous distance moved by bot 
		
		# rospy.loginfo("%s: Executing, creating natural number series with number of element %i" % (self.action_name, goal.num_steps))
		rospy.loginfo("Initializing with the moving forward task")

		# EXECUTE ACTION
		# CHECK IF YOU NEED A LOOP? ADD PREEMPTION CONDITON! 
		# IMPLEMENT WHAT TO DO TO EXECUTE ACTION
		# PUBLISH FEEDBACK AND WHATEVER SHIT ACC TO YOUR TASK
		# ADD WHAT TO DO IF YOU SUCCEED

		# executing the action
		while (self.yaw - self.init_yaw) < self.goal:
			# check if the goal isnt cancelled
			if self.action_server.is_preempt_requested():
				rospy.loginfo("%s PREEMPTED" % self.action_name)
				self.action_server.set_preempted()
				success = False
				break

			self._feedback.angle_rotated = self.yaw - self.init_yaw
			self._feedback.percentage_completed = (self._feedback.angle_rotated) * 100.0 / (self.goal)
                                                                                      
			self.vel_msg.angular.z = 0.05
			# publish the vel to cmd vel
			self.vel_publisher.publish(vel_msg)

			#  publish feedback
			self.action_server.publish_feedback(self._feedback)

			r.sleep()

		if success:
			self._result.value = self._feedback.percentage_completed
			self._result.message = "TEJU YAYYAY"
			rospy.loginfo("%s SUCCEEDED"% self.action_name)
			self.action_server.set_succeeded(self._result)



if __name__ == "__main__":
	rospy.init_node("tb_rotateberListNode")
	server = tb_rotate_ActionServer(rospy.get_name())
	rospy.spin()

