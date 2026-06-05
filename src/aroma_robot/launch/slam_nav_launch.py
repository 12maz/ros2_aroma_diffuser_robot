import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    aroma_share = get_package_share_directory('aroma_robot')
    nav2_share = get_package_share_directory('nav2_bringup')

    nav2_launch_file = os.path.join(nav2_share, 'launch', 'bringup_launch.py')
    nav2_params = os.path.join(aroma_share, 'config', 'nav2_params.yaml')
    slam_params = os.path.join(aroma_share, 'config', 'slam_toolbox_params.yaml')
    rviz_config = os.path.join(aroma_share, 'config', 'rviz_config.rviz')

    return LaunchDescription([
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
            package='slam_toolbox',
            executable='sync_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[slam_params],
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(nav2_launch_file),
            launch_arguments={
                'params_file': nav2_params,
                'map': os.path.join(aroma_share, 'maps', 'arena_map.yaml'),
            }.items(),
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config]
        ),
    ])
