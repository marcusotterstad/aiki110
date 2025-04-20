import rclpy
from rclpy.node import Node
from maott4996_sign.msg import BryterTilstand

class BevegelsesNode(Node):
    def __init__(self):
        super().__init__('maott4996_bevegelsesnode')
        self.subscription = self.create_subscription(
            BryterTilstand,
            'maott4996_brytertilstand',
            self.bryter_callback,
            10
        )
        self.publisher = self.create_publisher(
            BryterTilstand,
            'maott4996_motorstyring',
            10
        )
        self.get_logger().info('Bevegelsesnode aktiv')

    def bryter_callback(self, msg):
        if msg.bryter_tilstand == 1 or msg.bryter_tilstand == 0:
            # send tilstand videre gjennom maott4996_motorstyring
            self.publisher.publish(msg)
        else:
            self.get_logger().warn(f'Ignorerer ugyldig tilstand: {msg.bryter_tilstand}')

def main(args=None):
    rclpy.init(args=args)
    node = BevegelsesNode()
    rclpy.spin(node)
    rclpy.shutdown()
