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
        self.get_logger().info('Brytertjeneste startet')

    def bryter_callback(self, request, response):
        if request.bryter_id != 1:
            response.bryter_tilstand = -1
        else:
            # les av bryter
        return response

def main(args=None):
    rclpy.init(args=args)
    node = BryterService()
    rclpy.spin(node)
    rclpy.shutdown()
