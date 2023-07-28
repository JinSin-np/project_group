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

# print(Cash_on_hand)

# Convert the amount data to a list of integers
amounts = [int(item[1]) for item in Cash_on_hand]

increasing_period = []
decreasing_period = []

# Check for increasing and decreasing periods
current_trend = None
current_period = []

for i in range(1, len(amounts)):
    if amounts[i] > amounts[i - 1]:  # If amount increased from previous day
        if current_trend == "increasing":
            current_period.append(int(Cash_on_hand[i][0]))
        else:
            if current_period:
                increasing_period.append(current_period)
            current_trend = "increasing"
            current_period = [int(Cash_on_hand[i][0])]
    elif amounts[i] < amounts[i - 1]:  # If amount decreased from previous day
        if current_trend == "decreasing":
            current_period.append(int(Cash_on_hand[i][0]))
        else:
            if current_period:
                decreasing_period.append(current_period)
            current_trend = "decreasing"
            current_period = [int(Cash_on_hand[i][0])]

# Append the last period
if current_trend == "increasing":
    increasing_period.append(current_period)
elif current_trend == "decreasing":
    decreasing_period.append(current_period)

# Output the results
# for period in increasing_period:
#     print(f"Day {period[0]} to {period[-1]}: Increase in cash surplus")

# for period in decreasing_period:
#     print(f"Day {period[0]} to {period[-1]}: Decrease in cash surplus")

def
max_increase = 0
max_increase_day = 0

for i in range(1, len(Cash_on_hand)):
    previous_cash = Cash_on_hand[i - 1][1]
    current_cash = Cash_on_hand[i][1]
    increase = current_cash - previous_cash
    if increase > max_increase:
        max_increase = increase
        max_increase_day = int(Cash_on_hand[i][0])
print(f"Day: {max_increase_day}, AMOUNT: USD{max_increase}")









