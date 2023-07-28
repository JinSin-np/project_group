from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"COH.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store time sheet and Profit and Loss record
    Cash_on_hand = [] 

    # append time sheet and profit and loss record into the PandL_Records list
    for row in reader:
        #get the day, items and profit for each record
        #and append the salesRecords list
        Cash_on_hand.append([row[0],int(row[4])])

# Convert the amount data to a list of integers
amounts = [int(item[1]) for item in Cash_on_hand]

increasing_period = []
decreasing_period = []

# Check for increasing and decreasing periods
current_trend = None
current_period = []

for day in range(1, len(amounts)):
    if amounts[day] > amounts[day - 1]:  # If amount increased from previous day
        if current_trend == "increasing":
            current_period.append(int(Cash_on_hand[day][0]))
        else:
            if current_period:
                increasing_period.append(current_period)
            current_trend = "increasing"
            current_period = [int(Cash_on_hand[day][0])]
    elif amounts[day] < amounts[day - 1]:  # If amount decreased from previous day
        if current_trend == "decreasing":
            current_period.append(int(Cash_on_hand[day][0]))
        else:
            if current_period:
                decreasing_period.append(current_period)
            current_trend = "decreasing"
            current_period = [int(Cash_on_hand[day][0])]

# Append the last period
if current_trend == "increasing":
    increasing_period.append(current_period)
elif current_trend == "decreasing":
    decreasing_period.append(current_period)

# Output the results
for period in increasing_period:
    print(f"Day {period[0]} to {period[-1]}: Increase in cash surplus")

for period in decreasing_period:
    print(f"Day {period[0]} to {period[-1]}: Decrease in cash surplus")

# Scenerio 1
def max_increase_decrease_finder(Cash_on_hand):
    greatest_cash_surplus_increase = 0
    day_of_greatest_increase = 0
    day_of_greatest_decrease = 0
    greatest_cash_surplus_decrease = 0

    for day in range(1, len(Cash_on_hand)):
        previous_cash_on_hand = Cash_on_hand[day - 1][1]
        current_cash_on_hand = Cash_on_hand[day][1]
        change_in_cash_on_hand = current_cash_on_hand - previous_cash_on_hand
        
        if change_in_cash_on_hand > greatest_cash_surplus_increase:
            greatest_cash_surplus_increase = change_in_cash_on_hand
            day_of_greatest_increase = int(Cash_on_hand[day][0])
        
        if change_in_cash_on_hand < greatest_cash_surplus_decrease:
            greatest_cash_surplus_decrease = change_in_cash_on_hand
            day_of_greatest_decrease = int(Cash_on_hand[day][0])

    print(f"[HIGHEST CASH SURPLUS] Day: {day_of_greatest_increase}, AMOUNT: USD{greatest_cash_surplus_increase}")
    print(f"[HIGHEST CASH DEFICIT] Day: {day_of_greatest_decrease}, AMOUNT: USD{greatest_cash_surplus_decrease}")
    

# Call the function to find and print the results
max_increase_decrease_finder(Cash_on_hand)










