values_dict = {}
bids_dict = {}

f = open("input.txt", "r")

for line in f.readlines():
    line = line.split(" ")

    bid = line[1].strip()
    line = line[0].strip().replace('A', 'E').replace('K', 'D').replace('Q', 'C') \
        .replace('J', '1').replace('T', 'A')

    bids_dict[line] = bid

    linedct = {}
    for char in line:
        linedct[char] = linedct.get(char, 0) + 1

    if "1" in linedct.keys():
        js = linedct["1"]
        linedct["1"] = 0

        max = list(linedct.keys())[0]
        for val in linedct:
            if linedct[val] > linedct[max]:
                max = val
        linedct[max] = min(linedct[max] + js, 5)

    if 5 in linedct.values():
        values_dict[int("6" + line, 16)] = line
    elif 4 in linedct.values():
        values_dict[int("5" + line, 16)] = line
    elif 3 in linedct.values() and 2 in linedct.values():
        values_dict[int("4" + line, 16)] = line
    elif 3 in linedct.values():
        values_dict[int("3" + line, 16)] = line
    elif len(linedct.values()) == 3:
        values_dict[int("2" + line, 16)] = line
    elif 2 in linedct.values():
        values_dict[int("1" + line, 16)] = line
    else:
        values_dict[int("0" + line, 16)] = line

sorted_values = sorted(values_dict)
summe = 0
for (idx, val) in enumerate(sorted_values):
    summe += (idx + 1) * int(bids_dict[values_dict[val]])

print(summe)
