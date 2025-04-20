#Jayson Hamilton
# This program displays property taxes.

state_tax = float (0.025)
county_tax = float (0.05)
value = float (0.0)
total_tax = state_tax + county_tax
tax = value * total_tax


#TAX_FACTOR = 0.0065 # Represents the tax factor.

# Get the first lot number.
print('Enter the item amount or enter 0 to end.:')

item = int(input('Item Number:'))
#print('Enter the property lot number or enter 0 to end.')
#lot = int(input('Lot number: '))

# Continue processing as long as the user
# Enter zero to exit.
while item != 0:
    # Get the property value.
    value = float(input('Price of item:'))
   
    tax = value * total_tax

    # Display the tax.
    print(f'state tax: ${state_tax:,.2f}')
    print(f'county tax: ${county_tax:,.2f}')
    print('total amount:' ,(tax * total_tax + value))
    
    # Get the next item number.
    print('Enter the next item amount or enter 0 to end.:')
    #print('Enters item number.')
    item = int(input('Item Number: '))
    
