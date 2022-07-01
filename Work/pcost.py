#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27
# 1. Read file
# 2. Transfer each line of string to list
# 3. use row[1]*row[2] in each line, use for loop to add all results together
import csv

def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            total_cost = total_cost + int(row[1])*float(row[2])

    return float(total_cost)

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
