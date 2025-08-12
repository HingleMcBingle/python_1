def computepay(hrs, rate):
        pay = (hrs_reg * rate + hrs_plus * rate_plus)
        return pay

hrs =  input("How Many Hours Worked?")
rate =  input("Whats the Hourly Rate?")
hrs = float (hrs)
if hrs > 40 :
        hrs_plus = (hrs - 40)
if hrs_plus > 0 :
       hrs_reg = (hrs - hrs_plus)
rate = float(rate)
rate_plus = (rate * 1.5)

print('Pay',computepay(hrs, rate))
