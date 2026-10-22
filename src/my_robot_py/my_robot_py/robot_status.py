import rclpy
from rclpy.node import Node

class Robotstatus(Node):
    def __init__(self):
        super().__init__('robot_status')
        self.timer = self.create_timer(1.0, self.timer_callback)
    def timer_callback(self):
        self.get_logger().info('Robot is ready')
def main():
    rclpy.init()
    node = Robotstatus()
    try:    
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
if __name__ == '__main__':
    main()
