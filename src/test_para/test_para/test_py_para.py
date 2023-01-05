import rclpy
from rclpy.node import Node

class TParam(Node):
  def __init__(self):
    super().__init__('tparam')
    self.declare_parameter('my_para','내가만든파라미터') #첫번째 인자는 파라미터 이름, 두번쨰 인자는 value
    self.timer = self.create_timer(1, self.para)
    self.a = 'aaaaa'

  def para(self):
    my_para = self.get_parameter('my_para') # 이 코드는 객체의 주소를 반환함, 값 반환 X
    my_para = self.get_parameter('my_para').get_parameter_value() #다양한 값 반환
    my_para = self.get_parameter('my_para').get_parameter_value()._string_value #문자열만 반환
    my_para = self.get_parameter('my_para').get_parameter_value().string_value #문자열만 반환
    self.get_logger().info('파라미터를 출력합니다: {}'.format(my_para))
    self.get_logger().warn('파라미터를 출력합니다: {}'.format(my_para)) #노란색으로 로그 출력

def main(args = None):
  rclpy.init()
  node = TParam()
  rclpy.spin(node)
  rclpy.shutdown

if __name__ == '__main__':
  main()
