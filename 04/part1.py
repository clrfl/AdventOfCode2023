f = open("input.txt", "r")
file = f.readlines()
sum = 0

for line in file:
    line = line.strip().split(":")
    header = line[0].strip()
    line = line[1].strip().replace("  "," ").split("|")
    winner = line[0].strip().split(" ")
    line = line[1].strip().split(" ")

    wins = 0
    for element in line:
        if element in winner:
            wins += 1

    if wins == 0:
        continue
    points = 1
    for i in range(wins-1):
        points *= 2
    sum += points

print(sum)

