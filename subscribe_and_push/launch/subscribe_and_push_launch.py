from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
  subscribe_and_push_node = Node(
    package='subscribe_and_push',
    executable='subscribe_and_push',
  )

  ld = LaunchDescription()
  ld.add_action(subscribe_and_push_node)

  return ld