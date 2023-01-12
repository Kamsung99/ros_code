from launch import LaunchDescription
from launch_ros.actions import Node #rclpy.node에 있는 노드와 다름

def generate_launch_description():
  return LaunchDescription(
    [
    Node( #네임 스페이스는 선택사항이지만 권고
      package='turtlesim',
      namespace='ns1',
      executable='turtlesim_node',
      name = 'sim'
    ),
  Node(
    package='turtlesim',
    namespace='ns2',
    executable='turtlesim_node',
    name = 'sim'
    ),
  Node(
    package='turtlesim',
    executable='turtlesim_node',
    remappings= [ #이름을 강제로 변경
      ('/input/pose','turtlesim/turtle1/pose'),
      ('/output/pose','turtlesim2/turtle1/cmd_vel')
      ]
    )
  ]
  )
