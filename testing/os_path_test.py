import os.path

def makeafile():
    open("newfile.txt","w")

makeafile()

def test_homer():
    assert os.path.exists("newfile.txt") == True

