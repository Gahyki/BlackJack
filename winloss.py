import csv

f = open('blkjckhands.csv')
csv_f = csv.reader(f)
wincount = 0;

for row in csv_f:
    rowstring = ''.join(row[15])
    if rowstring == "Win":
        wincount = wincount + 1;
        print(wincount)

print("Total Wins: ", wincount)
print("Total Win Rate: ", wincount/900000)