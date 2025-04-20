#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from collections import defaultdict

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__("maott4996lytter_node")
        self.subscription = self.create_subscription(
            String,
            "maott4996",
            self.lytter_callback,
            10
        )
        self.dict = defaultdict(list)

    def lytter_callback(self, string_data):
        melding = string_data.data 
        melding_array = melding.split(" ")
        print(melding)
        self.add_terningkast(melding_array[0], int(melding_array[2]))

    def add_terningkast(self, navn, terningkast):
        if terningkast not in self.dict:
            self.dict[terningkast] = 1
        else:
            self.dict[terningkast] += 1
        self.skriv_resultat()

    def skriv_resultat(self):
        with open("./terningkast.txt", "w") as f:
            f.write(str(dict(self.dict)))

def main():
    rclpy.init()
    min_instans = MinimalSubscriber() 
    rclpy.spin(min_instans)
    min_instans.skriv_resultat()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

