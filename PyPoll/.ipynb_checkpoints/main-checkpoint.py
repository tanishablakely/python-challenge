#%%writefile main.py
import os
import csv
with open('election_data.csv', 'r') as csv_file:
    csv_reader_object = csv.reader(csv_file, delimiter=',')

#Set Variables
    #Skip Header
    header = next(csv_reader_object)
    
    # The total number of votes cast
    total_votes = 0
    
    # Track Candidate Votes
    candidates = dict()
    winner = ''
    
    for row in csv_reader_object:
        total_votes = total_votes + 1
        if row[2] in candidates:
            candidates[row[2]] = candidates[row[2]] + 1
        else:
            candidates[row[2]] = 1
    # The winner of the election based on popular vote.        
    winner = max(candidates.items(), key=lambda x : x[1])

    # Print Election Results

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    
   
    # The percentage and total number of votes each candidate won
    for candidate, votes in candidates.items():
        print(f"{candidate}: {round(votes*100/total_votes,3)}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner[0]}")
    print("-------------------------")
    
    # Final script should both print the analysis to the terminal and export a text file with the results.
    with open('results.txt', 'w') as output_file: 
        output_file.write("Election Results\n-------------------------\n")
        output_file.write(f"Total Votes: {total_votes}\n")
        output_file.write("-------------------------\n")
        for candidate, votes in candidates.items():
            output_file.write(f"{candidate}: {round(votes*100/total_votes,3)}% ({votes})\n")
        output_file.write("-------------------------\n")    
        output_file.write(f"Winner: {winner[0]}\n")
        output_file.write("-------------------------")