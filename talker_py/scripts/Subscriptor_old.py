#!/usr/bin/env python 
#license removed for brevity 

import rospy 
from std_msgs.msg import Int16

def callback(msg):     
    rospy.loginfo("mensaje recibido: %s",msg.data) 

def memory_subscriber():
    rospy.init_node('suscriptor_basico_roberto',anonymous=True)     
    #el primer argumento, es el nombrel del topic al que queremos suscribirnos...     
    #el segundo argumento es el tipo de mensaje,      
    rospy.Subscriber('chatter',Int16,callback)     
    rospy.spin() 
    rate = rospy.Rate(10) # 10hz
    contador=0
    acumulador=0
    loginfo("contador %d  acumulador %d")
    while contador!=10:
        #hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(msg.data)
        pub.publish(msg.data)
        rate.sleep()
        acumulador+=msg.data
        contador=contador+1
        loginfo("contador %d  acumulador %d")
        print(contador)

    print("La suma es: ",acumulador)

if __name__ == "__main__":
    try:
        memory_subscriber() 
    except rospy.ROSInterruptException:
        pass