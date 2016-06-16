import linecache
import sys
__author__ = 'hsenid'

file = open("output.csv", "r")
file2 = open("processed.csv", "w+")

for i in range(1, len(file.readlines()) + 1):
    line = linecache.getline("output.csv", i).split(',')
    total = 0
    maxValue = max(line)
    minValue = min(line)
    for j in range(0, len(line)):
        total += int(line[j])

    s = str(i).rstrip("\n") + "," + str(total).rstrip("\n") + "," + str(maxValue).rstrip("\n") + "," + str(minValue).rstrip("\n")
    file2.writelines(s + "\n")

file.close();
file2.close();