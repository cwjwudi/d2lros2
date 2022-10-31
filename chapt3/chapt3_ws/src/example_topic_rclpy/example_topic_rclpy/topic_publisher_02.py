#!/home/cwj/anaconda3/bin/python3
# -*- coding: utf-8 -*-

from tokenize import String
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import mujoco


class NodePublisher02(Node):
    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info("大家好，我是%s!" % name)
        self.command_publisher_ = self.create_publisher(String, "command", 10)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        """
        定时器回调函数
        """
        msg = String()
        msg.data = 'backup,mujoco'
        self.command_publisher_.publish(msg)
        self.get_logger().info(f'发布了指令：{msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = NodePublisher02("topic_publisher_02")
    rclpy.spin(node)
    rclpy.shutdown()
    