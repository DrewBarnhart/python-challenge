import csv
import os

path_to_csv = os.path.join("Resources", "election_data.csv")
path_to_analysis = os.path.join("Analysis", "analysis.txt")

total_votes = 0
candidates = {}
# 0, 1, 2, 3, 
# Charles : 800

with open(path_to_csv) as bank_csv:
    reader = csv.reader(bank_csv)

    header = next(reader)

    #row = reader[i]
    for row in reader:
        total_votes = total_votes + 1

        current_candidate = row[2]

        if current_candidate in candidates:
            candidates[current_candidate] += 1
        else:
            candidates[current_candidate] = 1

print(candidates)

#print(candidates.keys())
#print(candidates.values())
#print(candidates.items())

# ADD TITLE AND TOTAL VOTES

winner_name = ""
winner_votes = 0

for c, v in candidates.items():
    if v > winner_votes:
        winner_votes = v
        winner_name = c
    print(f"{c} {v/total_votes:.3%} ({v:,})")

print("-"*20)
print(f"WINNER:  {winner_name} ({winner_votes:,} votes)")

# with open and write to file


