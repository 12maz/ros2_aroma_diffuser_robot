# Aroma Diffuser Robot Project Final Report

## Project Summary

This project implements a ROS 2 package named `aroma_robot` for an autonomous aroma diffuser robot mission. The architecture includes publishing and subscribing nodes, a mission controller that cycles through goal waypoints, an aroma robot controller node that simulates diffuser state and mission status, and configuration assets for RViz, SLAM Toolbox, and Nav2.

## Package Structure

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

## Node Roles

- `publisher_node`: broadcasts robot status messages on `robot_status`.
- `subscriber_node`: listens to `robot_status` and logs updates.
- `mission_controller`: loads waypoint definitions and publishes mission goals to `mission/goal`, while issuing aroma diffuser commands to `aroma_command`.
- `aroma_robot`: receives goals and dispenser commands, then publishes active robot state and diffuser status.

## Launch Configurations

- `sim_launch.py`: Starts the publisher, subscriber, mission controller, and aroma robot controller for local simulation.
- `mission_launch.py`: Launches mission-specific nodes only.
- `slam_nav_launch.py`: Integrates SLAM Toolbox and Nav2 bringup for mapping and navigation.

## Configuration Assets

- `waypoints.yaml`: Defines mission waypoints and associated diffuser state.
- `rviz_config.rviz`: Provides a baseline RViz visualization with map, robot model, TF, and goal pose.
- `slam_toolbox_params.yaml`: Configures the SLAM Toolbox node.
- `nav2_params.yaml`: Contains navigation stack parameters for AMCL, map server, planner, and local controller.
- `maps/arena_map.*`: Contains a placeholder occupancy grid map for Nav2 and mapping tests.

## Usage

1. Build the package from the root workspace:
   ```bash
   colcon build --packages-select aroma_robot
   ```
2. Source the build environment:
   ```bash
   . install/setup.bash
   ```
3. Launch the simulation example:
   ```bash
   ros2 launch aroma_robot sim_launch.py
   ```
4. Launch the mission controller only:
   ```bash
   ros2 launch aroma_robot mission_launch.py
   ```
5. Launch SLAM and navigation:
   ```bash
   ros2 launch aroma_robot slam_nav_launch.py
   ```

## Conclusion

The generated repository now includes full ROS 2 package assets for an aroma diffuser robot mission, with node implementations, navigation and mapping configuration, and project documentation. This provides a complete starting point for ROS 2 system development and integration testing.
