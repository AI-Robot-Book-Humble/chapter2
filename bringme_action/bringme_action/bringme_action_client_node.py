import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from airobot_interfaces.action import StringCommand

class BringmeActionClient(Node):
    def __init__(self):
        super().__init__('bringme_action_client_node')
        self._action_client = ActionClient(self, StringCommand, 'command')

    def send_goal(self, order):
        goal_msg = StringCommand.Goal()
        goal_msg.command = order
        self._action_client.wait_for_server()
        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg, feedback_callback=self.feedback_callback
        )
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('ゴールは拒否されました')
            return

        self.get_logger().info('ゴールが承認されました')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def feedback_callback(self, feedback_msg):
        self.get_logger().info(f'フィードバック: 進捗 {feedback_msg.process}%')

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f'最終結果: {result.answer}')
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    bringme_action_client = BringmeActionClient()

    order = input('何を取ってきますか：')
    bringme_action_client.send_goal(order)

    rclpy.spin(bringme_action_client)
