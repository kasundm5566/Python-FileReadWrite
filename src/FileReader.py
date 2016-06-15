import linecache

__author__ = 'hsenid'

file = open("output.csv", "r")
file2 = open("processed.csv", "w")

for i in range(1, len(file.readlines()) + 1):
    line = linecache.getline("output.csv", i).split(',')
    total = 0
    maxValue = 0;
    minValue = 0;
    maxValue = max(line)
    minValue = min(line)
    for j in range(0, len(line)):
        total += int(line[j])

    file2.write(str(total) + " " + str(minValue) + " " + str(maxValue)+"\n")