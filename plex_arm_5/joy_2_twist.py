# ROS Client Library Python
import rclpy
from rclpy.node import Node

# Messages
from std_msgs.msg import String     # for logging
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist, TwistStamped

class Joy2Twist(Node):
    """Listen for sensor_msgs/msg/Joy and convert to geometry_msgs/msg/Twist"""
    def __init__(self):
        """
        Initialize a node 'joy_2_twist' subscription to topic '/joy' and
        publishes geometry_msgs/msg/Twist to '/cmd_vel'.
        """
        super().__init__('joy_2_twist')

        self.subscription = self.create_subscription(
            Joy,
            '/joy',
            self.joy_callback,
            10
        )
        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

    def joy_callback(self, msg):
        twist_msg = TwistStamped()     # new Twist msg

        self.get_logger().info('Received Joy Message')
        # geometry_msgs/msg/TwistStamped {
        #     Twist twist
        # }
        # geometry_msgs/msg/Twist {
        #     Vector3 linear
        #     Vector3 angular
        # }
        # msg = sensor_msgs/msg/Joy {
        #     float32[] axes
        #     int32[] buttons
        # }
        # Vector3 {
        #     float64 x,
        #     float64 y,
        #     float64 z
        # }

        # Axes = [6]
        # do something for twist_msg
        # twist_msg.twist.linear.x = axes[#]

        # Buttons = [21]
        # do something for twist_msg

        self.publisher.publish(twist_msg)
        self.get_logger().info('Published Twist Message')

def main(args=None):
    rclpy.init(args=args)

    node = Joy2Twist()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("\nDestroying nodes. Shutting down rclpy.")
        node.destroy_node()
        if rclpy.ok(): rclpy.shutdown()

if __name__ == '__main__':
    main()