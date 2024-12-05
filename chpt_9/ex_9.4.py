# 9.4 Add code to the previous program to figure out who has the most
#messages in the file. After all the data has been read and the dictionary has
#been created, look through the dictionary using a maximum loop (see Chapter 5:
#Maximum and minimum loops) to find who has the most messages and print how
#many messages the person has.

#ask user to input file name and default to filename if the length of the input is less than 3
fname = input("Enter file name:")
if len(fname) < 3:
    fname = "mbox-short.txt"

#attempt to open user input in file handle if it fails print nope and exit program
try:
    fhand = open(fname)
except:
    print("nope")
    exit

#empty dictionary to iterate values into 
emails = dict()
#empty count variable to intrate value into
lcount = None
#empty word variable to iterate corresponding key into
lword = None

#loop through and seperate lines starting with From in file
for line in fhand:
    if line.startswith("From "):
        #remove whitespace
        line.rstrip()
        #seperate words in line into a list
        line = line.split()
        #update line to only be index 1 of the list which contains the email from the "From" line
        line = line[1]
        #add email to empty dictionary emails variable
        emails[line] = emails.get(line,0) + 1
            

#loop through dictionary key and value to determine most recurring email 
for key,value in emails.items():
    if lcount is None or value > lcount:
        lcount = value
        lword = key



print(lword, lcount)



        


    
    