f = open("input.txt", "r")
dct={}
file = f.read().split("\n\n")

instructions = file[0].strip()
nodes = file[1].split("\n")

for node in nodes:
    if node.strip() == "":
        continue
    node = node.split(" = ")
    idx = node[0]
    targets = node[1].strip()[1:-1].split(", ")
    dct[idx] = targets

pointer = "AAA"
stepcounter = 0
while pointer != "ZZZ":
    for char in instructions:
        stepcounter += 1
        if char == "L":
            pointer = dct[pointer][0]
        elif char == "R":
            pointer = dct[pointer][1]
        if pointer == "ZZZ":
            break

print(stepcounter)