import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StatusSubscriber(Node):   
    def __init__(self):
        super().__init__('status_subscriber')
        self.subscription_ = self.create_subscription(String,'/robot_status',self.subscription_callback,10)

    def subscription_callback(self, msg):
        self.get_logger().info('Received: %s' % msg.data)

def main():
    rclpy.init()
    node = StatusSubscriber()
    try:    
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
if __name__ == '__main__':
    main()
