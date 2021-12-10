#! /usr/bin/env python

import rospy
import actionlib # used to import actionlib library for implementing simple action

import behaviourtree_tutorial.msg # the line imports the msgs genereated by the action specification


class naturalnumAction():
	# create msgs used to publish feedback/result
	_feedback = behaviourtree_tutorial.msg.naturalnumFeedback()
	_result = behaviourtree_tutorial.msg.naturalnumResult()

	def __init__(self,name):
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

		
