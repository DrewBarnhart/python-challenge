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

    header = next(reader)

    #row = reader[i]
    for row in reader:
    # for i in range(1000)
        current = int(row[1])
        total_amount = total_amount + current
        #total_amount += current

        if total_months == 0:
            profits_loss_list.append(0)
        else:
            current_profit_loss = current - previous
            profits_loss_list.append(current_profit_loss)

            if current_profit_loss > max_increase_value:
                max_increase_value = current_profit_loss
                max_increase_month = row[0]
            elif current_profit_loss < min_increase_value:
                min_increase_value = current_profit_loss
                min_increase_month = row[0]
        
        previous = current


        total_months = total_months + 1
       
        # total_months += 1

print("Financial Analysis")
print("-"*20)
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount:,}")
print(f"Avg. Change: ${sum(profits_loss_list) / (total_months-1):,.2f}")
print(f"Max P/L: {max_increase_month} (${max_increase_value:,})")
print(f"Min P/L: {min_increase_month} (${min_increase_value:,})")

with open(path_to_analysis, 'w') as analysis_file:
    analysis_file.write("Financial Analysis\n")
    analysis_file.write("-"*20)
    analysis_file.write(f"\nTotal Months: {total_months}\n")
    analysis_file.write(f"Total: ${total_amount:,}\n")
    analysis_file.write(f"Avg. Change: ${sum(profits_loss_list) / (total_months-1):,.2f}\n")
    analysis_file.write(f"Max P/L: {max_increase_month} (${max_increase_value:,})\n")
    analysis_file.write(f"Min P/L: {min_increase_month} (${min_increase_value:,})\n")

