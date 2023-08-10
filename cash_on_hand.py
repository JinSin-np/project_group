from pathlib import Path
import csv


# create a file to csv file.
def COH_data_reader():
    '''
    Function reads COH.csv file and appends data to a list
    No parameters needed
    '''
    fp = Path.cwd()/"COH.csv"
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        # create an empty lists to store Cash on hand record
        global Cash_on_hand
        Cash_on_hand = [] 

        # append Cash on hand record into the Cash_on_hand list
        for row in reader:
            #get the day, items and profit for each record
            #and append the salesRecords list
            Cash_on_hand.append([row[0],int(row[1])])
    return Cash_on_hand #returns cash on hand list

def print_cash_deficit():
    """
    Function to calculate cash deficit days or highest cash surplus day
    No parameters required
    """

    COH_data_reader() #calls function to read COH file

 # variables to store cash
    change_in_cash = []
    cash_deficit_days = []
    largest_surplus = []

    for day,cash in enumerate(Cash_on_hand[1:],start=1):
            cash_change = cash[1] - Cash_on_hand[day - 1][1]
            change_in_cash.append([day, cash_change])

        # Finds the days where cash is lower than the previous day and appends it to profit_deficit_days list
    for item in change_in_cash:
            if item[1] < 0:
                cash_deficit_days.append(item)
        # Checks if cash is always increasing
    if cash_deficit_days == []:
            # returns the day with the highest amount increment
            largest_surplus.append([max(change_in_cash, key=lambda x: x[1])])
            return largest_surplus
        
        # Returns days where profit is in a deficit
    return (cash_deficit_days)


