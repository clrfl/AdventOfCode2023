f = open("input.txt", "r")
file = f.readlines()


def walk(line_id, char_id, coming_from, steps):
    char = file[line_id][char_id]
    if char == "L":
        if coming_from == "top":
            return line_id, char_id + 1, "left", steps + 1
        else:
            return line_id - 1, char_id, "bottom", steps + 1

    elif char == "F":
        if coming_from == "bottom":
            return line_id, char_id + 1, "left", steps + 1
        else:
            return line_id + 1, char_id, "top", steps + 1

    elif char == "J":
        if coming_from == "top":
            return line_id, char_id - 1, "right", steps + 1
        else:
            return line_id - 1, char_id, "bottom", steps + 1

    elif char == "7":
        if coming_from == "left":
            return line_id + 1, char_id, "top", steps + 1
        else:
            return line_id, char_id - 1, "right", steps + 1

    elif char == "-":
        if coming_from == "left":
            return line_id, char_id + 1, "left", steps + 1
        else:
            return line_id, char_id - 1, "right", steps + 1

    elif char == "|":
        if coming_from == "top":
            return line_id + 1, char_id, "top", steps + 1
        else:
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

if above: pos.append((line_id - 1, char_id, "below", 1))
if below: pos.append((line_id + 1, char_id, "above", 1))
if left: pos.append((line_id, char_id - 1, "right", 1))
if right: pos.append((line_id, char_id + 1, "left", 1))

while pos[0][0] != pos[1][0] or pos[0][1] != pos[1][1]:
    pos = (walk(pos[0][0], pos[0][1], pos[0][2], pos[0][3]),
           walk(pos[1][0], pos[1][1], pos[1][2], pos[1][3]))

print(pos[0][3])


