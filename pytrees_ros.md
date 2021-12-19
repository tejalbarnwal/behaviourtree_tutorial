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
 
