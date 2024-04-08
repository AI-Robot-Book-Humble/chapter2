import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter

class ParameterServer(Node): # ParameterServerクラス
    def __init__(self):
        super().__init__('happy_parameter_server_node')
        # パラメータの宣言と初期値の設定
        self.declare_parameter('happy_param_int',Parameter.Type.INTEGER)  
        self.declare_parameter('happy_param_string', 'Happy World')  # パラメータの宣言
        # パラメータの値を新しい整数値に変更 
        self.set_parameters([Parameter('happy_param_int', Parameter.Type.INTEGER, 7)]) 
        self.timer = self.create_timer(1, self.timer_callback)  # タイマの生成
    
    def timer_callback(self):
        param_int    = self.get_parameter('happy_param_int').value  # パラメータの取得
        param_string = self.get_parameter('happy_param_string').value  # パラメータの取得
        self.get_logger().info(f'happy_param_int:{param_int}')  # パラメータの表示
        self.get_logger().info(f'happy_param_string:{param_string}')  # パラメータの表示

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
