import rclpy
from rclpy.node import Node
from maott4996_sign.srv import Maott4996Brytertilstand

class BryterService(Node):
    def __init__(self):
        super().__init__('maott4996_bryter_service')
        self.srv = self.create_service(
            Maott4996Brytertilstand,
            'maott4996_brytertilstand',
            self.bryter_callback
        )
        self.get_logger().info('brytertjeneste startet')
        self.counter = 0

    def bryter_callback(self, request, response):
        self.counter += 1

        if request.bryter_id != 1:
            response.bryter_tilstand = -1
        else:
            # Flip between 1 and 0 every 3 calls
            response.bryter_tilstand = self.counter % 2
        return response

def main(args=None):
    rclpy.init(args=args)
    node = BryterService()
    rclpy.spin(node)
    rclpy.shutdown()
