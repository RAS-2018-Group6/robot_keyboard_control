#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32
from pynput import keyboard
from pynput.keyboard import Key


class keyboard_control:

	def __init__(self):
		self.vel_pub = rospy.Publisher("/motor_controller/twist",Twist,queue_size = 1)
		self.linear_velocity = 0.0
		self.angular_velocity = 0.0
		self.vel_msg = Twist()

		self.vel_msg.linear.x = self.linear_velocity
		self.vel_msg.linear.y = 0.0
		self.vel_msg.linear.z = 0.0

		self.vel_msg.angular.x = 0.0
		self.vel_msg.angular.y = 0.0
		self.vel_msg.angular.z = self.angular_velocity

	def on_press(self,key):
		print('{0} pressed'.format(key))
		if key == Key.up:
		    	self.linear_velocity += 0.005
			self.vel_msg.linear.x = self.linear_velocity
			rospy.loginfo("\n Linear Velocity: "+str(self.linear_velocity)+"\n Angular Velocity: "+str(self.angular_velocity))
			self.vel_pub.publish(self.vel_msg)
		elif key == Key.down:
		    	self.linear_velocity -= 0.005
			self.vel_msg.linear.x = self.linear_velocity
			rospy.loginfo("\n Linear Velocity: "+str(self.linear_velocity)+"\n Angular Velocity: "+str(self.angular_velocity))
			self.vel_pub.publish(self.vel_msg)
		elif key == Key.left:
		    	self.angular_velocity += 0.005
			self.vel_msg.angular.z = self.angular_velocity
			rospy.loginfo("\n Linear Velocity: "+str(self.linear_velocity)+"\n Angular Velocity: "+str(self.angular_velocity))
			self.vel_pub.publish(self.vel_msg)
		elif key == Key.right:
		    	self.angular_velocity -= 0.005
			self.vel_msg.angular.z = self.angular_velocity
			rospy.loginfo("\n Linear Velocity: "+str(self.linear_velocity)+"\n Angular Velocity: "+str(self.angular_velocity))
			self.vel_pub.publish(self.vel_msg)
		elif key == Key.ctrl:
			self.linear_velocity = 0.0
			self.angular_velocity = 0.0
			self.vel_msg.linear.x = self.linear_velocity
			self.vel_msg.angular.z = self.angular_velocity
			rospy.loginfo("\n Linear Velocity: "+str(self.linear_velocity)+"\n Angular Velocity: "+str(self.angular_velocity))
			self.vel_pub.publish(self.vel_msg)
		else:
			rospy.loginfo("Non valid input")

	def on_release(self,key):
		if key == Key.esc:
			return False

	def read_inputs(self):
		rospy.init_node('read_inputs')

		with keyboard.Listener(on_press = self.on_press, on_release = self.on_release) as listener:
		    listener.join()

		rate = rospy.Rate(10) #10HZ
		while not rospy.is_shutdown():
			rate.sleep()


if __name__ == '__main__':
	controler = keyboard_control()
	controler.read_inputs()
