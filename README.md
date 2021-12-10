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


