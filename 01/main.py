f = open("input.txt", "r")
result = 0
for line in f.readlines():
    line = line.strip()
    length = len(line)
    for i in range(length):
        if (line[i]).isnumeric():
            last = line[i]
        if (line[length - i - 1]).isnumeric():
            first = line[length - i - 1]
    result += int(first + last)
print(result)
