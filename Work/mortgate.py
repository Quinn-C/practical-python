#!/usr/bin/env python3
'''
Plan

'''
principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment=1000
total_paid = 0.0
month=1
i = 0
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    i = i + 1
    if i < extra_payment_start_month or i > extra_payment_end_month:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

    else:
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
    if principal < 0:
        break
    print(i, round(total_paid, 2), round(principal, 2))

print('Total paid', total_paid)


with op
