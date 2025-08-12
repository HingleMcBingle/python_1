#The basic outline of this problem is to read the file, look for integers using the re.findall(), 
#looking for a regular expression of '[0-9]+' 
#and then converting the extracted strings to integers and summing up the integers.

import re

fhand = open("regex_sum_2044724.txt")
numb_pattern = ""
lst = list()
count = 0
for line in fhand:
    line = line.rstrip()
    x = re.findall("[0-9]+",line)
    lst.extend(x)

for numb in lst:
    numb = int(numb)
    count = count + numb

print(count)




