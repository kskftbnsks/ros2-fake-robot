#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_interfaces.msg import RobotStatus
from my_interfaces.srv import SetSpeedLimit
from std_srvs.srv import Trigger

class FakeRobotNode(Node):
    def __init__(self):
        super().__init__('fake_robot')
        
        self.publisher_ = self.create_publisher(RobotStatus, 'robot_status', 10)
        self.timer = self.create_timer(1.0, self.publish_status)
        
        self.name = "Robo-X1"
        self.battery = 100.0
        self.speed = 1.0
        self.emergency_stop = False
        
        self.speed_srv = self.create_service(
            SetSpeedLimit, 
            'set_speed_limit', 
            self.handle_set_speed_limit
        )
        
        self.reset_srv = self.create_service(
            Trigger, 
            'reset_battery', 
            self.handle_reset_battery
        )
        
        self.get_logger().info('Fake Robot node has been started.')

    def publish_status(self):
        msg = RobotStatus()
        msg.name = self.name
        
        if self.battery > 0.0:
            self.battery -= 0.5
            
        msg.battery = self.battery
        msg.speed = self.speed
        msg.emergency_stop = self.emergency_stop
        msg.stamp = self.get_clock().now().to_msg()
        
        self.publisher_.publish(msg)

    def handle_set_speed_limit(self, request, response):
        if 0.0 <= request.limit <= 2.0:
            self.speed = request.limit
            response.success = True
            response.message = f"Speed limit {self.speed} m/s ."
            self.get_logger().info(response.message)
        else:
            response.success = False
            response.message = f"Invalid speed limit: {request.limit}. Limit must be between 0 and 2.0 m/s!"
            self.get_logger().warn(response.message)
        return response

    def handle_reset_battery(self, request, response):
        self.battery = 100.0
        response.success = True
        response.message = "Battery has been reset to 100%!"
        self.get_logger().info(response.message)
        return response

def main(args=None):
    rclpy.init(args=args)
    node = FakeRobotNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()