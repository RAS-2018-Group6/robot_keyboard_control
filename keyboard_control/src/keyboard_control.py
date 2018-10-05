#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32
from pynput import keyboard

class keyboard_control:
	def __init__(self):
         self.vel_pub = rospy.Publisher("/motor_controller/twist",Twist,queue_size = 1)
         self.linear_velocity = 0
         self.angular_velocity = 0

    def on_press(key):
        if key.char == 'w':
            self.linear_velocity += 0.005
        if key.char == 's':
            self.linear_velocity -= 0.005
        if key.char == 'a':
            self.angular_velocity += 0.001
        if key.char == 'd':
            self.angular_velocity -= 0.001

    def on_release(key):
        key_name = get_key_name(key)
        if key_name == 'Key.esc':
            return False

	def read_inputs(self):
		rospy.init_node('read_inputs')
		#rospy.Subscriber('kobuki/encoders',Encoders,self.callback_encoder)
        #rospy.Subscriber("/motor_controller/twist", Twist, self.callback_twist)

        with keyboard.Listener(on_press=on_press,on_release = on_release) as listener:
            listenre.join()

        rospy.loginfo("\n Linear Velocity: "+str(self.linear_velocity)+"\n Angular Velocity: "+str(self.angular_velocity))

        vel_msg = Twist()

        vel_msg.linear.x = self.linear_velocity
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0

        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = self.angular_velocity


		rate = rospy.Rate(10) #10HZ
		while not rospy.is_shutdown():
			rate.sleep()


if __name__ == '__main__':
	controler = keyboard_control()
	controler.read_inputs()
