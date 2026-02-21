from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 1. 啟動官方的 turtlesim 節點
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim_node'
        ),
        # 2. 啟動你自定義的 turtle_controller 節點
        Node(
            package='my_robot_controller',
            executable='turtle_controller',
            name='turtle_controller'
        )
    ])
