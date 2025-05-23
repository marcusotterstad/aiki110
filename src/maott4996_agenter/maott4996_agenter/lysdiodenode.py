import rclpy
from rclpy.node import Node
from maott4996_sign.msg import BryterTilstand

class LysdiodeNode(Node):
    def __init__(self):
        super().__init__('maott4996_lysdiodenode')
        self.subscription = self.create_subscription(
            BryterTilstand,
            'maott4996_brytertilstand',
            self.bryter_callback,
            10
        )
        self.get_logger().info('Lysdiode aktiv')

    def bryter_callback(self, msg):
        if msg.bryter_tilstand == 1:
            # lys blinker
        elif msg.bryter_tilstand == 0:
            # lys av
        else:
            # lys gjør noe annet idk

def main(args=None):
    rclpy.init(args=args)
    node = LysdiodeNode()
    rclpy.spin(node)
    rclpy.shutdown()
