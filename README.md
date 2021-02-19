# demo_customer

I assume you have ros installed and catkin space setup


open terminal

move to your src folder of catkin_ws

cd catkin_ws/src


git clone https://github.com/raman123456789/demo_customer


move to catkin_ws

then do 

catkin_make



now that you have complied the code

now its time to run it.

first will source our workspace

cd catkin_ws/devel/setup.bash

Now before running code we have to  make sure Our VCAN cofiguration is set to up. 
IF not setup:
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link setup vcan0
sudo ip link set vcan0 down
sudo ip link set vcan0 up
candump vcan0
open new termal and run the blow command
cansend vcan0 055#11
you should be able to run them without any errors


then you are good to go.

Now once its is running we have to make sure

now run the following commands to run mobile application

roslaunch demo_customer demo_customer.launch channel:=vcan0 baud

OUTPUT: 
once you ran it you should be 

---------------------------------------------------------------
         CONNECTION TO CAN DEVICE-- SUCCESS
---------------------------------------------------------------

 and also a window with turlte in it.
and in the other terminal run
$candump vcan0
and open another teminal and run 
rosrun turtlesim turtle_telep_key
you should be able to control the turlte with upper and down arrow keys from the key board.
and also in the terminal where we opened candump, it shouls have output
  vcan0  188   [8]  00 02 01 00 00 00 00 00
  vcan0  188   [8]  00 02 01 00 00 00 00 00

BY this we get to know that things are working , now our task is to make it work with actual can device

for this do the configuration take help from arun. and
once you have you are able to see 
candump vcan0



QUICK START:
roslaunch demo_customer demo_customer.launch channel:=vcan0 baud_rate:=1000000

Here you can change it to channel:=can0 , and it will work with hardware can
and also you can specify baud_rate:=__ , your required baudrate(make sure you are giving valid once)

if you dont specify any arguments while launching,
roslaunch demo_customer demo_customer.launch
then 
the default values are :
"baudrate" default='1000000' 
"channel" default="can0"

CHEAKING:
in new terminal  run the following command and press top and bottom arrow keys, and you should see the turtle should be moving and also if you do candump vcan0/can0 you should see msgs printed)
rosrun turtlesim turtle_teleop_key

CONNECTING WITH MOBILE:

Now we need an android mobile with https://play.google.com/store/apps/details?id=com.robotca.ControlApp&hl=en&gl=US this app installed.
install it and open it , when you open it for the first time it will ask you for some permissions and provide it.

Now close the app and open it again.
and enter your IP(make sure both mobile and ros machine are connected to same wifi (same network))
then change ip with your ros machine  ip address and click on 'Show Advanced options' ,

then at 'Joystick topic' make to turtle1/cmd_vel
and press on okay and 
press on it.
then you should see a joy stick came on the app. and you can see the turtle is moving if you move joystick .also  in the can dump as well. if the hardware can is selected then the vechile should also move according to your joystick commands.

Thank you 
if you understand anything please feel free to contact me. 









