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

# max_increase = 0
# max_increase_day = 0

# for i in range(1, len(Cash_on_hand)):
#     previous_cash = Cash_on_hand[i - 1][1]
#     current_cash = Cash_on_hand[i][1]
#     increase = current_cash - previous_cash
#     if increase > max_increase:
#         max_increase = increase
#         max_increase_day = int(Cash_on_hand[i][0])
# print(f"The day with the highest increase is Day {max_increase_day} with an increase of ${max_increase}")

# first_amount = Cash_on_hand[0][1]
# last_amount = Cash_on_hand[-1][1]

# if last_amount > first_amount:
#     print("The amount has been increasing in general.")
# elif last_amount < first_amount:
#     print("The amount has been decreasing in general.")
# else:
#     print("The amount has not changed in general.")


increasing_days = []
decreasing_days = []

# Convert the amount data to a list of integers
amounts = [int(item[1]) for item in Cash_on_hand]

# Check for increasing and decreasing days
for i in range(1, len(amounts)):
    if amounts[i] > amounts[i - 1]:  # If amount increased from previous day
        increasing_days.append(int(Cash_on_hand[i][0]))
    elif amounts[i] < amounts[i - 1]:  # If amount decreased from previous day
        decreasing_days.append(int(Cash_on_hand[i][0]))

# Output the results
if increasing_days:
    print("The amount has been increasing on days:", increasing_days)
else:
    print("There is no increasing day.")

if decreasing_days:
    print("The amount has been decreasing on days:", decreasing_days)
else:
    print("There is no decreasing day.")