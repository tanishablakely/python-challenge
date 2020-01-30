#%%writefile main.py

# Store the file path associated with the file (note the backslash may be OS specific)
import os
import csv

csv_path = '03-Python_budget_data.csv'

with open(csv_path) as csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Skip Header
    csv_header = next(csv_reader)
    total_months = 0
    total_amount = 0
    previous_amount = 0
    current_amount = 0
    changes = []
    total_change = 0
    average_change = 0 
    max_change = 0
    min_change = 0
    
    print ("Financial Analysis\n----------------")

    for row in csv_reader:
        current_amount = row[1]
        
        #Calculate change in "Profit/Losses" from a previous period after the first month.
        if total_months > 0:
            changes.append(int(current_amount) - int(previous_amount))
        # The total number of months included in the dataset
        total_months = total_months + 1
        
        # The net total amount of "Profit/Losses" over the entire period
        total_amount = total_amount + int(current_amount)
        
        # Set value for the next iteration
        previous_amount = current_amount
    #for (month, change) in changes.items():
    for change in changes:
        # The total change in "Profit/Losses"
        total_change = total_change + change
        
    #The average of the changes in "Profit/Losses" over the entire period
    average_change = total_change/total_months
        
    #Print results
    print (f"Total Months: {total_months}")
    print (f"Total: ${total_amount}")
    print (f"Average Change: ${round(average_change,2)}")
    print (f"Greatest Increase in Profits: ${max(changes)}")
    print (f"Greatest Decrease in Profits: ${min(changes)}")