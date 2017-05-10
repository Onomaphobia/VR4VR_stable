#!/usr/bin/env python

# My POS control 

# Copyright (c) 2013, Rethink Robotics
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the Rethink Robotics nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

"""
Baxter RSDK Joint Position Example: keyboard
"""
import argparse
import struct
import sys
import baxter_interface
import baxter_external_devices
import socket
import math
import time

import rospy

from geometry_msgs.msg import (
    PoseStamped,
    Pose,
    Point,
    Quaternion,
)
from std_msgs.msg import Header

from baxter_core_msgs.srv import (
    SolvePositionIK,
    SolvePositionIKRequest,
)

# Make a "define" for a function
def gotoPosition():
    # setup baxter stuff
    left = baxter_interface.Limb('left')
    right = baxter_interface.Limb('right')
    left.set_joint_position_speed(0.3)
    right.set_joint_position_speed(0.3)
    grip_left = baxter_interface.Gripper('left')
    grip_right = baxter_interface.Gripper('right')
    grip_left.calibrate()
    grip_right.calibrate()
    lj = left.joint_names()
    rj = right.joint_names()
    #set joint name, and relate to offical joint name(rj[])
    jointName0 = lj[0] 
    jointName1 = lj[1]
    jointName2 = lj[2]
    jointName3 = lj[3]
    jointName4 = lj[4]
    jointName5 = lj[5]
    jointName6 = lj[6]
    jointName7 = rj[0] 
    jointName8 = rj[1]
    jointName9 = rj[2]
    jointName10 = rj[3]
    jointName11 = rj[4]
    jointName12 = rj[5]
    jointName13 = rj[6]
    print "baxter setup done"
    
    #setup network stuff
    socket.setdefaulttimeout(3000)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server_socket.bind(("", 10000))
    server_socket.listen(50)
    print "TCPServer Waiting for client on port 10000"
    client_socket, address = server_socket.accept()
    print "I got a connection from ", address
    
    #Set joint angle comand to each joint
    #jointCommand = {jointName0:right.joint_angle(rj[0]) , jointName1:right.joint_angle(rj[1]) , jointName2:right.joint_angle(rj[2]) , jointName3:right.joint_angle(rj[3]) , jointName4:right.joint_angle(rj[4]) , jointName5:right.joint_angle(rj[5]) , jointName6:right.joint_angle(rj[6])}
    
    #jointCommand = {jointName0:0 , jointName1:0 , jointName2:0 , jointName3:0 , jointName4:0 , jointName5:0 , jointName6:0}
    #right arm joint command
    #right.set_joint_positions(jointCommand) 
    
    data = client_socket.recv(1024) 
    print data
    joint_angle0=str(left.joint_angle(lj[0]))
    joint_angle1=str(left.joint_angle(lj[1]))
    joint_angle2=str(left.joint_angle(lj[2]))
    joint_angle3=str(left.joint_angle(lj[3]))
    joint_angle4=str(left.joint_angle(lj[4]))
    joint_angle5=str(left.joint_angle(lj[5]))
    joint_angle6=str(left.joint_angle(lj[6]))
    joint_angle7=str(right.joint_angle(rj[0]))
    joint_angle8=str(right.joint_angle(rj[1]))
    joint_angle9=str(right.joint_angle(rj[2]))
    joint_angle10=str(right.joint_angle(rj[3]))
    joint_angle11=str(right.joint_angle(rj[4]))
    joint_angle12=str(right.joint_angle(rj[5]))
    joint_angle13=str(right.joint_angle(rj[6]))

    jointAngleStr=joint_angle0+","+joint_angle1+","+joint_angle2+","+joint_angle3+","+joint_angle4+","+joint_angle5+","+joint_angle6+","+joint_angle7+","+joint_angle8+","+joint_angle9+","+joint_angle10+","+joint_angle11+","+joint_angle12+","+joint_angle13
  
    #Send the current joint angle    
    client_socket.send(jointAngleStr)
    #Right arm current joint angle position          
    print ("current joint angle:", jointAngleStr)
    
    while 1:
        
        data = client_socket.recv(1024)
        #print(data)
        if ( data == 'q' or data == 'Q'):
            client_socket.close()
            break;
        else:
            #convert string list to float list
            poseStr = data.split(',')
            #split string to 7 pos
            pos = [] 
            if( len(poseStr) == 18):
               for i in poseStr:
                 pos.append(float(i))
            #send command to robot
            #may need to add while loop to make the joint angle correct
            #pos0 = int(pos[0])
            pos0 = pos[0]
            pos1 = pos[1]
            pos2 = pos[2]
            pos3 = pos[3]
            pos4 = pos[4]
            pos5 = pos[5]
            pos6 = pos[6]
            pos7 = int(pos[7])
            pos8 = int(pos[8])
            pos9 = pos[9]
            pos10 = pos[10]
            pos11 = pos[11]
            pos12 = pos[12]
            pos13 = pos[13]
            pos14 = pos[14]
            pos15 = pos[15]
            pos16 = int(pos[16])
            pos17 = int(pos[17])
            #print ("pos[7]:", pos7)
            #print ("Command joint angle:", pos0, pos1, pos2, pos3, pos4, pos5, pos6, pos9, pos10, pos11, pos12, pos13, pos14, pos15)
            #Set joint angle comand to each joint
            ljointCommand = {jointName0:pos0 , jointName1:pos1 , jointName2:pos2 , jointName3:pos3 , jointName4:pos4 , jointName5:pos5 , jointName6:pos6}
            rjointCommand = {jointName7:pos9 , jointName8:pos10 , jointName9:pos11 , jointName10:pos12 , jointName11:pos13 , jointName12:pos14, jointName13:pos15}
            
            #left arm joint command
            if (pos8 == 8):
                grip_left.close()
            if (pos8 == 32):
                grip_left.open()
            if (pos7 == 99):
                left.set_joint_positions(ljointCommand)
                left.set_joint_positions(ljointCommand)
                left.set_joint_positions(ljointCommand)
                left.set_joint_positions(ljointCommand)
                left.set_joint_positions(ljointCommand)
            #right arm joint command
            if (pos17 == 8):
                grip_right.close()
            if (pos17 == 32):
                grip_right.open()
            if (pos16 == 99):
                right.set_joint_positions(rjointCommand)
                right.set_joint_positions(rjointCommand)
                right.set_joint_positions(rjointCommand)
                right.set_joint_positions(rjointCommand)
                right.set_joint_positions(rjointCommand)

            #time.sleep(0.08)
            
            #right.move_to_joint_positions(jointCommand)
            #Right arm current joint angle position          
            #print (right.joint_angle(rj[0]), right.joint_angle(rj[1]), right.joint_angle(rj[2]), right.joint_angle(rj[3]), right.joint_angle(rj[4]), right.joint_angle(rj[5]), right.joint_angle(rj[6]) )
