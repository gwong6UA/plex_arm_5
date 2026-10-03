# Launch file for testing translator node and joy_node
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description(args=None):
    return LaunchDescription([
        Node(
            package='plex_arm_5',
            executable='joy_2_joint',
            name='joy_2_joint',
            # namespace='',
            # parameters=[],        here for reference
            # remappings=[],
            output='screen',
        ),
        Node(
            package='plex_arm_5',
            executable='fake_xbox',
            name='fake_xbox',
            output='screen',
        )
    ])