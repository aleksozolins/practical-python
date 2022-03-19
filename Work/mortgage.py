# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
ex_payment_amt = 1000
ex_payment = 0
total_paid = 0.0
month = 0

while principal > 0 and ex_payment < 12:
    principal = principal * (1+rate/12) - payment - ex_payment_amt * ex_payment
    total_paid = total_paid + payment + ex_payment
    print (month, total_paid)
    month = month + 1

print('Total paid', round(total_paid, 2))
