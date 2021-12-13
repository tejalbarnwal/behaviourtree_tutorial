#! /usr/bin/env python

from __future__ import print_function
import rospy

import actionlib

import behaviourtree_tutorial.msg

def naturalnumAction_client():
	# creating a simple action client
	# name and type of action
	client = actionlib.SimpleActionClient("NaturalNumberListNode", 
										behaviourtree_tutorial.msg.naturalnumAction)

	print("WAITING FOR THE SERVER")
	# waits for the action server to begin
	client.wait_for_server()
	print("CREATING GOAL")
	# creates a goal to send to the action server
	goal = behaviourtree_tutorial.msg.naturalnumGoal(num_steps=5)
	print("SENDING GOAL")
	# send the goals
	client.send_goal(goal)
	print("WAITING FOR RESULT")
	# waits for the server to finish performing action
	client.wait_for_result()
	print("OBTAINED THE RESULT")
	# prints out the result of executing the action
	return client.get_result() 


if __name__=="__main__":
	try:
		rospy.init_node("naturalnumber_actioonClient")
		result = naturalnumAction_client()
		print("Result: ",", ".join([str(n) for n in result.sequence]))
	except rospy.ROSInterruptException:
		print("program interupted before completion", file=sys.stderr)
		