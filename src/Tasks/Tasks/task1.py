#!/usr/bin/env python3

import rclpy

from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import random
import math
import argparse

# Y:
# up/top - values increase
# down/bottom - values decrease

# X:
# right - values increase
# left - values decrease

left = float(input("left : "))  # outer
top = float(input("top : "))
right = float(input("right :"))
down = float(input("down : "))
left1 = float(input("left1 : "))  # inner
top1 = float(input("top1 : "))
right1 = float(input("right1 : "))
down1 = float(input("down1 : "))
print(" outer rec : left : " + str(left) + " right : " + str(right) +
      " top : " + str(top) + " down : " + str(down) + "\n")
print(" inner rec : left : " + str(left1) + " right : " + str(right1) +
      " top : " + str(top1) + " down : " + str(down1))
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

    def callback(self, pose: Pose):
        msg = Twist()

        # this is if block for outer and inner limits

        if pose.x > right or pose.y > top or pose.x < left or pose.y < down or (pose.x < right1 and pose.x > left1 and pose.y < top1 and pose.y > down1):

            msg.linear.x = next_correction_linear_x()
            msg.linear.y = next_correction_linear_y()

           #if pose.theta >
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

        print (str(msg.linear)+"    "+str(msg.linear.y)+"    "+str(msg.angular.z))

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
    rclpy.spin(node.callback)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
