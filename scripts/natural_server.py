#! /usr/bin/env python

import rospy
import actionlib # used to import actionlib library for implementing simple action

import behaviourtree_tutorial.msg # the line imports the msgs genereated by the action specification


class naturalnumAction_server():

	def __init__(self,name):
		# create msgs used to publish feedback/result
		self._feedback = behaviourtree_tutorial.msg.naturalnumFeedback()
		self._result = behaviourtree_tutorial.msg.naturalnumResult()

		self.action_name = name
		self.action_server = actionlib.SimpleActionServer(self.action_name,
															behaviourtree_tutorial.msg.naturalnumAction,
															execute_cb = self.server_callback, 
															auto_start= False)
		# here we define a SimpleActionServer
		# its arguments include- actionnamespace, action type, a callback
		# alsways define auto_start flag as false, because by default it is true.
		# ref to - https://answers.ros.org/question/107126/actionlib-auto_start-parameter/ to get more details
		self.action_server.start()
		# as the name suggests, this starts the action server

	def server_callback(self, goal):
		# helper variables
		r = rospy.Rate(1)
		success = True

		self._feedback.sequence = []
		
		rospy.loginfo("%s: Executing, creating natural number series with number of element %i" % (self.action_name, goal.num_steps))

		# executing the action
		for i in range(goal.num_steps):
			# check if the goal isnt cancelled
			if self.action_server.is_preempt_requested():
				rospy.loginfo("%s Preempted" % self.action_name)
				self.action_server.set_preempted()
				success = False
				break

			self._feedback.sequence.append(i+1)

			# publish the feedback
			self.action_server.publish_feedback(self._feedback)

			r.sleep()

		if success:
			self._result.sequence = self._feedback.sequence
			rospy.loginfo("%s succeeded"% self.action_name)
			self.action_server.set_succeeded(self._result)


if __name__ == "__main__":
	rospy.init_node("NaturalNumberListNode")
	server = naturalnumAction_server(rospy.get_name())
	rospy.spin()

