import rclpy
from rclpy.node import Node
from airobot_interfaces.srv import StringCommand


class BringmeClient(Node):
    def __init__(self):  # コンストラクタ
        super().__init__('bringme_client_node')
        self.client = self.create_client(StringCommand, 'command') # クライアントの生成
        # サービスが利用できるまで待機
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('サービスは利用できません．待機中...')        
        self.request = StringCommand.Request()  # リクエストのインスタンス生成

    def send_request(self, order):  # リクエストの送信メソッド
        self.request.command = order  # リクエストに値の代入   
        self.future = self.client.call_async(self.request) # サービスのリクエスト


def main():
    rclpy.init()
    node = BringmeClient()
    order = input('何を取ってきますか：')
    node.send_request(order)

    while rclpy.ok():
        rclpy.spin_once(node)  # ノードを1回スピンして、コールバックを処理する
        if node.future.done():  # サービスの処理が完了したかを確認
            try:
                response = node.future.result()  # サービスの結果を取得                  
            except Exception as e:
                node.get_logger().info(f"サービスのよび出しは失敗しました．{e}")
            else:                
                node.get_logger().info( # 結果の表示
                    f"\nリクエスト:{node.request.command} -> レスポンス: {response.answer}")
                break
    node.destroy_node()  
    rclpy.shutdown()
