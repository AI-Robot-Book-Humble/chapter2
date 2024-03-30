import rclpy
from rclpy.node import Node
from rcl_interfaces.srv import GetParameters

# ParameterClientクラスを定義します。Nodeクラスを継承しています。
class ParameterClient(Node):
    def __init__(self):
        # ノード名を'parameter_client'に設定します。
        super().__init__('happy_parameter_client')
        # パラメータサーバーのサービスに接続するクライアントを作成します。
        self.client = self.create_client(GetParameters, '/parameter_server/get_parameters')
        # サービスが利用可能になるまで待機します。
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        # GetParametersリクエストオブジェクトを作成します。
        self.request = GetParameters.Request()

    # パラメータの値を取得するメソッド
    def get_parameter(self, parameter_name):
        self.request.names = [parameter_name]  # 取得したいパラメータ名をリクエストに設定
        future = self.client.call_async(self.request)  # 非同期でサービスを呼び出します。
        rclpy.spin_until_future_complete(self, future)  # レスポンスが返ってくるまで待機します。
        if future.result() is not None:
            return future.result().values[0].string_value  # パラメータの値を返します。
        else:
            return None  # レスポンスがない場合はNoneを返します。

# メイン関数
def main(args=None):
    rclpy.init(args=args)  # ROS 2のPythonクライアントライブラリを初期化
    node = ParameterClient()  # ParameterClientクラスのインスタンスを作成
    parameter_value = node.get_parameter('happy_parameter')  # パラメータの値を取得
    node.get_logger().info(f'Value of the parameter: {parameter_value}')  # 値をログに出力
    rclpy.shutdown()  # ROS 2のシャットダウン処理

if __name__ == '__main__':
    main()
