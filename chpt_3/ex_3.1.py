hrs =  input("How Many Hours Worked?")
hrs = float (hrs)
if hrs > 40 :
        hrs_plus = (hrs - 40)
if hrs_plus > 0 :
       hrs_reg = (hrs - hrs_plus)
rate =  input("Whats the Hourly Rate?")
rate = float(rate)
rate_plus = (rate * 1.5)
print(hrs_reg * rate + hrs_plus * rate_plus)
