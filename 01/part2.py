f = open("input.txt", "r")
dictionary = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6",
        "seven": "7", "eight": "8", "nine": "9"}
result = 0
for line in f.readlines():
    line = line.strip()
    for entry in dictionary:
        line = line.replace(entry, entry + dictionary[entry] + entry)
    length = len(line)
    for i in range(length):
        if (line[i]).isnumeric():
            last = line[i]
        if (line[length - i - 1]).isnumeric():
            first = line[length - i - 1]
    result += int(first + last)
print(result)
