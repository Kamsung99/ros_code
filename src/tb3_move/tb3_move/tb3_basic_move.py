import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile

class Tb3_m_pub(Node):
  def __init__(self):
    super().__init__('tb3_move')
    self.qos_profile = QoSProfile(depth = 10)
    self.tb3_message_publisher = self.create_publisher(Twist, 'cmd_vel', qos_profile=self.qos_profile)
    self.timer = self.create_timer(0.1, self.tb3_move_go_publisher)

  def tb3_move_go_publisher(self):
    msg = Twist()
    msg.linear.x = 0.05
    msg.angular.z = 0.0

    msg.linear.x += 0.01

    self.tb3_message_publisher.publish(msg)
    self.get_logger().info(f'Published message: {msg.linear.x}, {msg.linear.z}')

def main(args=None):
  rclpy.init(args=args)
  node = Tb3_m_pub()
  try:
    rclpy.spin(node)
  except KeyboardInterrupt:
    node.get_logger().info('Keyboard interrupt!!!!')
  finally:
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
  main()
