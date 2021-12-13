# behaviourtree_tutorial

This repository is meant to practice actionlib tutorials and trying out a small PS based on ros pytrees.

## ActionLib Package
The `actionlib` package allows to create servers(to execute long running goals) and clients(to send request). The main difference btw a service and action lies in the fact that action allows us to can cel the request during the execution phase(preempting the goal) and gives a periodic feedback about how the request is progressing.

### `ROS Action Protocol`
The ROS msgs on which actionclient and action server communicate is characterized by an action specification. This action specification defines 3 things- goal, feedback and result! When the pkg is compiled all of these result into different msg types.

* The action specification file is written down in a specifc format in .action file. They are generally defined in action directory in the pkg. They syntax for the usage-
``` 
# define the goal
uint32 goal_fromCtoS
---
# define the result
uint32 result_fromStoC
---
# define a feedback msg
float32 feedback_fromStoC

```
This .action file results into creation of 6 msg types for rostopics.
These msg types are automatically generated when you specify the rquired dependencies in the CMakeLists.txt and package.xml.[Details Here](http://wiki.ros.org/actionlib)

Suppose you define teju.action file. Then the following msg types would be automatically generated-
- tejuAction.msg
- tejuActionGoal.msg
- tejuActionResult.msg
- tejuActionFeedback.msg
- tejuGoal.msg
- tejuResult.msg
- tejuFeedback

Goal, Result, Feedback
![image](https://user-images.githubusercontent.com/64950661/145539655-c6369770-9b4d-4903-9536-016f85bd7e2d.png)

ActionGoal
![image](https://user-images.githubusercontent.com/64950661/145539145-7dc7620e-cd55-4f59-be8a-b5e1ef73a4a4.png)

ActionFeedback
![image](https://user-images.githubusercontent.com/64950661/145539279-b65ba529-fdb1-42a7-b1e2-d9aff65d53ab.png)

ActionResult
![image](https://user-images.githubusercontent.com/64950661/145539308-44bce033-c223-469a-945d-6e2c7b467085.png)

Action (run - rosmsg show behaviourtree_tutorial/naturalnumAction)
```
behaviourtree_tutorial/naturalnumActionGoal action_goal
  std_msgs/Header header
    uint32 seq
    time stamp
    string frame_id
  actionlib_msgs/GoalID goal_id
    time stamp
    string id
  behaviourtree_tutorial/naturalnumGoal goal
    int32 num_steps
behaviourtree_tutorial/naturalnumActionResult action_result
  std_msgs/Header header
    uint32 seq
    time stamp
    string frame_id
  actionlib_msgs/GoalStatus status
    uint8 PENDING=0
    uint8 ACTIVE=1
    uint8 PREEMPTED=2
    uint8 SUCCEEDED=3
    uint8 ABORTED=4
    uint8 REJECTED=5
    uint8 PREEMPTING=6
    uint8 RECALLING=7
    uint8 RECALLED=8
    uint8 LOST=9
    actionlib_msgs/GoalID goal_id
      time stamp
      string id
    uint8 status
    string text
  behaviourtree_tutorial/naturalnumResult result
    int32[] sequence
behaviourtree_tutorial/naturalnumActionFeedback action_feedback
  std_msgs/Header header
    uint32 seq
    time stamp
    string frame_id
  actionlib_msgs/GoalStatus status
    uint8 PENDING=0
    uint8 ACTIVE=1
    uint8 PREEMPTED=2
    uint8 SUCCEEDED=3
    uint8 ABORTED=4
    uint8 REJECTED=5
    uint8 PREEMPTING=6
    uint8 RECALLING=7
    uint8 RECALLED=8
    uint8 LOST=9
    actionlib_msgs/GoalID goal_id
      time stamp
      string id
    uint8 status
    string text
  behaviourtree_tutorial/naturalnumFeedback feedback
    int32[] sequence
```

The description regarding to the auto_start flag could be found [here](https://answers.ros.org/question/107126/actionlib-auto_start-parameter/) 


Full API Reference for [simpleActionServer](https://docs.ros.org/en/api/actionlib/html/classactionlib_1_1simple__action__server_1_1SimpleActionServer.html)

Full API Reference for [simpleActionClient](https://docs.ros.org/en/api/actionlib/html/classactionlib_1_1simple__action__client_1_1SimpleActionClient.html)

### Note
1. Found that action name that you specify in the action server should be same the as the action name that you specify in the action client!
Henceforth, in the tutorial given at ROS wiki didnt explicitly mention this but , "fibonacci" is the one!
In the tutorial scripts we created, "NaturalNumberListNode" is the one! Further, this is the action name.
The action client and server communicate over a set of topics, described in the actionlib protocol. The action name describes the namespace containing these topics, and the action specification message describes what messages should be passed along these topics.

![image](https://user-images.githubusercontent.com/64950661/145781778-62b6a036-7e5d-4c99-9860-3b492f5197c3.png)

2. We can also use [axclient from actionlib](http://wiki.ros.org/actionlib_tutorials/Tutorials/Calling%20Action%20Server%20without%20Action%20Client) which provides a graphical way to send the goals to the action server.

## Doubts 
- [Auto_Start Flag](https://www.reddit.com/r/robotics/comments/rd4cje/ros_action_server/)



