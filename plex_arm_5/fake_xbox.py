# Emulate a fake controller for testing custom nodes
import rclpy
from rclpy.node import Node
from rclpy.clock import Clock, ClockType

from sensor_msgs.msg import Joy

# Fake an Xbox input via directly publishing to sensor_msgs/msg/Joy
class FakeXbox(Node):
    def __init__(self):
        super().__init__('fake_xbox')

        self.publisher = self.create_publisher(
            Joy,
            '/joy',
            10
        )

        self.timer = self.create_timer(
            0.05,
            self.timer_callback,
            clock=Clock(clock_type=ClockType.STEADY_TIME)
        )
        self.i = 0
    
    def timer_callback(self):
        msg = Joy()

        self.i += 1

        msg.axes = [0.0] * 6
        msg.buttons = [0] * 21

        self.publisher.publish(msg)


def main(args=None):
    rclpy.init()

    node = FakeXbox()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("Destroying nodes. Shutting down rclpy.")
        node.destroy_node()
        if rclpy.ok(): rclpy.shutdown()

if __name__ == '__main__':
    main()