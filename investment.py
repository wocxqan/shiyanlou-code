#!/usr/bin/env python3
amount = float(input("Enter amount: "))
inrate = float(input("Enter interest rate: "))
period = int(input("Enter period: "))
year = 1
value = 0

while year <= period:
    value = amount + (amount * inrate)
    print("Year {} Rs. {:.2f}".format(year, value))
    amount = value
    year += 1

