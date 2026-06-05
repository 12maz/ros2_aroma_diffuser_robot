import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped


class AromaRobot(Node):
    def __init__(self):
        super().__init__('aroma_robot_controller')
        self.status_publisher = self.create_publisher(String, 'robot_status', 10)
        self.command_subscriber = self.create_subscription(String, 'aroma_command', self.command_callback, 10)
        self.goal_subscriber = self.create_subscription(PoseStamped, 'mission/goal', self.goal_callback, 10)

        self.diffuser_state = 'OFF'
        self.last_goal = None
        self.status_timer = self.create_timer(1.0, self.publish_status)
        self.get_logger().info('Aroma robot controller initialized')

    def command_callback(self, msg: String):
        self.diffuser_state = msg.data.split(':')[-1].strip()
        self.get_logger().info(f'Received aroma command: {msg.data}')

    def goal_callback(self, msg: PoseStamped):
        self.last_goal = msg
        self.get_logger().info(
            f"Received mission goal at x={msg.pose.position.x:.2f}, y={msg.pose.position.y:.2f}, diffuser={self.diffuser_state}"
        )

    def publish_status(self):
        status = String()
        location = 'unknown'
        if self.last_goal is not None:
            location = f"{self.last_goal.pose.position.x:.2f},{self.last_goal.pose.position.y:.2f}"
        status.data = f"STATE: active | location={location} | diffuser={self.diffuser_state}"
        self.status_publisher.publish(status)

    def destroy_node(self):
        self.get_logger().info('Shutting down aroma robot controller')
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = AromaRobot()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
