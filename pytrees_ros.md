# PyTrees ROS

## The Mock Robot
The essential features of mock robot include :
- Battery
- LED Strip
- Docking Action Server
- Move Base Action Server
- Rotation Action Server
- Safety Sensors Pipeline

Topic found in mock robot
![image](https://user-images.githubusercontent.com/64950661/146653146-00633c47-c9e3-4288-96b1-ed8c6b848b72.png)


### Tut 1 - Data Gathering
Behaviour - collect data data from a subscriber and stores result on blackboard
Data Gatherers assemble under the parallel at or near the very root of the tree so they may always trigger their update() ad be processed before any decision making behaviours elsewhere in the tree
![image](https://user-images.githubusercontent.com/64950661/146667184-4ae3dc56-488d-4df3-9b24-25db98fdb509.png)

```
 <node pkg="py_trees_ros" name="tree" type="tutorial_tree" args="one"/>
 ```
 We cant simply change the topic name of /battery/state to get a topic ont he blackboard!
 
 ## Trying with turtlesim
 Tasks divided : 
- [x] Custom board implementation with blackboard
- [x] Custom Action Server to rotate turtlesim
- [x] Put pose to blackboard
- [x] Use bt for actionclient to rotate turtlesim by 90 degrees
 
![image](https://user-images.githubusercontent.com/64950661/147112109-a8c91104-0e96-4af1-a484-132b4f950164.png)


Sites I referred to implement this:
* https://github.com/splintered-reality/py_trees_ros/tree/release/0.5.x
* https://github.com/splintered-reality/py_trees_ros/tree/release/0.5.x/scripts
* https://github.com/splintered-reality/py_trees_msgs
* https://github.com/splintered-reality/py_trees_ros/blob/release/0.5.x/py_trees_ros/tutorials/five.py
* http://docs.ros.org/en/melodic/api/py_trees_ros/html/tutorials.html#module-py_trees_ros.tutorials.five
* http://docs.ros.org/en/melodic/api/py_trees_ros/html/terminology.html#term-guard
