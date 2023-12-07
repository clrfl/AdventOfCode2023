values_dict = {}
bids_dict = {}

f = open("input.txt", "r")

for line in f.readlines():
    line = line.split(" ")
    bid = line[1].strip()
    line = line[0].strip()
    bids_dict[line] = bid
    replaced = line.replace('A', 'E').replace('K', 'D').replace('Q', 'C') \
        .replace('J', 'B').replace('T', 'A')

    linedct = {}
    for char in line:
        linedct[char] = linedct.get(char, 0) + 1

    if 5 in linedct.values():
        values_dict[int("6" + replaced, 16)] = line
    elif 4 in linedct.values():
        values_dict[int("5" + replaced, 16)] = line
    elif 3 in linedct.values() and 2 in linedct.values():
        values_dict[int("4" + replaced, 16)] = line
    elif 3 in linedct.values():
        values_dict[int("3" + replaced, 16)] = line
    elif len(linedct.values()) == 3:
        values_dict[int("2" + replaced, 16)] = line
    elif 2 in linedct.values():
        values_dict[int("1" + replaced, 16)] = line
    else:
        values_dict[int("0" + replaced, 16)] = line

sorted_values = sorted(values_dict)
summe = 0
for (idx, val) in enumerate(sorted_values):
    summe += (idx + 1) * int(bids_dict[values_dict[val]])
    # print(str(idx+1) + " * " + bids_dict[values_dict[val]] + " w/ card " + values_dict[val] + " and val " + str(val))
print(summe)
