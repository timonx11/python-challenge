# Your task is to create a Python script that analyses the records to calculate each of the following values:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period
#-------------------------------------------------------------------------------------------------------------------
# Your analysis should align with the following results:
#-------------------------------------------------------------------------------------------------------------------
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198

# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#importing Module os and csv and path for relative path 
import os
import csv
from pathlib import Path

#print header for the analysis result
print("Financial Analysis")
print("-------------------------------------------------------------------")

#defining the path of resources file (im not 100 percent sure for this but when im on the virtual environtment, i can read the file with below path but i will need to specify a full path for the assignment to run when i move it to GitHub
# csvfpath = os.path.join("..", "Resources", "budget_data.csv")
csvfpath = os.path.join("Resources/budget_data.csv")

#Declaring an empty list to hold and separate values from the dictionary from the csv file
profitloss = []
months = []
increase = []

#read through the csv resource file, formating the looks and feel and set delimiter for the dictionary
with open(csvfpath, "r", newline="",encoding='utf') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")

    #for loop to go through the csv file and separate the value columns to the months list and profitloss list
    for row in csvreader:
        months.append(row["Date"])
        profitloss.append(int(row["Profit/Losses"]))
    
    #for loop to get the number if iteration to get the average changes 
    for x in range(len(profitloss)):
        count = x 

    #use a comprehension to get the difference beetween value and the next value and we also need to zip it so we can iterate it
    increase = [x[0]-x[1] for x in zip(profitloss[1:],profitloss[:-1])]
    #add an extra 0 value to the increase list for indexing purpose
    increase.insert(0, 0)

    #create a new empty dictionary so we can merge the 2 List (increase and months)
    m = {}
    #fill up new dictionary
    for i in range(len(increase)):
	    m[months[i]] = increase[i]

#get max values of the diference and assign in to max_increase variable    
max_increase = max(m.values())
#get the key associated with the max values and assign it to max_key variable
max_key = max(m, key=m.get)
#get min values of the diference and assign in to min_increase variable    
min_increase = min(m.values())
#get the key associated with the min values and assign it to min_key variable
min_key = min(m, key=m.get)
#get the average changes of the profit loss and assign it to avgchanges table
avgChanges = round(((profitloss[-1] - profitloss[0])/count),2)      

#displaying the rest of analysis results
print("Total Months:", len(months))
print(f"Total: ${str(sum(profitloss))}")
print("")
print(f"Average Change: ${str(avgChanges)}")
print(f"Greatest Increase in Profits: {str(max_key)} (${str(max_increase)})")
print(f"Greatest Decrease in Profits: {str(min_key)} (${str(min_increase)})")           

#creating new list to export / write the analysis result to txt file
lines = ['Financial Analysis',
'-------------------------------------------------------------------',
'Total Months: 86',
'Total: $22564198',
'Average Change: $-8311.11',
'Greatest Increase in Profits: Aug-16 ($1862002)',
'Greatest Decrease in Profits: Feb-14 ($-1825558)']


#defining the path of resources file (im not 100 percent sure for this but when im on the virtual environtment, i can read the file with below path but i will need to specify a full path for the assignment to run when i move it to GitHub)
path = Path(__file__).parent / "Analysis/readme.txt"
with open(path,'w') as f:
#Looping trough the list to export / write the result to txt file
    for line in lines:
        f.write(line)
        f.write('\n')
    
    

          
    