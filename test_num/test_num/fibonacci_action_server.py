import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from test_interfaces.action import Fibonacci

class FibonacciActionServer(Node):
  def __init__(self):
    super().__init__('fibonacci_action_server')
    self.action_server = ActionServer(Fibonacci,'fibonacci',self.fibo_call)

  def fibo_call(self, goal_handle):
    feedback_msg = Fibonacci.Feedback() #Fibonacci 액션의 피드백 생성
    sequence = [0, 1]
    for i in range(1, goal_handle.request.number):
      sequence.append(sequence[i]+ sequence[[i-1]]) #피보나치 수열
    self.get_logger().info('Feedback {}'.format(feedback_msg.pary_array))
    goal_handle.succeed() #골이 완성됬는지 아닌지 확인 할 수 있음
    goal_handle.publish_feedback(feedback_msg) # publish 실행
    result= Fibonacci.Result()
    return result

def main(args=None):
  rclpy.init(args=args)
  node = FibonacciActionServer()
  try:
    rclpy.spin(node)
  except KeyboardInterrupt:
    node.get_logger().info('Keyboard interrupt!!!!')
  finally:
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
  main()
