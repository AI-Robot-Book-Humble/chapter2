import rclpy
from rclpy.node import Node
from std_msgs.msg import String


# Sring型メッセージをサブスクライブして端末に表示するだけの簡単なクラス
class HappySubscriber(Node):
    def __init__(self):  # コンストラクタ
        super().__init__('happy_subscriber_node')
        # サブスクライバの生成
        self.sub = self.create_subscription(String,
                                            'topic', self.callback, 10)

    def callback(self, msg):  # コールバック関数
        self.get_logger().info(f'サブスクライブ: {msg.data}')


def main(args=None):  # main関数
    rclpy.init()
    node = HappySubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('Ctrl+Cが押されました．')
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
