import math

f = open("input.txt", "r")
dct = {}
file = f.read().split("\n\n")

instructions = file[0].strip()
nodes = file[1].split("\n")
#instrlen = len(instructions)
#print(instrlen)

for node in nodes:
    if node.strip() == "":
        continue
    node = node.split(" = ")
    idx = node[0]
    targets = node[1].strip()[1:-1].split(", ")
    dct[idx] = targets

pointers = []
for index in dct:
    if index[2] == "A":
        pointers.append(index)


def explore_node(pointer):
    stepcounter = 0
    endstates = []
    possible_steps = []

    while pointer not in endstates:
        endstates.append(pointer)
        for char in instructions:
            stepcounter += 1
            if char == "L":
                pointer = dct[pointer][0]
            elif char == "R":
                pointer = dct[pointer][1]

            if pointer[2] == "Z":
                possible_steps.append(stepcounter)

    #print(endstates)
    #print(possible_steps)
    #print(stepcounter)

    return [possible_steps, stepcounter]


results = []
for pointer in pointers:
    #print(pointer)
    res = explore_node(pointer)
    # luckily every node only hits ..Z once per iteration, being on the last node. This makes the solution much easier
    results.append(res[0][0]) #, int(res[1] / instrlen) - 1))
    #print(str(int(res[1] / instrlen)) + " instruction iterations until loop")
    #print(" -- ")

print(results)

print(math.lcm(*results))