#            while((abs(right.joint_angle(rj[0])-pos0)>0.0175) or (abs(right.joint_angle(rj[1])-pos1)>0.0175) or (abs(right.joint_angle(rj[2])-pos2)>0.0175) or (abs(right.joint_angle(rj[3])-pos3)>0.0175) or (abs(right.joint_angle(rj[4])-pos4)>0.0175) or (abs(right.joint_angle(rj[5])-pos5)>0.0175) or (abs(right.joint_angle(rj[6])-pos6)>0.0175)):
#                 jointCommand = {jointName0:pos0 , jointName1:pos1 , jointName2:pos2 , jointName3:pos3 , jointName4:pos4 , jointName5:pos5 , jointName6:pos6}
            joint_angle0=str(left.joint_angle(lj[0]))
            joint_angle1=str(left.joint_angle(lj[1]))
            joint_angle2=str(left.joint_angle(lj[2]))
            joint_angle3=str(left.joint_angle(lj[3]))
            joint_angle4=str(left.joint_angle(lj[4]))
            joint_angle5=str(left.joint_angle(lj[5]))
            joint_angle6=str(left.joint_angle(lj[6]))
            joint_angle7=str(right.joint_angle(rj[0]))
            joint_angle8=str(right.joint_angle(rj[1]))
            joint_angle9=str(right.joint_angle(rj[2]))
            joint_angle10=str(right.joint_angle(rj[3]))
            joint_angle11=str(right.joint_angle(rj[4]))
            joint_angle12=str(right.joint_angle(rj[5]))
            joint_angle13=str(right.joint_angle(rj[6]))

            jointAngleStr=joint_angle0+","+joint_angle1+","+joint_angle2+","+joint_angle3+","+joint_angle4+","+joint_angle5+","+joint_angle6+","+joint_angle7+","+joint_angle8+","+joint_angle9+","+joint_angle10+","+joint_angle11+","+joint_angle12+","+joint_angle13
  
        
            client_socket.send(jointAngleStr)
            #print ("current joint angle:", jointAngleStr)

            
def main():
    """Use omni position to get everu joint of baxter via socket.
    """
    epilog = """
See help inside the example with the '?' key for key bindings.
    """
    arg_fmt = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(formatter_class=arg_fmt,
                                     description=main.__doc__,
                                     epilog=epilog)
    parser.parse_args(rospy.myargv()[1:])

    print("Initializing node... ")
    rospy.init_node("rsdk_joint_position_keyboard")
    print("Getting robot state... ")
    rs = baxter_interface.RobotEnable()
    init_state = rs.state().enabled

    def clean_shutdown():
        print("\nExiting example...")
        if not init_state:
            print("Disabling robot...")
            rs.disable()
    rospy.on_shutdown(clean_shutdown)

    print("Enabling robot... ")
    rs.enable()

    gotoPosition()
    
    print("Done.")


if __name__ == '__main__':
    main()
