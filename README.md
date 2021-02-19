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





