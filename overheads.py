from pathlib import Path
import csv
def overheads_path_reader():
    '''
    Function to read overheads.csv file and appends data
    No parameters required
    '''
# create a file to csv file.
    fp = Path.cwd()/"overheads.csv"

    # read the csv file to append profit and quantity from the csv.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        # create an empty lists to store time sheet and overhead record
        global overheadRecords
        overheadRecords=[]

        # append time sheet and sales record into the overheadRecords list
        for row in reader:
            #get the day, items and amount for each record
            #and append the salesRecords list
            overheadRecords.append([row[0],row[1],row[3]])
        return overheadRecords

def largest_overheads():
    '''
    Function to calculate the largest overhead and its percentage
    '''
    # Create a dictionary to store the total overhead for each category
    overheads_path_reader()
    overheadCategories = {}

    # Calculate total overhead for each category
    for record in overheadRecords:
        category = record[1]
        amount = float(record[2])
        if category in overheadCategories:
            overheadCategories[category] += amount
        else:
            overheadCategories[category] = amount

    # Find the category with the highest overhead
    highest_overhead_category = max(overheadCategories, key=overheadCategories.get)
    highest_percentage = round((overheadCategories[highest_overhead_category] / sum(overheadCategories.values())) * 100,2)
    return highest_overhead_category, highest_percentage

