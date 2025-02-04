# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1
extra_payment_start_month = int(input('Extra payment start month: '))
extra_payment_end_month = int(input('Extra payment end month: '))
extra_payment_amount = int(input('Enter amount: '))

while principal > 0:
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal * (1+rate/12) - payment - extra_payment_amount
        total_paid = total_paid + payment + extra_payment_amount
        if principal < 0:
            total_paid = total_paid - principal
            principal = principal - principal
        print (f'month={month}, total paid={total_paid:0.2f}, principal={principal:0.2f}, *')
        month = month + 1
    else:
        month < extra_payment_start_month or month > extra_payment_end_month
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        if principal < 0:
            total_paid = total_paid - principal
            principal = principal - principal
        print (f'month={month}, total paid={total_paid:0.2f}, principal={principal:0.2f}')
        month = month + 1

print('Total paid', round(total_paid, 2))
