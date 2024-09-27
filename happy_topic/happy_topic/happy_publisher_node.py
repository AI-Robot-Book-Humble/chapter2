import rclpy                         # ROS2のPythonモジュール
from rclpy.node import Node          # rclpy.nodeモジュールからNodeクラスをインポート
from std_msgs.msg import String      # std_msgs.msgモジュールからStringクラスをインポート


class HappyPublisher(Node):  # "Happy World"とパブリッシュ並びに表示するクラス
    def __init__(self):  # コンストラクタ
        super().__init__('happy_publisher_node')
        self.pub = self.create_publisher(String, 'topic', 10)   # パブリッシャの生成
        self.timer = self.create_timer(1, self.timer_callback)  # タイマーの生成
        self.i = 10

    def timer_callback(self):  # コールバック関数
        msg = String()
        if self.i > 0:
            msg.data = f'ハッピーカウントダウン {self.i}'
        elif self.i == 0:
            msg.data = f'発射！'
        else:
            msg.data = f'経過時間 {-self.i}'
        self.pub.publish(msg)
        self.get_logger().info(f'パブリッシュ: {msg.data}')
        self.i -= 1


def main(args=None):  # main関数
    rclpy.init()
    node = HappyPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('Ctrl+Cが押されました．')
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
