import os # Python library containing OS functions
path = '.' # initialise path to current directory
files = os.listdir(path) # create list of files
for name in files: #loop through list
     print(name) # print each file
