from setuptools import setup

package_name = 'aroma_robot'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', [
            'launch/sim_launch.py',
            'launch/slam_nav_launch.py',
            'launch/mission_launch.py',
        ]),
        ('share/' + package_name + '/config', [
            'config/waypoints.yaml',
            'config/rviz_config.rviz',
            'config/slam_toolbox_params.yaml',
            'config/nav2_params.yaml',
        ]),
        ('share/' + package_name + '/maps', [
            'maps/arena_map.yaml',
            'maps/arena_map.pgm',
        ]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='University Student',
    maintainer_email='you@example.com',
    description='Autonomous Navigation & Aroma Diffuser Robot Mission',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher_node = aroma_robot.publisher_node:main',
            'subscriber_node = aroma_robot.subscriber_node:main',
            'mission_controller = aroma_robot.mission_controller:main',
            'aroma_robot = aroma_robot.aroma_robot:main',
        ],
    },
)
