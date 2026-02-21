# ROS 2 Humble Learning Project
This repository documents the progress and source code developed during the ROS 2 Humble tutorial series. It focuses on the fundamental concepts of ROS 2, including nodes, topics, services, and launch files.

## Development Environment
- Operating System: Ubuntu 22.04 LTS
- ROS 2 Version: Humble
- Programming Language: Python 3.10

## Dependencies
This project requires the official ROS 2 `ros_tutorials` package for simulation and testing purposes.

```
git clone https://github.com/ros/ros_tutorials.git -b humble
```

## Installation and Setup
To set up this workspace and compile the packages:
1. Create Workspace:
```
mkdir -p ~/ros2_ws/src
```
```
cd ~/ros2_ws/src
```
2. Clone Repository:
```
git clone https://github.com/haochy/ros2_learning.git
```
3. Install Dependencies:
```
cd ~/ros2_ws
```
```
rosdep install -i --from-path src --rosdistro humble -y
```
4. Build Workspace:
```
colcon build --symlink-install
```
```
source install/setup.bash
```

## Packages
### my_robot_controller
A custom package containing experimental nodes for robot control.

### Nodes
- `my_first_node.py`: Introduction to ROS 2 Node structure and logging.
- `draw_circle.py`: Controls the `turtlesim` node to move in a circular trajectory by publishing to the `/turtle1/cmd_vel` topic.
- `pose_sub.py`: Subscribes to `/turtle1/pose` to monitor real-time coordinate data.
- `turtle_controller.py`: A closed-loop controller that manages turtle movements based on feedback and specific logic.
- `param_controller.py`: Demonstrates the use of ROS 2 parameters for dynamic node configuration.

### Launch Files
- `turtle_launch.py`: Automates the execution of the `turtlesim_node` and the custom controller nodes simultaneously.

## Usage
To run the main controller:
1. Start the simulation environment:
```
ros2 run turtlesim turtlesim_node
```
2. Execute the controller node:
```
ros2 run my_robot_controller turtle_controller
```
Alternatively, use the launch file:
```
ros2 launch my_robot_controller turtle_launch.py
```

## References
- Tutorial Series: [ROS2 Tutorial for Beginners (YouTube)](https://www.youtube.com/watch?v=0aPbWsyENA8&list=PLLSegLrePWgJudpPUof4-nVFHGkB62Izy)
- Official Documentation: [ROS 2 Humble Documentation](https://docs.ros.org/en/humble/)
