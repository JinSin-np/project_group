from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"overheads.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store time sheet and overhead record
    overheadRecords=[]

    # append time sheet and sales record into the overheadRecords list
    for row in reader:
        #get the day, items and amount for each record
        #and append the salesRecords list
        overheadRecords.append([row[0],row[1],row[3]])
print(overheadRecords)