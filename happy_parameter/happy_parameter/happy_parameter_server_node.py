import rclpy
from rclpy.node import Node

# ParameterServerクラスを定義します。Nodeクラスを継承しています。
class ParameterServer(Node):
    def __init__(self):
        # ノード名を'parameter_server'に設定します。
        super().__init__('parameter_server')
        # 'example_parameter'という名前のパラメータを宣言し、初期値を'Hello World'に設定します。
        self.declare_parameter('example_parameter', 'Hello World')

# メイン関数
def main(args=None):
    rclpy.init(args=args)  # ROS 2のPythonクライアントライブラリを初期化
    node = ParameterServer()  # ParameterServerクラスのインスタンスを作成
    try:
        rclpy.spin(node)  # ノードをspinし、コールバック関数を実行可能にします。
    except KeyboardInterrupt:
        pass  # キーボード割り込み（Ctrl+C）が発生した場合は終了します。
    rclpy.shutdown()  # ROS 2のシャットダウン処理

if __name__ == '__main__':
    main()
