from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, TextSubstitution
from launch_ros.actions import Node #rclpy.node에 있는 노드와 다름
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
  my_para_de = DeclareLaunchArgument('my_para_launch',default_value=TextSubstitution(text='default_para'))

  para_node = Node(#네임 스페이스는 선택사항이지만 권고
        package='test_para',
        executable='tp',
        parameters=[{
          "my_para": LaunchConfiguration('my_para_launch')}]
        )
  return LaunchDescription(
    [
      my_para_de,
      para_node
    ]
  )
