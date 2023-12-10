from matplotlib import pyplot as plt
from matplotlib import patches as patches
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

seen = {(line_id, char_id)}

if above:
    pos = (line_id - 1, char_id, "below", 1)
elif below:
    pos = (line_id + 1, char_id, "above", 1)
elif left:
    pos = (line_id, char_id - 1, "right", 1)
elif right:
    pos = (line_id, char_id + 1, "left", 1)

seen.add((pos[0], pos[1]))

while pos[0] != line_id or pos[1] != char_id:
    pos = (walk(pos[0], pos[1], pos[2], pos[3]))
    seen.add((pos[0], pos[1]))

for element in seen:
    if element in right_set:
        right_set.remove(element)
    if element in left_set:
        left_set.remove(element)

print(seen)
print(len(seen) / 2)

fig, ax = plt.subplots(figsize=(16,16), dpi=100)
ax.set_xlim(0, len(file[0]))
ax.set_ylim(0, len(file))
for coords in seen:
    char = file[int(coords[0])][int(coords[1])]
    if char == "-":
        ax.add_patch(patches.Rectangle((float(coords[0]) + 0.2, float(coords[1]) + 0.0), 0.6, 1, linewidth=0, facecolor="b"))
    elif char == "|":
        ax.add_patch(patches.Rectangle((float(coords[0]) + 0.0, float(coords[1]) + 0.2), 1, 0.6, linewidth=0, facecolor="b"))

    elif char == "7":
        ax.add_patch(patches.Rectangle((float(coords[0]) + 0.2, float(coords[1]) + 0.0), 0.6, 0.8, linewidth=0, facecolor="b"))
        ax.add_patch(patches.Rectangle((float(coords[0]) + 0.2, float(coords[1]) + 0.2), 0.8, 0.6, linewidth=0, facecolor="b"))

    elif char == "J":
        ax.add_patch(patches.Rectangle((float(coords[0]) + 0.2, float(coords[1]) + 0.0), 0.6, 0.8, linewidth=0, facecolor="b"))
        ax.add_patch(patches.Rectangle((float(coords[0]) + 0.0, float(coords[1]) + 0.2), 0.8, 0.6, linewidth=0, facecolor="b"))

    elif char == "F":
        ax.add_patch(patches.Rectangle((float(coords[0]) + 0.2, float(coords[1]) + 0.2), 0.6, 0.8, linewidth=0, facecolor="b"))
        ax.add_patch(patches.Rectangle((float(coords[0]) + 0.2, float(coords[1]) + 0.2), 0.8, 0.6, linewidth=0, facecolor="b"))

    elif char == "L":
        ax.add_patch(patches.Rectangle((float(coords[0]) + 0.2, float(coords[1]) + 0.2), 0.6, 0.8, linewidth=0, facecolor="b"))
        ax.add_patch(patches.Rectangle((float(coords[0]) + 0.0, float(coords[1]) + 0.2), 0.8, 0.6, linewidth=0, facecolor="b"))

    elif char == "S":
        ax.add_patch(patches.Rectangle((float(coords[0]) + 0.0, float(coords[1]) + 0.0), 1, 1, linewidth=0, facecolor="green"))


for coords in right_set:
    ax.add_patch(patches.Rectangle((int(coords[0]), int(coords[1])), 1, 1, linewidth=0, facecolor="yellow"))

for coords in left_set:
    ax.add_patch(patches.Rectangle((int(coords[0]), int(coords[1])), 1, 1, linewidth=0, facecolor="red"))

plt.show()