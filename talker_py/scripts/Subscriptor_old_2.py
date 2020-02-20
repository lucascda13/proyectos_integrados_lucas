#!/usr/bin/env python 
#license removed for brevity 

import rospy 
from std_msgs.msg import Int16

acumulador=0
contador=0

def callback(msg):     
    global acumulador, contador
    rospy.loginfo("mensaje recibido: %s",msg.data) 
    acumulador=acumulador+msg.data
    contador=contador+1
    rospy.loginfo(" contador %d  acumulador %d",contador,acumulador)
    if contador==10:
        pub= rospy.Publisher('roberto', Int16, queue_size=10)
        rospy.loginfo(acumulador)
        pub.publish(acumulador)
        contador=0


def memory_subscriber():
    rospy.init_node('suscriptor_basico_roberto',anonymous=True)     
    #el primer argumento, es el nombrel del topic al que queremos suscribirnos...     
    #el segundo argumento es el tipo de mensaje,      
    rospy.Subscriber('chatter',Int16,callback)     
    rospy.spin() 

    #rate = rospy.Rate(10) 
    #contador=0
    #acumulador=0
    #loginfo("contador %d  acumulador %d")
    #while contador!=10:
        #hello_str = "hello world %s" % rospy.get_time()
        #rospy.loginfo(msg.data)
        #pub.publish(msg.data)
        #rate.sleep()
        
def publicador():
    global acumulador
    pub= rospy.Publisher('roberto', Int16, queue_size=10)
    rate = rospy.Rate(10) 
    while contador!=10:
        rospy.loginfo(acumulador)
        pub.publish(acumulador)

if __name__ == "__main__":
    try:
        memory_subscriber() 
        #rospy.init_node('suscriptor_basico_roberto',anonymous=True) 
        #rospy.Subscriber('chatter',Int16,callback)

       # publicador()
    except rospy.ROSInterruptException:
        pass