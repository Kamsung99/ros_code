import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.qos import QoSProfile

class t_pub(Node):
  def __init__(self):
    super().__init__('time_publisher')
    self.qos_profile = QoSProfile(depth = 20)
    self.time_publisher = self.create_publisher(String, 'time', qos_profile=self.qos_profile)
    self.timer = self.create_timer(1, self.t_publisher)
    self.count = 0

  def t_publisher(self):
    msg = String()
    msg.data = f'time {self.count}'
    self.time_publisher.publish(msg)
    self.get_logger().info(f'Published message: {msg.data}')
    self.count += 1

def main(args=None):
  rclpy.init(args=args)
  node = t_pub()
  try:
    rclpy.spin(node)
  except KeyboardInterrupt:
    node.get_logger().info('Keyboard interrupt!!!!')
  finally:
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
  main()
