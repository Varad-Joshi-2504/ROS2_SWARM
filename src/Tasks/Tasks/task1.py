#!/usr/bin/env python3

import rclpy

from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import random

class Task1(Node):

    def  __init__(self):
        super().__init__('task1')
        self.w = input("enter length of outer rectangle : ")
        self.h = input("enter height of outer rectangle : ")
        #self.w1 = input("enter length of inner rectangle")
        #self.h1 = input("enter height of inner rectangle")
        self.xleft = 1.0
        self.xright = 1.0
        self.ytop = 1.0
        self.ydown = 1.0
        while((self.xright-self.xleft ==self.w) and (self.xleft<self.xright)):
            self.xright =random.uniform(0,11)
            self.xleft =random.uniform(0,11)
        
        while((self.ydown-self.ytop ==self.h) and (self.ytop<self.ydown)):
            self.ydown =random.uniform(0,11)
            self.ytop =random.uniform(0,11)
        self.cmd_vel_publisher_=self.create_publisher(Twist,'/turtle1/cmd_vel',10)
        self.pose_subscriber_=self.create_subscription(Pose,'/turtle1/pose',self.callback,10)
        self.get_logger().info('...')
    
    def next_linear_x(self):
        """return the next value of x"""
        return random.uniform(0.5, 5)
        

    def next_linear_y(self):
        """return the next value of y"""
        return random.uniform(0.5, 5)

    def next_angular_z(self):
        """return next value of z"""
        return random.uniform(0.1, 0.9)
        

    
    def callback(self , pose:Pose):
        msg = Twist()
        
        if pose.x > self.xright or pose.y > self.ydown or pose.x < self.xleft or pose.y < self.ytop:
            msg.linear.x=self.next_linear_x()
            msg.linear.y=self.next_linear_y()
            msg.angular.z=self.next_angular_z()

        else:
            msg.linear.x=5.0
            msg.linear.y=0.0
            msg.angular.z=0.0

        self.cmd_vel_publisher_.publish(msg)




def main(args=None):
    rclpy.init(args=args)
    node = Task1()
    rclpy.spin(node)
    rclpy.shutdown()

