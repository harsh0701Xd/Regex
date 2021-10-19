import os
import re
f_location = input('File location - ')
os.chdir(f_location) # for defining path location for the data.txt file
#print(os.getcwd())
#print(os.listdir())
sum = 0
fname = input('Enter file name - ')
fh = open(fname)
for line in fh:
    s_num = re.findall('[0-9]+',line)
    for num in s_num:
        sum = sum + int(num)
print(sum)
