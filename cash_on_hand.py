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

def find_deficits(Cash_on_hand):
    deficits = []
    for day in range(1, len(Cash_on_hand)):
        previous_cash = Cash_on_hand[day - 1][1]
        current_cash = Cash_on_hand[day][1]
        deficit = previous_cash - current_cash

        if deficit > current_cash:
            day = int(Cash_on_hand[day][0])
            deficits.append((day, deficit))

    # for day, deficit in deficits:
        print(f"[CASH DEFICIT] DAY: {day}, AMOUNT: {deficit}")

find_deficits(Cash_on_hand)

def bob(Cash_on_hand):
    final_amount = []
    for day in range(1, len(Cash_on_hand)):
        previous_cash = Cash_on_hand[day - 1][1]
        current_cash = Cash_on_hand[day][1]
        amount = previous_cash - current_cash

        if amount > 0:
            day = int(Cash_on_hand[day][0])
            final_amount.append((day, amount))
        
        print(f"[CASH DEFICIT] DAY: {day}, AMOUNT: {amount}")

#         elif current_cash > amount:
#             highest_amount = current_cash
#             highest_amount_day = int(Cash_on_hand[day][0])
#             print("Cash surplus is higher every day")
#     # if highest_amount_day > 0:
#             print(f"Highest cash amount: USD{highest_amount} on DAY: {highest_amount_day}")

# bob(Cash_on_hand)




