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
        rospy.loginfo("lo envio: %d",acumulador)
        pub.publish(acumulador)
        contador=0


def memory_subscriber():
    rospy.init_node('suscriptor_basico_roberto',anonymous=True)     
    rospy.Subscriber('chatter',Int16,callback)     
    rospy.spin() 

        


if __name__ == "__main__":
    try:
        memory_subscriber() 
  
    except rospy.ROSInterruptException:
        pass