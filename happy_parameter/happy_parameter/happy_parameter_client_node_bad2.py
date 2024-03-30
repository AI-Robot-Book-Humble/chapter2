import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from rcl_interfaces.srv import GetParameters, SetParameters

class ParameterClient(Node):
    def __init__(self):
        super().__init__('happy_parameter_client_node')
     

    def get_parameter(self, parameter_name):
        type_array = ["not_set", "bool_value", "integer_value", "double_value", "string_value", 
                         "byte_array_value", "bool_array_value", "integer_array_value", 
                         "double_array_value", "string_array_value"]
        client = self.create_client(GetParameters, '/happy_parameter_server_node/get_parameters')
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        print('1')
        request = GetParameters.Request()  # ローカル変数としてリクエストオブジェクトを作成
        print('2')
        request.names = [parameter_name]
        print('3')
        future = client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        res = future.result()
        print(f'result={res}')
        if res is not None:
            #return getattr(res.values[0],res.values[0].STRING)
            #return getattr(res.values[0],type_array[res.values[0].type])
            print('4')
            attr = getattr(res.values[0],"string_value")
            print('5')
            return attr
            #return res.values[0]
        else:
            return None

def main(args=None):
    rclpy.init(args=args)
    print('main:1')
    node = ParameterClient()
    print('main:2')
    parameter_value = node.get_parameter('happy_parameter')
    print('main:3')
    node.get_logger().info(f'Value of the parameter: {parameter_value}')
    print('main:4')
    rclpy.shutdown()

if __name__ == '__main__':
    main()
