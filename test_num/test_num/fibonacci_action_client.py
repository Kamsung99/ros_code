import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from test_interfaces.action import Fibonacci

class FibonacciActionClient(Node):
  def __init__(self):
    super().__init__('fibonacci_action_client')
    self.action_client = ActionClient(self,Fibonacci,'fibonacci')

  def send_goal(self, target):
    goal_msg = Fibonacci.Goal()
    goal_msg.number = target

    self.action_client.wait_for_server()

    self.send_goal_future = self.action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback) #중간중간 콜백이 옴

    self.send_goal_future.add_done_callback(self.goal_response_callback) #골이 완료처리 되면 한번 옴

  def feedback_callback(self, feedback_msg):
    feedback = feedback_msg.feedback
    self.get_logger().info('Received feedback: {}'.format(feedback.part_array))

  def goal_response_callback(self, future):
    goal_handle = future.result()
    if not goal_handle.accepted:
      self.get_logger().info('Goal Rejected')
      return #저쪽 노드로 보냄

    self.get_logger().info('Goal accepted!')

    self.get_result_future = goal_handle.get_result_async()
    self.get_result_future.add_done_callback(self.get_result_callback)

  def get_result_callback(self, future):
    result = future.result().result
    status = future.result().status #메세지 상태를 확인 가능 (성공 하였는지, 실패 하였는지)
    self.get_logger().info('Result: {}'.format(result.array))
    rclpy.shutdown()

def main(args=None):
  rclpy.init(args=args)
  node = FibonacciActionClient()
  node.send_goal(25) #25가 타겟이 되어 골이 됨
  rclpy.spin(node)

if __name__ == '__main__':
  main()
