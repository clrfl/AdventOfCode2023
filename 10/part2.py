f = open("input.txt", "r")
file = f.readlines()

left_set = set()
right_set = set()


def walk(line_id, char_id, coming_from, steps):
    char = file[line_id][char_id]
    if char == "L":
        surrounding_chars = {(line_id, char_id - 1),
                             (line_id + 1, char_id - 1),
                             (line_id + 1, char_id)}
        if coming_from == "top":
            for c in surrounding_chars:
                right_set.add(c)
            return line_id, char_id + 1, "left", steps + 1
        else:
            for c in surrounding_chars:
                left_set.add(c)
            return line_id - 1, char_id, "bottom", steps + 1

    elif char == "F":
        surrounding_chars = {(line_id, char_id - 1),
                             (line_id - 1, char_id - 1),
                             (line_id - 1, char_id)}
        if coming_from == "bottom":
            for c in surrounding_chars:
                left_set.add(c)
            return line_id, char_id + 1, "left", steps + 1
        else:
            for c in surrounding_chars:
                right_set.add(c)
            return line_id + 1, char_id, "top", steps + 1

    elif char == "J":
        surrounding_chars = {(line_id, char_id + 1),
                             (line_id + 1, char_id + 1),
                             (line_id + 1, char_id)}
        if coming_from == "top":
            for c in surrounding_chars:
                left_set.add(c)
            return line_id, char_id - 1, "right", steps + 1
        else:
            for c in surrounding_chars:
                right_set.add(c)
            return line_id - 1, char_id, "bottom", steps + 1

    elif char == "7":
        surrounding_chars = {(line_id, char_id + 1),
                             (line_id - 1, char_id + 1),
                             (line_id - 1, char_id)}
        if coming_from == "left":
            for c in surrounding_chars:
                left_set.add(c)
            return line_id + 1, char_id, "top", steps + 1
        else:
            for c in surrounding_chars:
                right_set.add(c)
            return line_id, char_id - 1, "right", steps + 1

    elif char == "-":
        if coming_from == "left":
            left_set.add((line_id - 1, char_id))
            right_set.add((line_id + 1, char_id))
            return line_id, char_id + 1, "left", steps + 1
        else:
            left_set.add((line_id + 1, char_id))
            right_set.add((line_id - 1, char_id))
            return line_id, char_id - 1, "right", steps + 1

    elif char == "|":
        if coming_from == "top":
            left_set.add((line_id, char_id + 1))
            right_set.add((line_id, char_id - 1))
            return line_id + 1, char_id, "top", steps + 1
        else:
            left_set.add((line_id, char_id - 1))
            right_set.add((line_id, char_id + 1))
            return line_id - 1, char_id, "bottom", steps + 1


def find_s():
    for i in range(len(file)):
        line = file[i]
        if "S" in line:
            return i, line.find("S")


pos = []
line_id, char_id = find_s()

above = True if file[line_id - 1][char_id] in ["|", "7", "F"] else False
below = True if file[line_id + 1][char_id] in ["|", "J", "L"] else False
left = True if file[line_id][char_id - 1] in ["-", "L", "F"] else False
right = True if file[line_id][char_id + 1] in ["-", "7", "J"] else False

path = {(line_id, char_id)}

if above:
    pos = (line_id - 1, char_id, "bottom", 1)
elif below:
    pos = (line_id + 1, char_id, "top", 1)
elif left:
    pos = (line_id, char_id - 1, "right", 1)
elif right:
    pos = (line_id, char_id + 1, "left", 1)

path.add((pos[0], pos[1]))

while pos[0] != line_id or pos[1] != char_id:
    pos = (walk(pos[0], pos[1], pos[2], pos[3]))
    path.add((pos[0], pos[1]))

for element in path:
    if element in right_set:
        right_set.remove(element)
    if element in left_set:
        left_set.remove(element)

max_r = 0
max_l = 0
for el in right_set:
    max_r = max(max_r, el[1])
for el in left_set:
    max_l = max(max_l, el[1])

working_set = left_set if max_r > max_l else right_set

inner_nodes = set()
while len(working_set) != 0:
    discovered = set()
    for coords in working_set:

        explore = [(coords[0]+1,coords[1]),
                   (coords[0]-1,coords[1]),
                   (coords[0],coords[1]+1),
                   (coords[0],coords[1]-1)]
        for node in explore:
            if node not in inner_nodes and node not in path:
                discovered.add(node)

        inner_nodes.add(coords)
    working_set = discovered

print(len(inner_nodes))