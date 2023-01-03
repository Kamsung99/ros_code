import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.qos import QoSProfile

class M_sub(Node):
  def __init__(self):
    super().__init__('time_subscriber')
    self.qos_profile = QoSProfile(depth = 10)
    self.message_subscriber = self.create_subscription(String, 'time', self.subsriber_message, qos_profile=self.qos_profile)

  def subsriber_message(self, msg):
    self.get_logger().info('Recived message: {}'.format(msg.data))

def main(args=None):
  rclpy.init(args=args)
  node = M_sub()
  try:
    rclpy.spin(node)
  except KeyboardInterrupt:
    node.get_logger().info('Keyboard interrupt!!!!')
  finally:
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
  main()
