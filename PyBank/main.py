#import the os module and module for reading csv files
import os
import csv

budget_data = os.path.join("Resources","budget_data.csv") #file where data is held

#read through csv file
with open(budget_data) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header=next(csvfile) #skip header row

    #variables/lists
    months = []
    Profit = []
    revenue_change = []

    for rows in csvreader:#read through cvs after header
        months.append(rows[0])
        Profit.append(int(rows[1]))
        
    for x in range(1, len(Profit)):#look for revenue change
        revenue_change.append((int(Profit[x]) - int(Profit[x-1])))

        revenue_average = sum(revenue_change) / len(revenue_change)#find average rev change
    
        total_months = len(months)#total # of months/length
    
        greatest_increase = max(revenue_change)#greatest incr in rev change
    
        greatest_decrease = min(revenue_change)#greatest decr in rev change

#print the Results in gitbash/terminal
    print(" ")
    print("Financial Analysis")
    print(".........................................................")
    print("total months: " + str(total_months))
    print("Total: " + "$" + str(sum(Profit)))
    print("Average change: " + "$" + str(revenue_average))
    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))
    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))

#create new txt file and print to it
    analysis_file = os.path.join("Analysis","analysis.txt",)
    with open(analysis_file, "w") as file:   
        file.write("Election Results" + "\n")
        file.write("......................................................." + "\n")
        file.write("total months: " + str(total_months) + "\n")
        file.write("Total: " + "$" + str(sum(Profit)) + "\n")
        file.write("Average change: " + "$" + str(revenue_average) + "\n")
        file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")
        file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")
        
