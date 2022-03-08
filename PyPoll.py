
# Importing the date
import datetime as dt
now  = dt.datetime.now()
print ('The time right now is' , now)

import csv
import os
# file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")
# election_data  = open(file_to_load,"r")
with open(file_to_load) as election_data:
    file_reader  = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

    # 1. Initialize a total vote counter.
    total_votes = 0
    candidate_options = []
    candidate_votes = {}
    for row in file_reader:
        total_votes+=1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] =0
        
        candidate_votes[candidate_name]+=1

#The total number of votes cast
print(total_votes)
#A list of candidates
print(candidate_options)
#the percentage of votes each candidate won
for candidate_name in candidate_votes:
    vote_percentage = (candidate_votes[candidate_name] / total_votes) * 100
    print(f'{candidate_name}: recieved {vote_percentage:.1f}% of the votes')
    
# the total of votes each candidate won
print(candidate_votes)
#The winner of the election based on popular vote
winning_candidate = ""
winning_count = 0
winning_percentage = 0
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name


winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


file_to_save = os.path.join("Analysis","election_analysis.txt")
# outfile = open(file_to_save,'w')
# outfile.write("hello world\n")
# outfile.close

with open(file_to_save,"w") as txt_file:
    txt_file.write(winning_candidate_summary)
    
# election_data.close()

