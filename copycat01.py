#!/usr/bin/env python3
"""Sammy Tamimi | Apprenti
    Pushing files around using shutil and os from std lib"""

# import addtl code to complete task
import shutil
import os

def main():
    # code to move files around
    os.chdir("/home/student/mycode/")

    #copy fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    #copy entire dirA to dirB
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()
