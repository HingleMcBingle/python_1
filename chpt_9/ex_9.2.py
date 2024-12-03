#9.2 Write a program that categorizes each mail message by which day of
#the week the commit was done. To do this look for lines that start with “From”,
#then look for the third word and keep a running count of each of the days of the
#week. At the end of the program print out the contents of your dictionary (order
#does not matter).

#ask user to input filename
fname = input("Enter a file name:")

#try to open filename entered by user or display file cannot be opened and exit application
try:
    fhand = open(fname)
except:
    print("File cannot be opened")
    exit()
#empty dictionary 
wkdy = dict()

#parse through only lines in the file that start with From
for line in fhand:
    if line.startswith("From "):
        #seperate lines into list items 
        email = line.split()
        #parse through email list for day of the week sent
        for value in email:
            day = email[2]
            wkdy[day] = wkdy.get(day,0) + 1
print(wkdy)
            
        


