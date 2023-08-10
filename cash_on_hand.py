from pathlib import Path
import csv


# create a file to csv file.
def COH_data_reader():
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
    
    """

    COH_data_reader() #calls function to read COH file

 # variables to store cash
    change_in_cash = []
    cash_deficit_days = []
    largest_surplus = []

print(Cash_on_hand)

def print_cash_deficit(data):
    if len(data) < 2: # checks if the length of the data list is less than 2
        return

    # Initialize prev_cash with the first day's cash amount
    day, prev_cash = data[0] # assigns the first day and cash amount to variables

    for next_day, cash in data[1:]: # loops through the data list starting from the second element
        if cash < prev_cash: # if previous day cash is less than current day cash print the following line
            deficit = prev_cash - cash
            print(f"[CASH DEFICIT] DAY: {next_day}, AMOUNT: {deficit}")
        prev_cash = cash #
        # elif prev_cash > cash: # if previous day cash is more than current day cash print the following line
        #     print(f"CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
            # print(f"[HIGHEST CASH SURPLUS] DAY: {}, AMOUNT: {}")




print_cash_deficit(Cash_on_hand)

