hrs =  input("How Many Hours Worked?\n")
try:
    hrs = float (hrs)
#create seperate variable for hours worked above 40
    if hrs > 40 :
        hrs_plus = (hrs - 40)
    if hrs <= 40 :
        hrs_plus = 0

    hrs_reg = (hrs - hrs_plus)

    rate =  input("Whats the Hourly Rate?\n")

    rate = float(rate)
    rate_plus = (rate * 1.5)

    print(hrs_reg * rate + hrs_plus * rate_plus)

except:
    print("PLZ enter a NUMBER :)")
