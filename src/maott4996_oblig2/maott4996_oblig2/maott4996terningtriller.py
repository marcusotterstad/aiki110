#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__("maott4996triller_node")
        self.publisher = self.create_publisher(
            String,
            "maott4996",
            10
        )
        self.create_timer(1, self.kast_terning)

    def kast_terning(self):
        msg = String()
        terningkast = random.randint(1,20)
        msg.data = f'maott4996 trillet {terningkast} på en D20.'
        print(f"sending {terningkast}")
        self.publisher.publish(msg)

def main():
    rclpy.init()
    min_instans = MinimalPublisher()
    for x in range(10):
        rclpy.spin_once(min_instans, timeout_sec=10)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
