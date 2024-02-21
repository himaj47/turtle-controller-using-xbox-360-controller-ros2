import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class TurtleControl(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        self.arr_vals = []

        self.joy_sub = self.create_subscription(Joy,"/joy",self.subs_callback,10)
        self.control_vel = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.get_logger().info("turtle_controller node started...")

    def subs_callback(self,msg:Joy):
        self.arr_vals = msg.axes

        # printing values got from xbox 360 controller
        # self.get_logger().info("leftHatX = " + str(-self.arr_vals[0]) + "    leftHatY = " + str(self.arr_vals[1]))
        
        data = Twist()
        data.linear.y = self.arr_vals[1]*10
        data.linear.x = -self.arr_vals[0]*10
        data.angular.z = self.arr_vals[3]*5

        self.control_vel.publish(data)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControl()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()