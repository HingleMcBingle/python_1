#10.1 Revise a previous program as follows: Read and parse the “From”
#lines and pull out the addresses from the line. Count the number of messages from
#each person using a dictionary.
#After all the data has been read, print the person with the most commits by
#creating a list of (count, email) tuples from the dictionary. Then sort the list in
#reverse order and print out the person who has the most commits.

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
#empty list to iterate into            
lst = list()
#iterate through emails dictionary to append key values as value keys in list and sort by values
for key,value in emails.items():
    lst.append((value,key))
    lst.sort(reverse = True)
#print the first key value in the sorted list 
for val,key in lst[:1]:
    print(key,val)
