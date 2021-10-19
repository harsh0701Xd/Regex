import re
sum = 0
fname = input('Enter file name - ')
fh = open(fname)
for line in fh:
    s_num = re.findall('[0-9]+',line)
    for num in s_num:
        sum = sum + int(num)
print(sum)
