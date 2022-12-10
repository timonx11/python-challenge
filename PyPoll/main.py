# In this Challenge, you are tasked with helping a small, rural U.S. town modernise its vote-counting process.
# You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote
# Your analysis should align with the following results:

# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------

#importing Module os and csv and path for relative path 
import os
import csv
from pathlib import Path
#print header for the analysis result
print("Election Results")
print("-------------------------------")

#defining the path of resources file (im not 100 percent sure for this but when im on the virtual environtment, i can read the file with below path but i will need to specify a full path for the assignment to run after i move it to GitHub)
# csvfpath = os.path.join("..", "Resources", "election_data.csv")
csvfpath = os.path.join("Resources/election_data.csv")


#Declaring an empty list to hold and separate values from the csv file
votes = []
candidates = []
Charles = []
Diana = []
Raymon = []

#read through the csv resource file, formating the looks and feel and set delimiter for the dictionary
with open(csvfpath, "r", newline="",encoding='utf') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")

    #for loop to go through the csv file and separate the value columns to the months list and profitloss list
    for row in csvreader:
        votes.append(row["Ballot ID"])
        candidates.append(row["Candidate"])

    #for loop to go count the number of votes each candidates get and put it on separate list to extract the results further 
    for x, candidate in enumerate(candidates):
        if candidate == 'Raymon Anthony Doane':
            Raymon.append(candidates[x])
        elif candidate == 'Charles Casper Stockham':
            Charles.append(candidates[x])
        elif candidate == 'Diana DeGette':
            Diana.append(candidates[x])
        else:
            print("Unlisted Candidates")

    #declaring a variable for each candidate to get the votes percentage result    
    raymon_percent = round(((len(Raymon)/len(votes))*100),3)
    diana_percent = round(((len(Diana)/len(votes))*100),3)
    charles_percent = round(((len(Charles)/len(votes))*100),3)
    
    #variable needed to compare the results and decide the winner
    can1 = len(Diana)
    can2 = len(Raymon)
    can3 = len(Charles)
    #creating a function to compare the vote results
    def max_num(can1, can2, can3):
        if can1 > can2:
            if can1 > can3:
                return (Diana[27])
            else:
                return (Charles[0])
        else:
            if can2 > can3:
                return (Raymon[13])
            else:
                return (Charles[0])


#print the election results
print("Total Votes:", len(votes))
print("-------------------------------")
print(f"Charles Casper Stockham: {str(charles_percent)}% ({len(Charles)})")
print(f"Diana DeGette: {str(diana_percent)}% ({len(Diana)})")
print(f"Raymon Anthony Doane: {str(raymon_percent)}% ({len(Raymon)})")
print("-------------------------------")
print(f"Winner: {max_num(can1,can2,can3)}")
print("-------------------------------")

#creating new list to export / write the election result to txt file
lines = ['Election Results',
'-------------------------',
'Total Votes: 369711',
'-------------------------',
'Charles Casper Stockham: 23.049% (85213)',
'Diana DeGette: 73.812% (272892)',
'Raymon Anthony Doane: 3.139% (11606)',
'-------------------------',
'Winner: Diana DeGette',
'-------------------------']

# with open('c:/Users/timn/Documents/GitHub/python-challenge/PyPoll/Analysis/readme.txt', 'w') as f:
#defining the path of written file (im not 100 percent sure for this but when im on the virtual environtment, i can write the file with below path but i will need to specify a full path for the assignment to run after i move it to GitHub)

path = Path(__file__).parent / "Analysis/readme.txt"
with open(path,'w') as f:
#Looping trough the list to export / write the result to txt file
    for line in lines:
        f.write(line)
        f.write('\n')