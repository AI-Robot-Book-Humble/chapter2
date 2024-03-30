import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from rcl_interfaces.msg import ParameterType
from rcl_interfaces.srv import GetParameters, SetParameters

class ParameterClient(Node):
    def __init__(self):
        super().__init__('happy_parameter_client_node')
        #values = self.get_parameters_from_another_node(self, 'node_name', ['param_name'])
        values = self.get_parameters_from_another_node('/happy_parameter_server_node', ['happy_parameter'])
        print(f'values={values}')
        
    def get_parameters_from_another_node(self, node_name, parameter_names):
        # create client
        client = self.create_client(
            GetParameters,
            '{node_name}/get_parameters'.format_map(locals()))

        # call as soon as ready
        ready = client.wait_for_service(timeout_sec=5.0)
        if not ready:
            raise RuntimeError('Wait for service timed out')

        request = GetParameters.Request()
        request.names = parameter_names
        future = client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        # handle response
        response = future.result()
        if response is None:
            e = future.exception()
            raise RuntimeError(
                'Exception while calling service of node '
                "'{args.node_name}': {e}".format_map(locals()))
        
        return_values = []

        for pvalue in response.values:
            if pvalue.type == ParameterType.PARAMETER_BOOL:
                value = pvalue.bool_value
            elif pvalue.type == ParameterType.PARAMETER_INTEGER:
                value = pvalue.integer_value
            elif pvalue.type == ParameterType.PARAMETER_DOUBLE:
                value = pvalue.double_value
            elif pvalue.type == ParameterType.PARAMETER_STRING:
                value = pvalue.string_value
            elif pvalue.type == ParameterType.PARAMETER_BYTE_ARRAY:
                value = pvalue.byte_array_value
            elif pvalue.type == ParameterType.PARAMETER_BOOL_ARRAY:
                value = pvalue.bool_array_value
            elif pvalue.type == ParameterType.PARAMETER_INTEGER_ARRAY:
                value = pvalue.integer_array_value
            elif pvalue.type == ParameterType.PARAMETER_DOUBLE_ARRAY:
                value = pvalue.double_array_value
            elif pvalue.type == ParameterType.PARAMETER_STRING_ARRAY:
                value = pvalue.string_array_value
            elif pvalue.type == ParameterType.PARAMETER_NOT_SET:
                value = None
            else:
                raise RuntimeError("Unknown parameter type '{pvalue.type}'" \
                    .format_map(locals()))
            return_values.append(value)
        
        return return_values


def main(args=None):
    rclpy.init(args=args)
    print('main:1')
    node = ParameterClient()
    print('main:2')
    #parameter_value = node.get_parameters_from_another_node()
    # create clientget_parameter('happy_parameter')
    print('main:3')
    #node.get_logger().info(f'Value of the parameter: {parameter_value}')
    print('main:4')
    rclpy.shutdown()

if __name__ == '__main__':
    main()
