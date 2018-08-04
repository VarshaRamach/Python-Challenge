# Module dependencies
import os
import csv

output_file = "Financial_Summary_Statement.txt"

# Set path for file
filepath = 'Resources/budget_data.csv'

# Open the CSV
with open(filepath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# to hide header and start at line 2 
    Header = next(csvfile, None)

# Initialize variables
    total_months = 0
    total_revenue = 0
    total_change = 0
    delta_revenue = 0
    previous_revenue = 0
    list_change = []
    list_months = []
    greatest_profit = [" ", 0]
    greatest_loss = [" ", 0]

# to track total months and total revenue included in dataset
    for row in csvreader:
        month_year = row[0]
        list_months.append(month_year)
        
        revenue = float(row[1])
        list_change.append(revenue - previous_revenue)
        total_revenue += revenue
        previous_revenue = revenue

    # Looping to calculate change in revenue    
        total_months = len(list_months)
        for a in range(1, len(list_months)):
            delta_revenue = list_change[a] - list_change[a-1]
            total_change += delta_revenue
            
            if delta_revenue > greatest_profit[1]:
                greatest_profit = [list_change[a], delta_revenue]
                increase_date = row[0]
            
            elif delta_revenue < greatest_loss[1]:
                greatest_loss = [list_change[a], delta_revenue]
                decrease_date = row[0]


    # Calculating Average Revenue
    avg_revenue = round(sum(list_change) / len(list_months))


# Generate output
output = (
    f"\n Financial Analysis for XYZ Company \n"
    f"\n ======================================================= \n"
    f"\n Total Months: {total_months} \n"
    f"\n Total: $ {total_revenue} \n"
    f"\n Average Change: $ {avg_revenue} \n"
    f"\n Greatest Increase in Profits: {increase_date} (${greatest_profit[1]}) \n "
    f"\n Greatest Decrease in Profits: {decrease_date} (${greatest_loss[1]}) \n"
)
# Display output in terminal
print(output)

# Export summary to .txt file
with open(output_file, "w+") as txt_file:
    txt_file.write(output)

