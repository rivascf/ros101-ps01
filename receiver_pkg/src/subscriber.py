#!/usr/bin/env python

import rospy
from receiver_pkg.msg import Persona

def callback(data):
    rospy.loginfo('{} tiene {} years.'.format(data.name, data.age))

def listener():

    rospy.init_node('my_listener', anonymous=True)
    rospy.Subscriber('my_chatter', Persona, callback)

    #spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()        
