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
        self.subscription
        self.get_logger().info('Lysdiode lytter på brytertilstand...')

    def bryter_callback(self, msg):
        if msg.bryter_tilstand == 1:
            self.get_logger().info('LED: PÅ')
        elif msg.bryter_tilstand == 0:
            self.get_logger().info('LED: AV')
        else:
            self.get_logger().warn(f'LED: Ugyldig tilstand: {msg.bryter_tilstand}')

def main(args=None):
    rclpy.init(args=args)
    node = LysdiodeNode()
    rclpy.spin(node)
    rclpy.shutdown()
