import rclpy
from rclpy.node import Node


class MinimalParam(Node):
    def __init__(self):
        super().__init__('minimal_param_node')

        # declare rec parameters

        self.declare_parameters('outer_rec',[['left',0.0],['top', 0.0],['down', 0.0],['right', 0.0]])

        # self.declare_parameter('left', 0.0)
        # self.declare_parameter('top', 0.0)
        # self.declare_parameter('down', 0.0)
        # self.declare_parameter('right', 0.0)

        # for left paramete

        self.left_param = self.get_parameter(
            'outer_rec.left').get_parameter_value().double_value
        self.top_param = self.get_parameter(
            'outer_rec.top').get_parameter_value().double_value
        self.down_param = self.get_parameter(
            'outer_rec.down').get_parameter_value().double_value
        self.right_param = self.get_parameter(
            'outer_rec.right').get_parameter_value().double_value

        self.set_parameters([rclpy.Parameter(
            'outer_rec.left',
            rclpy.Parameter.Type.DOUBLE,
            self.left_param)])

        # for top parameter

        self.set_parameters([rclpy.Parameter(
            'outer_rec.top',
            rclpy.Parameter.Type.DOUBLE,
            self.top_param
        )])

        # for down parameter

        self.set_parameters([rclpy.Parameter(
            'outer_rec.down',
            rclpy.Parameter.Type.DOUBLE,
            self.down_param
        )])

        # for right parameter

        self.set_parameters([rclpy.Parameter(
            'outer_rec.right',
            rclpy.Parameter.Type.DOUBLE,
            self.right_param
        )])


def main():
    rclpy.init()
    node = MinimalParam()
    rclpy.spin(node)


if __name__ == '__main__':
    main()
