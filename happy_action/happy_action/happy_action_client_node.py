import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from happy_action_interfaces.action import Happy


class HappyActionClient(Node):
    def __init__(self):
        super().__init__('happy_action_client')
        # アクションクライアントの作成（ノードオブジェクト,アクション型，アクション名）
        self._action_client = ActionClient(self, Happy, 'happy')

    def send_goal(self, action_no):
        goal_msg = Happy.Goal()  # ゴールメッセージ型のインスタンスを作成
        goal_msg.action_no = action_no  # ゴールメッセージのaction_noに値を設定
        self._action_client.wait_for_server()  # アクションサーバが利用可能になるまで待機
        # 非同期でゴールをアクションサーバに送信し，フィードバックを受け取るコールバックを設定
        self._send_goal_future = self._action_client.send_goal_async(goal_msg,
                    feedback_callback=self.feedback_callback)
        # ゴール送信の結果を受け取るためのコールバックを設定 
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()  # ゴールハンドルの取得
        if not goal_handle.accepted:  # ゴールが受理されなかった場合
            self.get_logger().info('ゴールが拒否されました．')
            return
        self.get_logger().info('ゴールが承認されました.')
        # ゴールの結果を非同期で取得，結果が得られたらコールバックを呼び出す
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result  # ゴールの結果を取得
        self.get_logger().info(f'結果：{result.result}')
         
    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback  # フィードバックメッセージの取得
        self.get_logger().info(f'フィードバックを受信：残り{feedback.remaining_time}秒')


def main(args=None):
    rclpy.init(args=args)  # ROS2の通信の初期化
    action_client = HappyActionClient()  # ノードの生成
    action_client.send_goal(1)  # アクション番号1のゴールを送信
    action_client.send_goal(5)  # アクション番号5のゴールを送信
    action_client.send_goal(7)  # アクション番号7のゴールを送信
    rclpy.spin(action_client)  # ノードをコールバックを繰り返し呼び出し，スピンが破棄されるまで待機
    action_client.destroy_node()  # ノードの破棄
    rclpy.shutdown()  # ROS2通信の終了処理
