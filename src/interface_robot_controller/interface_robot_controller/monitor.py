#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_interfaces.msg import RobotStatus

class MonitorNode(Node):
    def __init__(self):
        super().__init__('monitor')
        
        self.subscription = self.create_subscription(
            RobotStatus,
            'robot_status',
            self.listener_callback,
            10
        )
        self.get_logger().info('Monitor node has been started. Tracking battery level...')

    def listener_callback(self, msg):
        self.get_logger().info(f"Listening -> [{msg.name}] Battery: {msg.battery:.1f}% | Speed: {msg.speed} m/s")
        
        if msg.battery < 20.0:
            self.get_logger().warn(f"WARNING! Battery is at a critical level: {msg.battery:.1f}%!")

def main(args=None):
    rclpy.init(args=args)
    node = MonitorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()