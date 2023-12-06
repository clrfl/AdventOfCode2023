import math

f = open("input.txt", "r")
file = f.readlines()

time = file[0].strip().split(":")[1]
dist = file[1].strip().split(":")[1]

while " " in time or " " in dist:
    time = time.replace(" ", "")
    dist = dist.replace(" ", "")

time = int(time)
dist = int(dist)

found = False
iteration = 1
lower_time = 0
upper_time = time

# binary search
while iteration < 100:
    split = time / pow(2, iteration)

    if lower_time * (time - lower_time) > dist:
        lower_time -= split
    else:
        lower_time += split

    if upper_time * (time - upper_time) > dist:
        upper_time += split
    else:
        upper_time -= split

    iteration += 1

upper_time = math.floor(upper_time)
lower_time = math.ceil(lower_time)

print(upper_time - lower_time + 1)