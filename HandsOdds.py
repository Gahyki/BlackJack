import csv
import numpy as np
import matplotlib.pyplot as plt

file = open("blkjckhands.csv", "r")
reader = csv.reader(file)
next(reader)
hand = []

for column in reader:
    hand.append(int(column[2]) + int(column[3]) + int(column[4]) + int(column[5]))

# set() -> get all unique values of array
unique = sorted(set(hand))
freq = []

for element in unique:
    freq.append(hand.count(element))

print(unique)
print(freq)

for i in range(len(unique)):
    print(str(unique[i]) + ": " + str((freq[i]/900000)*100) + "%")

y_pos = np.arange(len(unique))
plt.bar(y_pos, freq, align='center', alpha=0.5)
plt.xticks(y_pos, unique)
plt.ylabel('Frequency'.upper())
plt.title('Odds of each hand in blackjack'.upper())

plt.show()

