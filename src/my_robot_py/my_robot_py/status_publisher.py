import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StatusPublisher(Node):   
    def __init__(self):
        super().__init__('status_publisher')
        self.publisher_ = self.create_publisher(String,'/robot_status',10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'Robot is ready'
        self.publisher_.publish(msg)

def main():
    rclpy.init()
    node = StatusPublisher()
    try:    
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
if __name__ == '__main__':
    main()