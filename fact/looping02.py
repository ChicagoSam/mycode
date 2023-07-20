#!/usr/bin/env python3

#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Using a file's lines as a source for the for-loop"""

# open file in read mode
dnsfile = open("dnsservers.txt", "r")
comservers= open("comservers.txt", "w")
orgservers= open("orgservers.txt", "w")

# create list of lines
dnslist = dnsfile.readlines()

# loop over lines, separate and write into respective files
for svr in dnslist:
    if svr.endswith (".com\n"):
        print(svr, end="", file=comservers)
    elif svr.endswith (".org\n"):
        print(svr, end="", file=orgservers)

# close the files (we created the list of lines)
dnsfile.close() # best practice to close your files
comservers.close()
orgservers.close()
