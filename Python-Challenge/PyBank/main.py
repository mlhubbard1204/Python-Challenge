
import csv
import os


months = []
profit = []

budget_data = os.path.join('Desktop', 'Python-Challenge', 'PyBank', 'budget_data.csv')


with open(budget_data, newline="") as csvfile:
    budget = csv.reader(csvfile, delimiter=",")

 
    next(budget)

 
    for row in budget:

        
        months.append(row[0])

        
        profit.append(float(row[1]))


total_time = (len(months))


total_profit = sum(profit)


change = total_profit / total_time


max_profit = max(profit)


index_max = profit.index(max_profit)
max_month = months[index_max]


min_profit = min(profit)


index_min = profit.index(min_profit)
min_month = months[index_min]

analysis = (f'''Financial Analysis
Total Months: {total_time}
Total: ${total_profit}
Average Change: {change}
Greatest Increase in Profits: {max_month} {max_profit}
Greatest Decrease in Profits: {min_month} {min_profit:}''')

print(analysis)
