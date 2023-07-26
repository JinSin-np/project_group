from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"profit-and-loss.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store time sheet and Profit and Loss record
    PandL_Record = [] 

    # append time sheet and profit and loss record into the PandL_Records list
    for row in reader:
        #get the day, items and profit for each record
        #and append the salesRecords list
        PandL_Record.append([row[0],int(row[4])])

def profit_deficit_calculator():
    '''
    Calculates the change in net profit then returns the days where the net profit is lower than the previous day as a list (returns change as a negeative number).
    if the net profit is always increasing, returns the day with the highest amount increment (returns change as a positive number)
    required parameters: None
    '''
    # List to store values
    change_in_net_profit = []
    profit_deficit_days = []

    # Calculates the daily change in net profit and appends it to change_in_net_profit list
    for day,profit in enumerate(PandL_Record[1:],start=1):
        net_profit_change = profit[1] - PandL_Record[day - 1][1]
        change_in_net_profit.append([day, net_profit_change])

    # Finds the days where net profit is lower than the previous day and appends it to profit_deficit_days list
    for item in change_in_net_profit:
        if item[1] < 0:
            profit_deficit_days.append(item)

    # Checks if net profit is always increasing
    if profit_deficit_days == []:
        # returns the day with the highest amount increment
        return max(change_in_net_profit, key=[1])

print(profit_deficit_calculator())




