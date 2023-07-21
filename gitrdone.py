#!/usr/bin/env python3

"""automating post lab git commands"""

#TO DO add alias for gitrdone
#append to ~/.bashrc?

#import modules for tools
import os
import subprocess

#asking user for commit message before starting process
#add While to make sure comment not blank or git commit will fail, if message, thanks and break, else "cannot be blank"
comment = input(
        "What is the comment for this git add, commit, and push?\n"
        )

#Git commands with variable comment
#add error handling
def main():
    print("Changing directories...")
    os.chdir('/home/student/mycode')

    print("git add *...")
    subprocess.run(['git','add','.']) # . or *?

    print(f"git commit '{comment}'...")
    subprocess.run(['git', 'commit', '-m', f'{comment}'])

    print("git push origin HEAD...")
    subprocess.run(['git','push','origin','HEAD'])

    print(f"Pushed with comment '{comment}'!")

if __name__=='__main__':
    main()


