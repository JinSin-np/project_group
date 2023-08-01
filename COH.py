from pathlib import Path
import csv


# create a file to csv file.
fp = Path.cwd()/"COH & P&L.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store time sheet and Profit and Loss record
    Cash_on_hand = [] 

    # append time sheet and profit and loss record into the PandL_Records list
    for row in reader:
        #get the day, items and profit for each record
        #and append the salesRecords list
        Cash_on_hand.append([row[0],int(row[3])])

print(Cash_on_hand)

# def COH (Cash_on_hand):
#     Positive_Cash_on_hand = 0
#     expenses = 0
#     Revenue_1 = 0
#     for items in Cash_on_hand:
#         if items[1] == "Wholesales (B2B)" or "Retail" or "Sales E Commerce" or "Services":
#             Revenue_1 += items[3]
#             print(Revenue_1)

# COH(Cash_on_hand)