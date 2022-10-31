#!/home/cwj/anaconda3/bin/python3
# -*- coding: utf-8 -*-

from ast import arg
import rclpy
from rclpy.node import Node

class Node04(Node):
    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info("大家好，我是%s!" % name)


def main(args=None):
    rclpy.init(args=args) # 初始化rclpy
    node = Node04("node_04") # 新建一个节点
    rclpy.spin(node) # 保持节点运行，检测是否受到退出指令（Ctrl+C)
    rclpy.shutdown() # 关闭rclpy
    