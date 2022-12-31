#!/usr/bin/env python3

import rclpy

from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import random

class Task1(Node):

    def  __init__(self):
        super().__init__('task1')
        # self.w = float(input("enter length of outer rectangle : "))    #this block takes the width and height of outer rectangle
        # self.h = float(input("enter height of outer rectangle : "))
        # self.c1 = float(input("enter x axis center of outer rectangle : "))
        # self.c2 = float(input("enter y axis center of outer rectangle : "))
        # self.left= self.c1 - (self.w / 2.0)
        # self.top= self.c2 - (self.h / 2.0)
        # self.right=self.c1+ (self.w / 2.0)
        # self.down=self.c2 + (self.h / 2.0)

        # self.w1 = float(input("enter length of inner rectangle : "))  #this block takes the width and height of inner rectangle   [don't use thsi block some problem here]
        # self.h1 = float(input("enter height of innner rectangle : "))
        # self.c11 = float(input("enter x axis center of inner rectangle : "))
        # self.c21 = float(input("enter y axis center of inner rectangle : "))
        # self.left1= self.c11 - (self.w1 / 2.0)
        # self.top1= self.c21 - (self.h / 2.0)
        # self.right1=self.c11+ (self.w1 / 2.0)
        # self.down1=self.c21 + (self.h1 / 2.0)

        self.left= float(input("left : "))
        self.top= float(input("top : "))
        self.right=float(input("right :"))
        self.down=float(input("down : "))

        self.left1= float(input("left1 : "))
        self.top1= float(input("top1 : "))
        self.right1=float(input("right1 : "))
        self.down1=float(input("down1 : "))

        print(" left : " + str(self.left) + " right : " + str(self.right) + " top : " + str(self.top) + " down : " + str(self.down) + "\n")
        print(" left : " + str(self.left1) + " right : " + str(self.right1) + " top : " + str(self.top1) + " down : " + str(self.down1))
        self.cmd_vel_publisher_=self.create_publisher(Twist,'/turtle1/cmd_vel',10)
        self.pose_subscriber_=self.create_subscription(Pose,'/turtle1/pose',self.callback,10)
        self.get_logger().info('...')
    
    def next_correction_linear_x(self): #next x value for correction
        """return the next value of x"""
        return random.uniform(0.0,0.2)
        

    def next_correction_linear_y(self): #next y value for correction
        """return the next value of y"""
        return random.uniform(0.0,0.2)

    def next_correction_angular_z(self): #next z value for correction
        """return next value of z"""
        return 0.9
    
    def next_linear_x(self): #next z value for correction
        """return next value of z"""
        return random.uniform(0.0,5.0)

    def next_linear_y(self): #next z value for correction
        """return next value of z"""
        return random.uniform(0.0,5.0)
        
    def next_angular_z(self): #next z value for correction
        """return next value of z"""
        return random.uniform(0.5,0.9)

    
    def callback(self , pose:Pose):
        msg = Twist()
        
        if pose.x > self.right or pose.y > self.down or pose.x < self.left or pose.y < self.top:  #this main if block is for outer rectangle
            msg.linear.x=self.next_correction_linear_x()
            msg.linear.y=self.next_correction_linear_y()
            msg.angular.z=self.next_correction_angular_z()
        
        else:
            
            if pose.x < self.right1 and pose.y < self.down1 and pose.x > self.left1 and pose.y > self.top1:  #this secondary if block is for inner rectangle
                msg.linear.x=self.next_correction_linear_x()
                msg.linear.y=self.next_correction_linear_y()
                msg.angular.z=self.next_correction_angular_z()


            else:            #if inside big rec and outside small recc then this:
                msg.linear.x=self.next_linear_x()
                msg.linear.y=self.next_linear_y()
                msg.angular.z=self.next_angular_z()


        self.cmd_vel_publisher_.publish(msg)




def main(args=None):
    rclpy.init(args=args)
    node = Task1()
    rclpy.spin(node)
    rclpy.shutdown()