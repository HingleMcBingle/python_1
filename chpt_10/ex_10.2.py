#This program counts the distribution of the hour of the day for each
#of the messages. You can pull the hour from the “From” line by finding the time
#string and then splitting that string into parts using the colon character. Once
#you have accumulated the counts for each hour, print out the counts, one per line,
#sorted by hour as shown below.

fname = input("Le name of file?:")
if len(fname) < 1: fhand = open('mbox-short.txt')
else: fhand = open(fname)
lst = list()
time_hr = dict()
for line in fhand:
    if line.startswith("From "):
        line.rstrip()
        line = line.split()
        time = line[5] 
        hr_min_sec = time.split(':')
        hr = hr_min_sec[0]
        time_hr[hr] = time_hr.get(hr,0) + 1

for key,val in time_hr.items():
    lst.append((key,val))
    lst.sort()

for key,val in lst:
    print(key,val)        
        
         
        


    