from pathlib import Path
import csv

# create a file to csv file.
def profit_and_loss_file_reader():
    '''
    Function to read overheads.csv file and appends data
    No parameters required
    '''
    fp = Path.cwd()/"project_group"/"csv_reports"/"profit_and_loss.csv"
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        global PandL_Record
        # create an empty lists to store time sheet and Profit and Loss record
        PandL_Record = [] 

        # append time sheet and profit and loss record into the PandL_Records list
        for row in reader:
            #get the day, items and profit for each record
            #and append the salesRecords list
            PandL_Record.append([row[0],float(row[1])])
    return PandL_Record

def profit_deficit_calculator():
    '''
    Calculates the profit deficit days or highest profit surplus day
    required parameters: None
    '''
    # List to store values

    # calls function to read Net-Profit file
    profit_and_loss_file_reader()
    
    change_in_net_profit = []
    profit_deficit_days = []
    largest_surplus = []

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
        largest_surplus.append([max(change_in_net_profit, key=lambda x: x[1])])
        return largest_surplus
    
    # Returns days where profit is in a deficit
    return (profit_deficit_days)
    




