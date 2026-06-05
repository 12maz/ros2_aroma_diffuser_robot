import yaml
from pathlib import Path

import rclpy
from rclpy.node import Node
from ament_index_python.packages import get_package_share_directory
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String


class MissionController(Node):
    def __init__(self):
        super().__init__('mission_controller')
        self.declare_parameter('cycle_delay', 10.0)
        self.cycle_delay = self.get_parameter('cycle_delay').value

        self.goal_publisher = self.create_publisher(PoseStamped, 'mission/goal', 10)
        self.command_publisher = self.create_publisher(String, 'aroma_command', 10)

        self.waypoints = self.load_waypoints()
        self.current_index = 0
        self.get_logger().info(f'Loaded {len(self.waypoints)} waypoints for the mission')

        self.timer = self.create_timer(self.cycle_delay, self.publish_next_waypoint)

    def load_waypoints(self):
        try:
            share_dir = get_package_share_directory('aroma_robot')
            yaml_path = Path(share_dir) / 'config' / 'waypoints.yaml'
            with open(yaml_path, 'r', encoding='utf-8') as file:
                config = yaml.safe_load(file)
                return config.get('waypoints', [])
        except Exception as ex:
            self.get_logger().error(f'Failed to load waypoints.yaml: {ex}')
            return []

    def publish_next_waypoint(self):
        if not self.waypoints:
            self.get_logger().warn('No waypoints available for mission')
            return

        waypoint = self.waypoints[self.current_index]
        goal_msg = PoseStamped()
        goal_msg.header.stamp = self.get_clock().now().to_msg()
        goal_msg.header.frame_id = waypoint.get('frame_id', 'map')
        goal_msg.pose.position.x = waypoint['position']['x']
        goal_msg.pose.position.y = waypoint['position']['y']
        goal_msg.pose.position.z = waypoint['position'].get('z', 0.0)
        goal_msg.pose.orientation.x = waypoint['orientation']['x']
        goal_msg.pose.orientation.y = waypoint['orientation']['y']
        goal_msg.pose.orientation.z = waypoint['orientation']['z']
        goal_msg.pose.orientation.w = waypoint['orientation']['w']

        self.goal_publisher.publish(goal_msg)
        self.get_logger().info(f"Published waypoint '{waypoint['name']}' as mission goal")

        command_msg = String()
        command_msg.data = f"DIFFUSER: {waypoint.get('aroma_command', 'OFF')}"
        self.command_publisher.publish(command_msg)
        self.get_logger().info(f"Published aroma command: {command_msg.data}")

        self.current_index = (self.current_index + 1) % len(self.waypoints)


def main(args=None):
    rclpy.init(args=args)
    node = MissionController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
