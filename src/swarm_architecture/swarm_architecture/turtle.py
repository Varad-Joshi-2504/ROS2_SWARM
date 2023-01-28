
#!/usr/bin/env python3

import rclpy

from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

import random

# Y:
# up/top - values increase
# down/bottom - values decrease

# X:
# right - values increase
# left - values decrease


class Locomoter(Node): #to topic node

    def __init__(self):

        super().__init__('locomoter')

class Sensor(Node):  #client

    def __init__(self):

        super().__init__('sensor')

        

class Trail(Node): #service

    def __init__(self):

        super().__init__('trail')

class Environment(Node): #service

    def __init__(self):

        super().__init__('env')
        #self.srv = self.create_service(add_env, 'add_two_ints', self.add_two_ints_callback)

    # def add_two_ints_callback(self, request, response):
    #     response.sum = request.a + request.b
    #     self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))

       # return response
        


def main():
    rclpy.init()
    locomoter = Locomoter()
    sensor = Sensor()
    trail = Trail()
    env = Environment()
    rclpy.spin(env)
    rclpy.spin(sensor)
    rclpy.spin(trail)
    rclpy.spin(locomoter)
    rclpy.shutdown()


if __name__ == '__main__':
    main()

