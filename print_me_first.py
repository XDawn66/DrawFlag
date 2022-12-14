#Program Name: print_me_first
#Program Description:
#   This is a program to return student info, the lab name, and the current time
#
#   This program will return the name of the student, the lab name, and the time
#@Author : Zhenyu Jiang
#@Date: 11/12/2022
#

def printinfo():
    from datetime import datetime
    name = "CNET-142 - Zhenyu Jiang"
    output = "{:20}".format("Name")+":"+name+'\n'
    Lab = "Lab 7 - Olympics Rings"
    output2 = "{:22}".format("Lab")+":"+Lab+'\n'
    currentTime = datetime.now()
    time = currentTime.strftime("%b-%d-%Y %a (%I:%M:%S%p)")
    output3 = "{:17}".format("Current Time")+":"+time+'\n'
    myword = output+output2+output3
    return myword
