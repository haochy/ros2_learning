import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen
from functools import partial

class ParamController(Node):
    def __init__(self):
        super().__init__('param_controller')
        
        # 1. 宣告參數 (名稱, 預設值)
        self.declare_parameter('red_rgb', [255, 0, 0])
        self.declare_parameter('blue_rgb', [0, 0, 255])
        self.declare_parameter('pen_width', 3)
        self.declare_parameter('x_limit', 5.5)

        self.previous_x = 0
        self.cmd_vel_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pose_sub = self.create_subscription(Pose, 'turtle1/pose', self.pose_callback, 10)
        
        self.get_logger().info('Turtle Controller with Parameters has been started')

    def pose_callback(self, pose: Pose):
        # 2. 取得參數值
        red_rgb = self.get_parameter('red_rgb').value
        blue_rgb = self.get_parameter('blue_rgb').value
        p_width = self.get_parameter('pen_width').value
        x_limit = self.get_parameter('x_limit').value

        cmd = Twist()
        # 簡單的邊界邏輯
        if pose.x > 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0:
            cmd.linear.x = 1.0
            cmd.angular.z = 0.9
        else:
            cmd.linear.x = 5.0
            cmd.angular.z = 0.0
        self.cmd_vel_pub.publish(cmd)

        # 根據參數設定顏色
        if pose.x > x_limit and self.previous_x <= x_limit:
            self.previous_x = pose.x
            self.get_logger().info(f'Changing color to Red: {red_rgb}')
            self.call_set_pen_service(red_rgb[0], red_rgb[1], red_rgb[2], p_width, 0)
            
        elif pose.x <= x_limit and self.previous_x > x_limit:
            self.previous_x = pose.x
            self.get_logger().info(f'Changing color to Blue: {blue_rgb}')
            self.call_set_pen_service(blue_rgb[0], blue_rgb[1], blue_rgb[2], p_width, 0)

    def call_set_pen_service(self, r, g, b, width, off):
        client = self.create_client(SetPen, '/turtle1/set_pen')
        while not client.wait_for_service(1.0):
            self.get_logger().info('waiting for service...')
        
        request = SetPen.Request()
        request.r = r
        request.g = g
        request.b = b
        request.width = width
        request.off = off
        
        future = client.call_async(request)
        future.add_done_callback(partial(self.call_back_set_pen))

    def call_back_set_pen(self, future):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().error(f'SetPen service call failed: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = ParamController()
    rclpy.spin(node)
    rclpy.shutdown()
