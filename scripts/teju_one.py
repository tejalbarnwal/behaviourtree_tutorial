#!/usr/bin/env python

import functools
import py_trees
import py_trees_ros
import py_trees.console as console
import rospy
import sys

import argparse
import importlib


##############################################################################
# Behaviours
##############################################################################


def create_root():
    """
    Create a basic tree and start a 'Topics2BB' work sequence that
    takes the asynchronicity out of subscription.
    Returns:
        :class:`~py_trees.behaviour.Behaviour`: the root of the tree
    """
    root = py_trees.composites.Parallel("Tutorial")

    topics2bb = py_trees.composites.Sequence("Topics2BB")
    battery2bb = py_trees_ros.battery.ToBlackboard(name="Battery2BB",
                                                   topic_name="/battery/state",
                                                   threshold=30.0
                                                   )
    priorities = py_trees.composites.Selector("Priorities")
    idle = py_trees.behaviours.Running(name="Idle")

    root.add_child(topics2bb)
    topics2bb.add_child(battery2bb)
    root.add_child(priorities)
    priorities.add_child(idle)
    return root


def shutdown(behaviour_tree):
    behaviour_tree.interrupt()

##############################################################################
# Main
##############################################################################


if __name__ == '__main__':
    """
    Entry point for the demo script.
    """
    print("TEJU: start with node")
    rospy.init_node("tree")

    print("TEJU: create an instace for rrot")
    root = create_root()

    behaviour_tree = py_trees_ros.trees.BehaviourTree(root)
    print("TEJU: create a tree out from the root")

    rospy.on_shutdown(functools.partial(shutdown, behaviour_tree))
    if not behaviour_tree.setup(timeout=15):
        console.logerror("failed to setup the tree, aborting.")
        sys.exit(1)
    behaviour_tree.tick_tock(500)
    rospy.spin()
