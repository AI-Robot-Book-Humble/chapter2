import time
import threading
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, GoalResponse, CancelResponse
from rclpy.callback_groups import ReentrantCallbackGroup
from airobot_interfaces.action import StringCommand  # アクションファイルのインポート

class BringmeActionServer(Node):
    def __init__(self):
        super().__init__('bringme_action_server')
        self._action_server = ActionServer(
            self,
            StringCommand,
            'command',
            execute_callback=self.execute_callback,
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback,
            handle_accepted_callback=self.handle_accepted_callback,
            callback_group=ReentrantCallbackGroup()
        )
        self.food = ['apple', 'banana', 'candy']

    def goal_callback(self, goal_request):
        self.get_logger().info(f"ゴールリクエストが来ました．コマンド: {goal_request.command}")
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle):
        self.get_logger().info(f"キャンセルリクエストを受け取りました．")
        return CancelResponse.ACCEPT

    def handle_accepted_callback(self, goal_handle):
        self.get_logger().info("ゴールが承認されました。非同期で処理を開始します。")
        threading.Thread(target=self.execute_callback, args=(goal_handle,)).start()

    def execute_callback(self, goal_handle):
        feedback_msg = StringCommand.Feedback()
        feedback_msg.process = 0

        for i in range(5):
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info('ゴールがキャンセルされました。')
                return StringCommand.Result()

            time.sleep(1)
            feedback_msg.process += 20
            self.get_logger().info(f"フィードバック送信中: {feedback_msg.process}%")
            goal_handle.publish_feedback(feedback_msg)

        result = StringCommand.Result()
        for item in self.food:
            if item in goal_handle.request.command:
                result.answer = 'はい，これです．'
                goal_handle.succeed()
                self.get_logger().info(f"ゴールの結果: {result.answer}")
                return result
        
        result.answer = '見つけることができませんでした．'
        goal_handle.succeed()
        self.get_logger().info(f"ゴールの結果: {result.answer}")
        return result

def main(args=None):
    rclpy.init(args=args)
    bringme_action_server = BringmeActionServer()
    rclpy.spin(bringme_action_server)
    bringme_action_server.destroy_node()
    rclpy.shutdown()
