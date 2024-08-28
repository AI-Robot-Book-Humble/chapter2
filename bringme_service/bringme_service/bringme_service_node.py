import time
import rclpy
from rclpy.node import Node
from airobot_interfaces.srv import StringCommand

class BringmeService(Node):  # ハッピーサービスクラス
    def __init__(self):  # コンストラクタ
        super().__init__('bringme_service')
        # サービスの生成（サービス型，サービス名, コールバック関数)
        self.service = self.create_service(StringCommand, 'command',self.callback)
        self.food = ['apple', 'banana', 'candy']   

    def callback(self, request, response):  # コールバック関数
        time.sleep(5)
        for item in self.food:
            if item in request.command:
                response.answer = 'はい，これです．'
                return response
        response.answer = '見つけることができませんでした．'
        return response


def main():  # main関数
    rclpy.init()
    node = BringmeService()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("Ctrl+CLが押されました．")
    finally:
        node.destroy_node()
        rclpy.shutdown()
  
