
# This program display: the purchase, the state sales tax, the county sales tax, the total sales tax, and the total of the sale.

state_tax = 0.025
county_tax = 0.05
total_tax = state_tax + county_tax

# Get the first item number and amount.
print('Enter the item amount or enter 0 to end.:')
item = int(input('Item Number:'))

# Continue processing as long as the user
# does not enter item number 0.
while item != 0:
    # Get the Item value.
    value = float(input('Price of item:'))

    # Calculate the Item's tax.
    tax = value * total_tax

    # Display the tax.
    print(f'state tax: ${state_tax:,.2f}')
    print(f'county tax: ${county_tax:,.2f}')
    print('total amount:' ,(tax * total_tax + value))

    # Get the next item number.
    print('Enter the item amount or enter 0 to end.:')
    #print('Enter the next lot number or enter 0 to end.')
    item = int(input('Item Number: '))
