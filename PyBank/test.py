import csv
import os

path_to_csv = os.path.join("Resources", "budget_data.csv")
path_to_analysis = os.path.join("Analysis", "analysis.txt")

total_months = 0
total_amount = 0
previous = 0
profits_loss_list = []

max_increase_value = 0
max_increase_month = ""

min_increase_value = 0
min_increase_month = ""

with open(path_to_csv) as bank_csv:
    reader = csv.reader(bank_csv)
    # print(reader[0])
    for row in reader:
       # print (row)
        # for column in row:
        #     print(type(column),end=" ")
        print (row[1])