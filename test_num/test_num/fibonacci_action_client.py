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

    return self.action_client.send_goal_async(goal_msg) #저쪽 노드로 보냄

def main(args=None):
  rclpy.init(args=args)
  node = FibonacciActionClient()
  node.send_goal(25) #25가 타겟이 되어 골이 됨
  rclpy.spin_until_future_complete(node, future) #끝날때 까지 스핀
  node.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
