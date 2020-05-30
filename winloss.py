import csv

f = open('blkjckhands.csv')
csv_f = csv.reader(f)
wincount = 0
pushcount = 0

#Loop over each Row
for row in csv_f:
    rowstring = ''.join(row[15])
    #count wins
    if rowstring == "Win":
        wincount = wincount + 1
    #count losses
    if rowstring == "Push":
        pushcount = pushcount + 1

#Print Wins, Losses, and Pushes
print("Total Wins: ", wincount)
print("Total Losses: ", 900000-(wincount+pushcount))
print("Total Pushes: ", pushcount)

#Print Win Rate, Loss Rate, Push Rate
print("Total Win Rate: ", wincount/900000)
print("Total Loss Rate: ", (900000-(wincount+pushcount)) / 900000)
print("Total Push Rate: ", pushcount/900000)
