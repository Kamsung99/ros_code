import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Header
from rclpy.qos import QoSProfile

class MT_sub(Node):
  def __init__(self):
    super().__init__('message_subscriber')
    self.qos_profile = QoSProfile(depth = 10)
    self.message_subscriber = self.create_subscription(String, 'message', self.subsriber_message, qos_profile=self.qos_profile)
    self.timer_subscriber = self.create_subscription(Header, 'time', self.subsriber_time, qos_profile=self.qos_profile)

  def subsriber_message(self, msg):
    self.get_logger().info('Recived message: {}'.format(msg.data))

  def subsriber_time(self, msg):
    self.get_logger().info('Recived message: {}'.format(msg.stamp))

def main(args=None):
  rclpy.init(args=args)
  node = MT_sub()
  try:
    rclpy.spin(node)
  except KeyboardInterrupt:
    node.get_logger().info('Keyboard interrupt!!!!')
  finally:
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
  main()
