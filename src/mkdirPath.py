from errno import EEXIST
from os import makedirs,path

# Description: Create the path and the folder
# Input: mypath: (str) the path to create
# Output: None
def mkdir_p(mypath):
    #Creates a directory. equivalent to using mkdir -p on the command line
    try:
        makedirs(mypath)
    except OSError as exc: # Python >2.5
        if exc.errno == EEXIST and path.isdir(mypath):
            pass
        else: raise