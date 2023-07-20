#!/usr/bin/env python3

# import libraries
import shutil #used to move files
import os #access to low level OS operations

def man():
    #called at runtime

    #force home dir start
    os.chdir('/home/student/mycode/')

    #move file to folder
    shutil.move('raynor.obj', 'ceph_storage/')

    #pause and prompt for new name
    xname = input('What is the new name for kerrigan.obj? ')

    #move and rename
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

if __name__ == "__main__":
    main()
