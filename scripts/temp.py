#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import can

temp=[]


t=False
idx=392
try:
    bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=1000000)
except:
    print("****				PLEASE MAKE CAN UP              	 ****")

def callback(data):
    x_linear=data.linear.x
    x_angular=data.angular.x
    
    # if x_linear==2:
    #     msg=[0x00,0X02,0X1,0x0, 0X0,0X0,0X0,0X0]
    # elif x_linear==-2:
    #     msg=[0x00,0X02,0X2,0x0, 0X0,0X0,0X0,0X0]
    # else :
    #     msg=[0x00,0X00,0X0,0x0, 0X0,0X0,0X0,0X0]
    a=abs(x_linear)
    print(x_linear)
    if a == 0:
        b=0
    elif a>0 and a<0.2 : #  3
        b=2.0
        
    elif a>=0.12 and a<0.4:
        b=2.4
        
    elif a>=0.4 and a<0.6:
        b=2.8
        
    elif a>=0.6 and a<0.8:
        b=3.2
    elif a>=0.8 and a<1:
        b=3.6
    else :
        b=0
    print(b)
    hex_v=int(b*256)
    print(hex_v)
    hex_v=hex(hex_v)
    print(hex_v)
    hex_v=hex_v[2:]
    k=hex_v
    print('k-',hex_v)
    print('len k',len(k))
    print(type(k))
    if len(k)==4:
        d1=k[:2]
        d2=k[2:]
    elif len(k)==3:
        d1='0'+k[0]
        d2=k[1:]
    elif len(k)==2:
        d1='00'
        d2=k
    elif len(k)==1:
        d1='00'
        d2='0'+k
    else:
        d1='00'
        d2='00'
    d1 = int(d1, 16)
    d2 = int(d2, 16)
    print('d1',d1)
    print('d2',d2)

    if x_linear>0:
        d3=0X1
    elif x_linear<0:
        d3=0X2
    else: 
        d3=0X0
    print(d1,d2,d3)
    msg=[d2,d1,d3,0X0,0X0,0X0,0X0,0X0]
    print(msg)

    # sendCAN_messagesToArduino(8,idx,msg)
    can_msg = can.Message(arbitration_id=0x188,
                              data=msg,
                              extended_id=False)
    bus.send(can_msg)
    
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('mobile_subscriber', anonymous=True)

    rospy.Subscriber("turtle1/cmd_vel", Twist, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

