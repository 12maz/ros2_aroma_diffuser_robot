import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    share_dir = get_package_share_directory('aroma_robot')
    rviz_config = os.path.join(share_dir, 'config', 'rviz_config.rviz')

    return LaunchDescription([
        Node(
            package='aroma_robot',
            executable='publisher_node',
            name='status_publisher',
            output='screen'
        ),
        Node(
            package='aroma_robot',
            executable='subscriber_node',
            name='status_subscriber',
            output='screen'
        ),
        Node(
            package='aroma_robot',
            executable='mission_controller',
            name='mission_controller',
            output='screen',
            parameters=[{'cycle_delay': 12.0}]
        ),
        Node(
            package='aroma_robot',
            executable='aroma_robot',
            name='aroma_robot_controller',
            output='screen'
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='map_to_odom',
            output='screen',
            arguments=['0', '0', '0', '0', '0', '0', 'map', 'odom']
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='odom_to_base_link',
            output='screen',
            arguments=['0', '0', '0', '0', '0', '0', 'odom', 'base_link']
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config]
        ),
    ])
