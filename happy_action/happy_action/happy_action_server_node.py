import random
import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer   # アクションサーバクラスのインポート
from happy_action_interfaces.action import Happy  # カスタムアクション定義のインポート


class HappyActionServer(Node):
    def __init__(self):
        super().__init__('happy_action_server')  # ノード名をhappy_action_serverで初期化
        # アクションサーバの作成(アクション型, アクション名, コールバック関数)
        self._action_server = ActionServer(
            self, Happy, 'happy', self.execute_callback)
        self.happy_actions = ({
            1:'他の人へ親切な行動をします．',
            2:'他の人とつながる行動をします．',
            3:'健康になるために運動をします．',
            4:'マインドフルネスをします．',
            5:'新しいことに挑戦します．',
            6:'ゴールを決めて，まず１歩を踏み出します．',
            7:'レジリエンス（回復力）をつけます．',
            8:'物事の良い面を見ます．',
            9:'人は皆違っていることを受け入れます．',
            10:'皆で協力して世界を良くします．'})

    def execute_callback(self, goal_handle):  # ゴールを受信したときに呼び出されるコールバック
        self.get_logger().info('ゴールを処理中...')

        feedback_msg = Happy.Feedback()  # フィードバックメッセージのインスタンスを作成
        feedback_msg.remaining_time = random.randrange(1,10)  # 残り時間をランダムに作成

        no = goal_handle.request.action_no  # ゴールからアクション番号を取得
        self.get_logger().info(f'ゴールを受信：[{no}番] {self.happy_actions[no]}')   
        
        while True:  # ゴール処理
            if  feedback_msg.remaining_time == 0:
                self.get_logger().info('ゴールの処理は終了しました．')
                break
            else:
                feedback_msg.remaining_time -= 1
                self.get_logger().info(f'フィードバック：残り{feedback_msg.remaining_time}秒')
                goal_handle.publish_feedback(feedback_msg)  # フィードバックをパブリッシュ
                time.sleep(1)
            
        goal_handle.succeed()  # ゴールの成功を通知
        result = Happy.Result()  # 結果メッセージのインスタンスを作成
        if feedback_msg.remaining_time == 0:  # 結果メッセージの内容を設定
            result.result = 'とてもハッピーになりました．'
        else:
            result.result = '少しハッピーになりました．'
        self.get_logger().info(f'結果の返信：{result.result}')   # 結果をログに出力
        return result  # 結果の返却 

def main():
    rclpy.init()
    happy_action_server = HappyActionServer()
    try:
        rclpy.spin(happy_action_server)
    except KeyBoardInterrupt:
        pass
    finally:
        happy_action_server.destroy_node()
        rclpy.shutdown()
