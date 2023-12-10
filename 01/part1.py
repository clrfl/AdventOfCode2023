import string

result = 0
for line in open("input.txt", "r").readlines():
    line = line.strip().strip(string.ascii_lowercase)
    result += int(line[0] + line[-1])
print(result)
