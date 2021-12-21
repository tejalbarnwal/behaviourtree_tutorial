#! /usr/bin/env python

from __future__ import print_function
import rospy

import actionlib

import behaviourtree_tutorial.msg

import functools
import py_trees
import py_trees_ros
import py_trees.console as console
import rospy
import sys

def create_root():
    # behaviours
    root = py_trees.composites.Parallel("Tutorial")
    topics2bb = py_trees.composites.Sequence("Topics2BB")
    scan2bb = py_trees_ros.subscribers.EventToBlackboard(
        name="Scan2BB",
        topic_name="/dashboard/scan",
        variable_name="event_scan_button"
    )
    battery2bb = py_trees_ros.battery.ToBlackboard(name="Battery2BB",
                                                   topic_name="/battery/state",
                                                   threshold=30.0
                                                   )
    priorities = py_trees.composites.Selector("Priorities")
    battery_check = py_trees.meta.success_is_failure(py_trees.composites.Selector)(name="Battery Emergency")
    is_battery_ok = py_trees.blackboard.CheckBlackboardVariable(
        name="Battery Ok?",
        variable_name='battery_low_warning',
        expected_value=False
    )
    flash_led_strip = py_trees_ros.tutorials.behaviours.FlashLedStrip(
        name="Flash Red",
        colour="red")

    scan = py_trees.composites.Sequence(name="Scan")
    is_scan_requested = py_trees.blackboard.CheckBlackboardVariable(
        name="Scan?",
        variable_name='event_scan_button',
        expected_value=True
    )
    scan_preempt = py_trees.composites.Selector(name="Preempt?")
    is_scan_requested_two = py_trees.meta.success_is_running(py_trees.blackboard.CheckBlackboardVariable)(
        name="Scan?",
        variable_name='event_scan_button',
        expected_value=True
    )
    scanning = py_trees.composites.Parallel(name="Scanning", policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ONE)
    scan_rotate = py_trees_ros.actions.ActionClient(
        name="Rotate",
        action_namespace="/rotate",
        action_spec=py_trees_msgs.RotateAction,
        action_goal=py_trees_msgs.RotateGoal(),
        override_feedback_message_on_running="rotating"
    )
    scan_flash_blue = py_trees_ros.tutorials.behaviours.FlashLedStrip(name="Flash Blue", colour="blue")
    scan_celebrate = py_trees.composites.Parallel(name="Celebrate", policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ONE)
    scan_flash_green = py_trees_ros.tutorials.behaviours.FlashLedStrip(name="Flash Green", colour="green")
    scan_pause = py_trees.timers.Timer("Pause", duration=3.0)
    idle = py_trees.behaviours.Running(name="Idle")

    # tree
    root.add_children([topics2bb, priorities])
    topics2bb.add_children([scan2bb, battery2bb])
    priorities.add_children([battery_check, scan, idle])
    battery_check.add_children([is_battery_ok, flash_led_strip])
    scan.add_children([is_scan_requested, scan_preempt, scan_celebrate])
    scan_preempt.add_children([is_scan_requested_two, scanning])
    scanning.add_children([scan_rotate, scan_flash_blue])
    scan_celebrate.add_children([scan_flash_green, scan_pause])
    return root


def shutdown(behaviour_tree):
    behaviour_tree.interrupt()

##############################################################################
# Main
##############################################################################


def main():
    """
    Entry point for the demo script.
    """
    rospy.init_node("tree")
    root = create_root()
    behaviour_tree = py_trees_ros.trees.BehaviourTree(root)
    rospy.on_shutdown(functools.partial(shutdown, behaviour_tree))
    if not behaviour_tree.setup(timeout=15):
        console.logerror("failed to setup the tree, aborting.")
        sys.exit(1)
    behaviour_tree.tick_tock(500)

