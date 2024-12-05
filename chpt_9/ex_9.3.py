# 9.3 Write a program to read through a mail log, build a histogram using
#a dictionary to count how many messages have come from each email address, and
#print the dictionary.

fname = input("Enter file name:")

try:
    fhand = open(fname)
except:
    print("nope")
    exit

emails = dict()

for line in fhand:
    if line.startswith("From "):
        fline = line.split()

        for value in fline:
            email = fline[1]
            emails[email] = emails.get(email,0) + 1

print(emails)


        


    
    