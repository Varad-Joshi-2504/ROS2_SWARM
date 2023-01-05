#!/usr/bin/env python3

import rclpy

from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from tutorial_interfaces.msg import Num
import random
import math
import argparse

# Y:
# up/top - values increase
# down/bottom - values decrease

# X:
# right - values increase
# left - values decrease

# pose_danger_x:0.0
# pose_danger_y=0.0


class TurtleBoundaryLimiter(Node):

    def __init__(self):
        super().__init__('Turtle_boundary')
        self.cmd_vel_publisher_ = self.create_publisher(
            Twist, '/turtle1/cmd_vel', 10)
        self.pose_subscriber_ = self.create_subscription(
            Pose, '/turtle1/pose', self.callback, 10)
        self.get_logger().info('...')

        self.declare_parameters(
            'outer_rec', [['left', 0.0], ['top', 0.0], ['down', 0.0], ['right', 0.0]])

        self.out_left_param = self.get_parameter(
            'outer_rec.left').get_parameter_value().double_value
        self.out_top_param = self.get_parameter(
            'outer_rec.top').get_parameter_value().double_value
        self.out_down_param = self.get_parameter(
            'outer_rec.down').get_parameter_value().double_value
        self.out_right_param = self.get_parameter(
            'outer_rec.right').get_parameter_value().double_value

        self.set_parameters([rclpy.Parameter(
            'outer_rec.left',
            rclpy.Parameter.Type.DOUBLE,
            self.out_left_param
        )])

        # for top parameter

        self.set_parameters([rclpy.Parameter(
            'outer_rec.top',
            rclpy.Parameter.Type.DOUBLE,
            self.out_top_param
        )])

        # for down parameter

        self.set_parameters([rclpy.Parameter(
            'outer_rec.down',
            rclpy.Parameter.Type.DOUBLE,
            self.out_down_param
        )])

        # for right parameter

        self.set_parameters([rclpy.Parameter(
            'outer_rec.right',
            rclpy.Parameter.Type.DOUBLE,
            self.out_right_param
        )])

        self.declare_parameters(
            'inner_rec', [['left', 0.0], ['top', 0.0], ['down', 0.0], ['right', 0.0]])

        self.inner_left_param = self.get_parameter(
            'inner_rec.left').get_parameter_value().double_value
        self.inner_top_param = self.get_parameter(
            'inner_rec.top').get_parameter_value().double_value
        self.inner_down_param = self.get_parameter(
            'inner_rec.down').get_parameter_value().double_value
        self.inner_right_param = self.get_parameter(
            'inner_rec.right').get_parameter_value().double_value

        self.set_parameters([rclpy.Parameter(
            'inner_rec.left',
            rclpy.Parameter.Type.DOUBLE,
            self.inner_left_param
        )])

        # for top parameter

        self.set_parameters([rclpy.Parameter(
            'inner_rec.top',
            rclpy.Parameter.Type.DOUBLE,
            self.inner_top_param
        )])

        # for down parameter

        self.set_parameters([rclpy.Parameter(
            'inner_rec.down',
            rclpy.Parameter.Type.DOUBLE,
            self.inner_down_param
        )])

        # for right parameter

        self.set_parameters([rclpy.Parameter(
            'inner_rec.right',
            rclpy.Parameter.Type.DOUBLE,
            self.inner_right_param
        )])

    def callback(self, pose: Pose):
        msg = Twist()

        self.get_logger().info("outer : \n"+str(self.out_down_param)+str(self.out_left_param)+str(self.out_top_param)+str(self.out_right_param))
        self.get_logger().info("inner : \n"+str(self.inner_down_param)+str(self.inner_left_param)+str(self.inner_top_param)+str(self.inner_right_param))
       
        # this is if block for outer and inner limits

        if pose.x > self.out_right_param or pose.y > self.out_top_param or pose.x < self.out_left_param or pose.y < self.out_down_param or (pose.x < self.inner_right_param and pose.x > self.inner_left_param and pose.y < self.inner_top_param and pose.y > self.inner_down_param):

            msg.linear.x = next_correction_linear_x()
            msg.linear.y = next_correction_linear_y()

           # if pose.theta >
            msg.angular.z = next_correction_angular_z()
            # self.warning = warning_callback()
            # msg.linear.x = next(warning_callback())
            # msg.linear.y = next(warning_callback())
            # msg.angular.z = next(warning_callback())

        else:  # if inside big rec and outside small recc then this:

            msg.linear.x = next_linear_x()
            msg.linear.y = next_linear_y()
            msg.angular.z = next_angular_z()
            # self.general = general_movement()
            # msg.linear.x = next(general_movement())
            # msg.linear.y = next(general_movement())
            # msg.angular.z = next(general_movement())

        print(str(msg.linear)+"    "+str(msg.linear.y)+"    "+str(msg.angular.z))

        self.cmd_vel_publisher_.publish(msg)


# def warning_callback():  # pose:Pose):
#  #   q = p + pose.linear_velocity*theta

#     # if (pose.x + pose.linear_velocity*math.sin(pose.theta))==pose_danger_x or (pose.y + pose.linear_velocity*math.cos(pose.theta)):
#     yield random.uniform(0.1, 0.3)
#     yield random.uniform(0.1, 0.3)
#     yield 0.7


# def general_movement():
#     yield random.uniform(3.0, 5.0)
#     yield random.uniform(3.0, 5.0)
#     yield random.uniform(0.0, 0.2)


def next_correction_linear_x():  # next x value for correction
    """return the next value of x"""
    return random.uniform(0.1, 0.3)


def next_correction_linear_y():  # next y value for correction
    """return the next value of y"""
    return random.uniform(0.1, 0.3)


def next_correction_angular_z():  # next z value for correction
    """return next value of z"""
    return 0.7


def next_linear_x():  # next z value for correction
    """return next value of z"""
    return random.uniform(3.0, 5.0)


def next_linear_y():  # next z value for correction
    """return next value of z"""
    return random.uniform(3.0, 5.0)


def next_angular_z():  # next z value for correction
    """return next value of z"""
    return random.uniform(0.0, 0.2)


def main():
    # parser = argparse.ArgumentParser(
    #     prog = 'turtle-limit',
    #     description = 'Limit the turtle in its track')
    # parser.add_argument('-l',
    #                     '--left',
    #                     action='store')
    # parser.add_argument('--name',
    #                     action='store',
    #                     help='Name of the turtle')
    # args = parser.parse_args()
    # print("Turtle ", args.name, " can go at the most ", args.left, " meters to the left")
    rclpy.init()
    node = TurtleBoundaryLimiter()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
