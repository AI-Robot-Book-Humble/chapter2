import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import ParameterType
from rcl_interfaces.srv import GetParameters, SetParameters

class ParameterClient(Node):
    def __init__(self):
        super().__init__('happy_parameter_client_node')
        self.client = self.create_client(GetParameters, '/happy_parameter_server_node/get_parameters'.format_map(locals()))        
        while not self.client.wait_for_service(timeout_sec=1.0):  # サービスが利用できるまで待機
            self.get_logger().info('サービスは利用できません．待機中...')        
        self.request = GetParameters.Request()  # リクエストのインスタンス生成      
            
    def send_request(self,names):   # リクエストの送信        
        self.request.names = names  # リクエストに値を代入
        self.future = self.client.call_async(self.request)  # サービスのリクエスト
    

def main(args=None):
    rclpy.init(args=args)
    node = ParameterClient()
    names = ['happy_param_int','happy_param_string']  # パラメータ名のリストを代入
    node.send_request(names)

    while rclpy.ok():        
        rclpy.spin_once(node)
        if node.future.done():              # サービスの処理が終了したら
            try:
                res = node.future.result()  # サービスの結果をレスポンスに代入
            except Exception as e:          # エラーの場合
                node.get_logger().info(f"サービスの呼び出しに失敗しました．{e}")
            else:                           # ログにパラメータ名と値を表示
                node.get_logger().info(f"{names[0]}: {res.values[0].integer_value}")
                node.get_logger().info(f"{names[1]}: {res.values[1].string_value}")
                break   
    rclpy.shutdown()