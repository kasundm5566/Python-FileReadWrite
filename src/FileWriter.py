__author__ = 'hsenid'

import random
import sys

try:
    noOfRecords = int(input("Enter no of records: "))
except Exception as e:
    print("Error with the input...")
    sys.exit(e)

try:
    noOfLines = int(input("Enter no of lines: "))
except Exception as e:
    print("Error with the input...")
    sys.exit(e)

file = open("output.csv", "w")

for i in range(0, noOfLines, 1):
    for j in range(0, noOfRecords, 1):
        if (j == noOfRecords - 1):
            # print(random.randint(1, 100), end='')
            file.write(str(random.randint(1, 100)) + '')
        else:
            # print(random.randint(1, 100), end=',')
            file.write(str(random.randint(1, 100)) + ',')
    # print()
    file.write("\n")
file.close()

