# PyTrees Documentation

## Intro
Various deicion making engines - behaviour trees, hierarchial finite state machines, task networks, and scripting engines

Go through "Behavior Trees in Robotics and AI" to have brief overview about their usability

## Behaviours
A `behaviour` is the smallest element in a behaviour tree similar to a LEAF. A behaviour could be check condition or an an action

#### Skeleton
``` python
import py_trees

class Foo(py_trees.behaviour.Behaviour):
	def __init__(self, name):
		# minimal one time initlaization
		# for initializinfg other times just use the setup() method
		# It initiates the behaviour sufficiently for offline dot graph generation
	def setup(self):
		# this function can be called manually or it can be called automatically with initalizations
		# One time initializations of resources that are required for execution
		# jo constructor handle mhi kr skta jaise hardware connections, middleware and other heavy resources
	def initialise(self):
		# This is called when the behaviour is ticked first time 
		# jab behaviour ka work shuru krne se pehle kuch krwana toh h ye krna hota h
		# this basically configures and resets the behaviour ready for (repeated) execution
	def update(self):
		# every time the behaviour is ticked this fucntion is called
		# yahi se return hota h ki running tha ya failure ya success
		# it should return either failure, success, running or invalid(unintialized or inactive)
	def terminate(self, new_status):
		# you can pass failure/ success / invalid to it and behaviour ek non running state mein chala jayega

```

The lifecycle of a behaviour is given by:
1. __init__()
2. setup()
the above two methods are called explicitly
3. Then you start ticking the behaviour
the `tick()` determines when to call intialize(), stop() and terminate()
The initialize mehtod is only called when the behaviour is not already running
4. tick() also always calls update()
5. update() decuides the behaviour status

## Composites
They are the factories and the decision makers of a behaviour tree
They could be a sequence, selector, chooser or parallel

#### Sequence [Rectangle]
Eexcutes children sequentially

#### Selector [Octagon]
Select a path through the tree, interruptible by higher priorities

#### Chooser [Bordered Octagon]
Like a selector, but commits to a path once started until it finishes

#### Parallel [Parallelogram]
Manage Children concurrently where you can also define all policy acc to your needs
Policy could be successonall, successoone or successonselected

## Decorators
They are used only for a single child and they provide us to make common modicifications such as inverting, timout, status to blackboard, ya running is success, successis failure..

## Blackboards
They are mechanism for sharing the data btw different behaviour in a tree
The implemenatiion way follows clients and key-value jaisa form
Clients register for the key they want to access and data is stored in key-value form



