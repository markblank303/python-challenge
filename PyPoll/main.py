#import the os module and module for reading csv files
import os
import csv

poll_data = os.path.join("Resources","election_data.csv") #file where data is held

#dictionary for name and count
candidates = {}


#read through csv file
with open(poll_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header=next(csvfile)#skips header

    for row in csvreader:
        if row[2] in candidates.keys():
            candidates[row[2]]+=1
        else:
            candidates[row[2]] = 1

        total = candidates.values()
        total_votes = sum(total)

            
        list_candidates = candidates.keys()
        #find percentage of votes    
        votes_per = [f'{(x/total_votes)*100:.3f}%' for x in candidates.values()]
            
        #find winner
        winner = list(candidates.keys())[list(candidates.values()).index(max(candidates.values()))]
        
        

#print the Results in gitbash/terminal
print(" ")
print("Election Results")
print("--------------------------")
print(f" Total Votes: {int(total_votes)}")
print("--------------------------")
i = 0
for candidate, vote in candidates.items():
    print(f'{candidate}: {votes_per[i]} ({vote})') 
    i+=1
print("--------------------------")
print(f" Winner: {winner}")
print("--------------------------")

#create new txt file and print to it
analysis_file = os.path.join("Analysis","analysis.txt")
with open(analysis_file, "w") as file:   
    file.write("Election Results" + "\n")
    file.write("..................................." + "\n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("..................................." + "\n")
    i = 0
    for candidate, vote in candidates.items():
        file.write(f'{candidate}: {votes_per[i]} ({vote})\n') 
        i+=1
    file.write("..................................." + "\n")
    file.write("Winner: "  + winner + "\n")
    file.write("..................................." + "\n")

