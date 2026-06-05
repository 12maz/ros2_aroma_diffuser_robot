# ROS 2 Aroma Diffuser Robot

This repository contains a ROS 2 package named `aroma_robot` designed for an autonomous aroma diffuser robot mission. The project includes ROS 2 nodes, launch files, SLAM Toolbox and Nav2 configuration, map assets, and RViz visualization setup.

## Contents

- `src/aroma_robot/package.xml`
- `src/aroma_robot/setup.py`
- `src/aroma_robot/aroma_robot/publisher_node.py`
- `src/aroma_robot/aroma_robot/subscriber_node.py`
- `src/aroma_robot/aroma_robot/mission_controller.py`
- `src/aroma_robot/aroma_robot/aroma_robot.py`
- `src/aroma_robot/launch/sim_launch.py`
- `src/aroma_robot/launch/mission_launch.py`
- `src/aroma_robot/launch/slam_nav_launch.py`
- `src/aroma_robot/config/waypoints.yaml`
- `src/aroma_robot/config/rviz_config.rviz`
- `src/aroma_robot/config/slam_toolbox_params.yaml`
- `src/aroma_robot/config/nav2_params.yaml`
- `src/aroma_robot/maps/arena_map.yaml`
- `src/aroma_robot/maps/arena_map.pgm`

## Build Instructions

From the workspace root:

```bash
colcon build --packages-select aroma_robot
. install/setup.bash
```

## Run Examples

- Launch the simulated mission stack:
  ```bash
  ros2 launch aroma_robot sim_launch.py
  ```
- Launch mission-only components:
  ```bash
  ros2 launch aroma_robot mission_launch.py
  ```
- Launch SLAM and Nav2 integration:
  ```bash
  ros2 launch aroma_robot slam_nav_launch.py
  ```

## Notes

This repository includes complete ROS 2 assets for mission sequencing, SLAM Toolbox mapping, Nav2 path planning, and RViz visualization. The `sim_launch.py` file starts the mission controller, a simple aroma robot controller, a status publisher, and a status subscriber, plus static transform publishers and RViz support for local simulation.
