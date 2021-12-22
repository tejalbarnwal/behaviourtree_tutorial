#!/usr/bin/env python

import py_trees
import py_trees_ros
import py_trees.console as console
import rospy
import sys
from turtlesim.msg import Pose
import behaviourtree_tutorial.msg
import functools
import argparse
import importlib

"""
chatter_to_blackboard = ToBlackboard(topic_name="chatter",
                                     topic_type=std_msgs.msg.String,
                                     blackboard_variables = {'chatter': None}
                                     )
"""
def create_root():
	#### ROOT
	root = py_trees.composites.Parallel("TejuTutorial")

	#### BRANCH 1
	# added something to put data to black board
	topics2bb = py_trees.composites.Sequence("Topics2BB")
	pose2bb = py_trees_ros.subscribers.ToBlackboard(topic_name = "/turtle1/pose",
													topic_type=Pose,
													blackboard_variables = {"tejupose": None})
	
	# added a std_msgs.msg.Empty type for bool if scan is to be performed
	scan2bb = py_trees_ros.subscribers.EventToBlackboard(
		name = "Scan2BB",
		topic_name = "/dashboard/scan",
		variable_name = "event_scan_button"
		)

	#### BRANCH 2
	priorities = py_trees.composites.Selector("Priorities")

	## BRANCH 2.2
	idle = py_trees.behaviours.Running(name="Idle")

	## BRANCH 2.1
	# add scan pipeline ( a sequence)
	scan = py_trees.composites.Sequence(name="Scan")

	is_scan_requested = py_trees.blackboard.CheckBlackboardVariable(
		name="Scan?",
		variable_name = "event_scan_button",
		expected_value = True
		)
	scan_preempt = py_trees.composites.Selector(name = "Preempt?")

	is_scan_requested_two = py_trees.meta.success_is_running(py_trees.blackboard.CheckBlackboardVariable)(
		name = "Scan?",
		variable_name="event_scan_button",
		expected_value=True)

	scan_rotate = py_trees_ros.actions.ActionClient(
		name = "Rotate",
		action_namespace = "tb_rotateberListNode",
		action_spec = behaviourtree_tutorial.msg.tb_rotateAction,
		action_goal=behaviourtree_tutorial.msg.tb_rotateGoal(),
		override_feedback_message_on_running="Teju yay its ROTATING"
		)

	# TREE
	root.add_children([topics2bb, priorities])
	topics2bb.add_children([pose2bb, scan2bb])
	priorities.add_children([scan,idle])
	scan.add_children([is_scan_requested,scan_preempt])
	scan_preempt.add_children([is_scan_requested_two,scan_rotate])

	return root

def shutdown(behaviour_tree):
	behaviour_tree.interrupt()


if __name__ == "__main__":

	print("TEJU : start the node")
	rospy.init_node("tree")

	print("TEJU : create an instance for root")
	root = create_root()

	behaviour_tree = py_trees_ros.trees.BehaviourTree(root)
	print("TEJU : create a tree out from the root")

	rospy.on_shutdown(functools.partial(shutdown, behaviour_tree))
	if not behaviour_tree.setup(timeout=15):
		console.logerror("failed to setup the tree, aborting")
		sys.exit(1)

	behaviour_tree.tick_tock(500)
	rospy.spin()