#!/usr/bin/env python3

#import modules for tools
import os

repo = git.Repo('origin')
origin = repo.remote(name='origin')


#asking user for commit message before starting process
comment = input(print("What is the comment for this git add, commit, and push?\n"))

print("Changing directories...")
os.chdir('/home/student/mycode')

print("git add *...")
repo.git.add('--all')

print(f"git commit '{comment}'")
repo.git.commit(-m, '{comment}') #not sure about this

print("git push origin HEAD")
origin.push()
