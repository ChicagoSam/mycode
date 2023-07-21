#!/usr/bin/env python3

#import modules for tools
import os
import subprocess

#asking user for commit message before starting process
comment = input(
        "What is the comment for this git add, commit, and push?\n"
        )

print("Changing directories...")
os.chdir('/home/student/mycode')

print("git add *...")
subprocess.run(['git','add','.']) # . or *?

print(f"git commit '{comment}'...")
subprocess.run(['git', 'commit', '-m', '{comment}'])

print("git push origin HEAD...")
subprocess.run(['git','push','origin','HEAD'])

print("(finish message)!")


