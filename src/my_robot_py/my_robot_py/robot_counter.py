import rclpy
from rclpy.node import Node

class RobotCounter(Node):
    def __init__(self):
        super().__init__('robot_counter')
        self.count = 0
        self.timer = self.create_timer(1.0, self.counter_callback)     
    def counter_callback(self):
        self.count+=1
        self.get_logger().info('Count:%d' % self.count)
    
def main():
    rclpy.init()
    node = RobotCounter()
    try:    
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
if __name__ == '__main__':
    main()
