# Identify the variables for the program
# Coname, EmpId, date, time, payperiod, fname, lname, mname, hoursWorked, hrsperweek, hoursWorked,
# Vachrs, grossPay, netPay, payRate,
# stateTax, fedTax, ficaTax, hrsout
# Identify constants
# deduct = 100,
# stateTaxrate = 0.05, fedTaxrate = 0.02,
# ficaTaxrate = 0.027
# Vachrs = 120
# weekPryr = 52
# hrsPryr = 2080
# OvrTime =  1.5
# Sickhrs = 24
# Prsnl = 8
# hrsperweek = 40
'''
'identify any equations and formulas
    #grossPay = payRate * hoursWorked
    #netPay = grossPay - ( taxes + deduct)
    #taxes = fedTax + ficaTax + stateTax
    #fedTax = grossPay * fedTaxrate
    #ficaTax = grossPay * ficaTaxrate
    #stateTax = grossPay * stateTaxrate
    #Vachrs = hrsweek - Vachrs
    #Sickhrs = hrsperweek - Sickleave
    #Prsnl = hrsperweek - Prsnl
    #hrsperweek = weekPryr * hrsperweek
    #OvrTime = hoursWorked * OvrTime
    ''
if hours > hrsperweeks:
     #calculate the gross pay with overtime.
     #First, get the number overtime hours worked.
     Ovrtime = hours - hrsperweek

     #calculate the amount of overtime pay.
     Ovrtime = hrsperweeks *payRate * Ovrtime 

     #calculate the gross pay.
     gross_pay = base_hours * payRate *overtime_pay
   else:
      #calculate the gross pay without overtime.
      grosspay = hours * payRate 
    
'''
#convert the algorithm to Python Code statements (or whatever language you're using)
# creating constants below
STATE_TAX_RATE = float(0.05)
FED_TAXRATE = float(0.02)
FICA_TAX_RATE = float(0.0765)
deduct = float(100.00)
Vachrs = float(120)
OvrTime = float(1.5)
Sickhrs = float (24)
Prsnl = float (16)
hrsperweek = float (40)
hrsPryr = float (2080)
weekPryr = float (52)
# prompt the user for the data and assigning the value to the variables
Date = input("Date:")
Time =(input("Time:"))
payPeriod = input("Payperiod Start Date:")
payperiod = input("Payperiod End Date:")
fname = input("Employee First Name:")
lname = input("Eployee Last Name:")
EmpID = input("Employee No.:")
hoursWorked = float(input("Enter Hours Worked:"))
hrsout = float(input("Hours Out:"))
payRate = float(input("Enter Payrate:"))
# perform calculations
grosspay = hoursWorked * payRate #calculate the gross pay without overtime.
grossPay = payRate * hoursWorked    # calculating 
fedTax = grossPay * FED_TAXRATE      # calculating 
ficaTax = grossPay * FICA_TAX_RATE    # calculating 
stateTax = grossPay * STATE_TAX_RATE  # calculating 
taxes = fedTax + ficaTax + stateTax # calculating 
netPay = grossPay - taxes # calculating
hrsperweek = hrsperweek
Vachrs = hrsperweek + hrsperweek + hrsperweek - hrsout # calculating
Sickhrs = hrsperweek - Sickhrs # calculating
Prsnl = hrsperweek - Prsnl # calculating
OvrTime = hoursWorked * OvrTime # calculating
if hoursWorked > hrsperweek:
     #calculate the gross pay with overtime.
     #First, get the number overtime hours worked.
     Ovrtime = hoursWorked - hrsperweek

     #calculate the amount of overtime pay.
     Ovrtime = hrsperweek * payRate * Ovrtime 

     #calculate the gross pay.
     grosspay = hrsperweek * payRate * Ovrtime
else:
      #calculate the gross pay without overtime.
      grosspay = hoursWorked * payRate 
# formatting output in currency format
# fromatting was added 6-6-2023
print ("Richard Dangley Rope Shop Pay Check")
print("P.o. Box 2216", '\t',"decatur, AL",'\t\t\t', "EARNINGS STATEMENT")
print('|===============================================================|')
print('| EMPLOYEE NAME/ADDRESS', '\t', 'EMPLOYEE ID')
print('|===============================================================|')
print('| Employee Name ', fname, " ", lname, " ", EmpID, '|',payPeriod, "|", payperiod)
#print('|hours', '\t\t', ' ', 'payrate', '\t', ' ', 'grosspay','\t   ',   'netpay','     |')
#print('|', hours, '\t\t', ' ', 'payrate', '\t', ' ', 'grosspay','\t   ',   'netpay + Ovrtime','     |')
print('|hours', '\t\t', ' ', 'payrate', '\t', ' ', 'grosspay','\t   ',   'netpay','     |')
print('|===============================================================|')
print('|',f'{hoursWorked:,.2f}', '\t','|',  f'${payRate:,.2f}',  '\t','|', f'${grossPay:,.2f}',  '\t' ,'|',  f'${netPay:,.2f}')
# be sure to make corrections to variable names. Apply formatting to this code
#displaying the output
print("________________________________________")
print("Gross Pay    |     Federal Tax") 
print("________________________________________")
print(format(grossPay, ".2f"),"         ",  format(fedTax, ".2f")) 
print("________________________________________")
print("Gross Pay = ",  format(grossPay, ".2f"),format(fedTax, ".2f"))  
print("Gross Pay = ", grossPay)
print(" federal Taxes = ", fedTax)
print(" federal Taxes = ", format(fedTax, ".2f"))
print(" State Taxes = ", stateTax)
print(" State Taxes = ", format(stateTax, ".2f"))
print(" FICA = ", format(ficaTax, ".2f"))
print(" FICA = ", ficaTax)
print(" Net Pay = ", format(netPay, ".2f"))
print(" Net Pay = ", netPay)
print(" Deductions = ", format(deduct, ".2f"))
print(" Deductions = ", deduct)
print(" Over Time = ", format (OvrTime, ".2f"))
print(" Over Time = ", OvrTime)
print(" Vaction = ", format(Vachrs, ".2f"))
print(" Vaction = ", Vachrs)
print(" Sick Hours = ", format(Sickhrs, ".2f"))
print(" Sick = ", Sickhrs)
print(" Personal Hours = ", format(Prsnl, ".2f"))
print(" Personal = ", Prsnl)

# name constants to repersent the base hours and
# the overtime multiplier.

'''
hrsperweek = 40 # base hours per week
Ovrtime = 1.5 # overtime multiplier

#get the hours worked and the hourly pay rate.
hrsperweek = float(input('Enter the numbers of hours worked: ' ))
pay_rate = float (input('Enter the hourly pay rate: '))

'''

 #calculate and display the gross pay.
'''
if hours > hrsperweeks:
     #calculate the gross pay with overtime.
     #First, get the number overtime hours worked.
     Ovrtime = hours - hrsperweek

     #calculate the amount of overtime pay.
     Ovrtime = hrsperweeks *payRate * Ovrtime 

     #calculate the gross pay.
     gross_pay = base_hours * payRate *overtime_pay
   else:
      #calculate the gross pay without overtime.
      grosspay = hours * payRate 
'''


     




