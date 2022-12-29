#!/usr/bin/env python3

import rclpy

from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import random

class TurtleController(Node):

    def  __init__(self):
        super().__init__('turtle_controller')
        self.cmd_vel_publisher_=self.create_publisher(Twist,'/turtle1/cmd_vel',10)
        self.pose_subscriber_=self.create_subscription(Pose,'/turtle1/pose',self.callback,10)
        self.get_logger().info('...')


    def next_x(self,x,left,right):
        """return the next value of x"""
        return random.uniform(0.5, 3)
        

    
    def callback(self , pose:Pose):
        msg = Twist()
        
        if pose.x > 9 or pose.y > 9 or pose.x < 2 or pose.y < 2:
            msg.linear.x=self.next_x(pose.x , 2, 9)
            msg.linear.y=0.0
            msg.angular.z=0.9

        else:
            msg.linear.x=5.0
            msg.linear.y=0.0
            msg.angular.z=0.0

        self.cmd_vel_publisher_.publish(msg)




def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node)
    rclpy.shutdown()

