#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32

class keyboard_control:
	def __init__(self):
         self.vel_pub = rospy.Publisher("/motor_controller/twist",Twist,queue_size = 1)
         self.linear_velocity = 0
         self.angular_velocity = 0
         self.vel_msg = Twist()


	def read_inputs(self):
		rospy.init_node('read_inputs')
		#rospy.Subscriber('kobuki/encoders',Encoders,self.callback_encoder)
        #rospy.Subscriber("/motor_controller/twist", Twist, self.callback_twist)

		rate = rospy.Rate(10) #10HZ
		while not rospy.is_shutdown():
			rate.sleep()


if __name__ == '__main__':
	controler = keyboard_control()
	controler.read_inputs()
