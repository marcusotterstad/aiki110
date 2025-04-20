import rclpy
from rclpy.node import Node
from maott4996_sign.msg import BryterTilstand

class MotorNode(Node):
    def __init__(self):
        super().__init__('maott4996_motornode')
        self.subscription = self.create_subscription(
            BryterTilstand,
            'maott4996_motorstyring',
            self.motor_callback,
            10
        )
        self.get_logger().info('Motornode aktiv')

    def motor_callback(self, msg):
        if msg.bryter_tilstand == 1:
            # Kjør motor
        elif msg.bryter_tilstand == 0:
            # Stopp motor
        else:
            self.get_logger().warn(f'Feil: ukjent tilstand {msg.bryter_tilstand}')

def main(args=None):
    rclpy.init(args=args)
    node = MotorNode()
    rclpy.spin(node)
    rclpy.shutdown()
