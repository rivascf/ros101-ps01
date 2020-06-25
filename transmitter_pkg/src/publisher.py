#!/usr/bin/env python

import rospy
from receiver_pkg.msg import Persona

def talker():
    pub = rospy.Publisher('my_chatter', Persona, queue_size=10)
    rospy.init_node('my_talker', anonymous=True)
    r = rospy.Rate(10) #10Hz
    msg = Persona()
    msg.name = 'Pedro Penas'
    msg.age = 15

    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        r.sleep()

if __name__ == '__main__':
    talker()
#    try:
#        talker()
#    except rospy.ROSInterruptException:
#        pass