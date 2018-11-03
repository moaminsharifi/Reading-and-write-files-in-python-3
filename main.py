# Read and Write in Files Python
# Date 3 - 11 -2018 8:03 am
# Amin sharifi

# var of file = open("Name of file And Dir","method")
# r for read method
# w+ for write
newfile = open("text.txt","w+")

# Content Of File
str = "This Is Content Of File"

# Write In file
# Name Of Var File.Method(what We do)
# Ex Methods : read : To read All File , write : To Write All File , readline : To read Line By Line , writeline : To write Line By Line

newfile.write(str)
