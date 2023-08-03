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
        Cash_on_hand.append([row[0],int(row[1])])

print(Cash_on_hand)

def print_cash_deficit(data):
    if len(data) < 2:
        return

    # Initialize prev_cash with the first day's cash amount
    day, prev_cash = data[0]

    for next_day, cash in data[1:]:
        if cash < prev_cash:
            deficit = prev_cash - cash
            print(f"[CASH DEFICIT] DAY: {next_day}, AMOUNT: {deficit}")
        prev_cash = cash
        # elif prev_cash > cash:
        #     print(f"CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
            # print(f"[HIGHEST CASH SURPLUS] DAY: {}, AMOUNT: {}")




print_cash_deficit(Cash_on_hand)

