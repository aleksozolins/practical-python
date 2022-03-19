# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1

while month < 13:
    principal = principal * (1+rate/12) - payment - 1000
    total_paid = total_paid + payment + 1000
    print (month, 'extra', total_paid)
    month = month + 1

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    print (month, total_paid)
    month = month + 1

print('Total paid', round(total_paid, 2))
