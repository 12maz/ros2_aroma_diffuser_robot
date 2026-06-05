import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time


class PublisherNode(Node):
    def __init__(self):
        super().__init__('status_publisher')
        self.pub = self.create_publisher(String, 'robot_status', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.counter = 0
        self.get_logger().info('Publisher node started, publishing to robot_status at 1 Hz')

    def timer_callback(self):
        msg = String()
        msg.data = f"STATUS: operational | t={time.time():.1f} | count={self.counter}"
        self.pub.publish(msg)
        self.get_logger().info(f'Published: "{msg.data}"')
        self.counter += 1


def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
