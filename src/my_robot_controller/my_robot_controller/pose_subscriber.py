#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class PoseSubscriber(Node):
    def __init__(self):
        super().__init__('pose_subscriber')
        self.pose_subcriber_= self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10)

    def pose_callback(self,msg:Pose):
        
        self.get_logger().info("angular vel : " + str(msg.angular_velocity)+ " , linear vel : " + str(msg.linear_velocity) + " , theta : " + str(msg.theta)) 
        self.get_logger().info("x: " + str(msg.x)+ " , y : " + str(msg.y) +"\n")

        

def main(args=None):
    rclpy.init(args=args)
    node = PoseSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()
