from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='aroma_robot',
            executable='mission_controller',
            name='mission_controller',
            output='screen'
        ),
        Node(
            package='aroma_robot',
            executable='aroma_robot',
            name='aroma_robot_controller',
            output='screen'
        ),
    ])
