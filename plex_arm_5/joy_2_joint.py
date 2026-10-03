# ROS Client Library Python
import rclpy
from rclpy.node import Node

# Messages
from std_msgs.msg import String     # for logging
from sensor_msgs.msg import Joy
from control_msgs.msg import JointJog

class Joy2Joint(Node):
    def __init__(self):
        super().__init__('joy_2_joint')

        # get Joy messages
        self.subscription = self.create_subscription(
            Joy,
            '/joy',
            self.joy_callback,
            10
        )

        # publish JointJog messages to servo_node
        self.publisher = self.create_publisher(
            JointJog,
            '/servo_node/delta_joint_cmds',
            10
        )

    def joy_callback(self, msg):
        # JointJog instance
        joint_msg = JointJog()
        joint_msg.header.stamp = self.get_clock().now().to_msg()
        joint_msg.header.frame_id = 'base-link'
        
        # set joint names
        # joint_msg.joint_names = [
        #     'joint1',
        #     'joint2',
        #     'joint3',
        #     'joint4',
        #     'joint5',
        #     'joint6'
        # ]

        # set velocities
        joint_msg.velocities = [
            msg.axes[0], # Left Stick: left-right
            msg.axes[1], # Left Stick: up-down
            msg.axes[2], # Right Stick: left-right
            msg.axes[3], # Right Stick: up-down
            msg.axes[4], # Left Trigger
            msg.axes[5]  # Right Trigger
        ]

        # set displacements
        joint_msg.displacements = []

        # set duration
        joint_msg.duration = 0.0
        
        self.publisher.publish(joint_msg)

def main(args=None):
    rclpy.init(args=args)

    node = Joy2Joint()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("Destroying nodes. Shutting down rclpy.")
        node.destroy_node()
        if rclpy.ok(): rclpy.shutdown()

if __name__ == '__main__':
    main()