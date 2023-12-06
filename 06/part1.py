f = open("input.txt", "r")
file = f.readlines()

time = file[0].strip()
dist = file[1].strip()

while "  " in time or "  " in dist:
    time = time.replace("  ", " ")
    dist = dist.replace("  ", " ")

time = time.split(" ")[1:]
dist = dist.split(" ")[1:]

pairs = []
for i in range(len(time)):
    pairs.append((time[i], dist[i]))

results = []
for pair in pairs:
    wins = 0
    for mmps in range(int(pair[0])+1):
        rem_time = int(pair[0]) - mmps
        if mmps * rem_time > int(pair[1]):
            wins += 1
    results.append(wins)

total = 1
for entry in results:
    total *= entry

print(total)