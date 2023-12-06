f = open("input.txt", "r")
file = f.readlines()

cards = {}
for i in range(0, 213):
    cards[i] = 1

for i in range(len(file)):
    line = file[i]
    line = line.strip().split(":")
    header = line[0].strip()
    line = line[1].strip().replace("  ", " ").split("|")
    winner = line[0].strip().split(" ")
    line = line[1].strip().split(" ")

    wins = 0
    for element in line:
        if element in winner:
            wins += 1

    for j in range(wins):
        if i+j+1<len(file):
            cards[i+j+1] += cards[i]

sum = 0
for i in range(0, 213):
    sum += cards[i]
print(sum)
