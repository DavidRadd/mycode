#!/usr/bin/env python3

import shutil
import os

def main():

    # Move into a Working Directory. -- It's like using 'cd ~/mycode/5g_research'

    os.chdir("/home/student/mycode/")

    # Copy file a to b -- like using 'cp filea fileb'
    shutil.copy("5g_research/sdn_network.txt")


    # Copy the entire directoryA to directoryB
    shutil.copytree("5g_research", "5g_research_backup/")

    # delete the directory
    # os.system("rm -rf /home/student/mycode/5g_research_backup/")




