import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SubscriberNode(Node):
    def __init__(self):
        super().__init__('status_subscriber')
        self.sub = self.create_subscription(String, 'robot_status', self.listener_callback, 10)
        self.get_logger().info('Subscriber node started, listening to robot_status')

    def listener_callback(self, msg: String):
        # Simple processing: print and show a parsed status
        text = msg.data
        self.get_logger().info(f'Received robot status: {text}')


def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
