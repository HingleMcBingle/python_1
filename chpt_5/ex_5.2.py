#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.

#empty iterative variable for largest int
largest = None
#empty iterative variable for smallest int
smallest = None
#empty list to be updated with each user input number
numb_list = []
#infinite loop that takes in numbers from user and updates numb_list, smallest,largest variables then stops when "done" is input
while True:
    #ask user for number
    num = input("Enter a number: ")
    #if user enters "done" exit loop
    if num == "done":
        break
    #attempt to convert num into floating point and store in variable named "fnum" and update numb_list with each number entered from user
    try:
       fnum = float(num)
       numb_list.append(fnum)
    #if non number entered, tell user 'Invalid input'     
    except:
        print('Invalid input')
    
    #iterate through numb_list and update largest variable with numbers that are larger than previous input. convert number to int
    for val in numb_list:
        if largest is None:
            largest = int(val)
        elif val > largest:
            largest = int(val)
    #iterate through numb_list and update smallest variable with numbers that are smaller than previous input. convert number to int
    for val in numb_list:
        if smallest is None:
            smallest = int(val)
        elif val < smallest:
            smallest = int(val)
            
    #print(num)

print("Maximum is", largest)
print("Minimum is", smallest)