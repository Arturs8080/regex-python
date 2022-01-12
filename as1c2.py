import re  # imports the regular expression library
hand = open('')
numlist = list()  # create a list

for line in hand:
    line = line.rstrip()
    # regex that reads all integers in each line
    integers = re.findall('[0-9]+', line)
    # [0-9] means select any digits between 0 and 9
    # the + means one or more
    # findall will read multiple sets of numbers in same line.
    for number in integers:
        # append() method in python adds a single item to the existing list
        numlist.append(int(number))
print(sum(numlist))  # aggregates the numbers found in the list
