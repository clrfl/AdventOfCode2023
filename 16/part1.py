file = open("input.txt", "r").readlines()

positions = [(0, 0, "l")]
seen_positions = [(0, 0, "l")]
new_positions = []
len_lines = len(file)
len_chars = len(file[0].strip())


def go_right(pos):
    global new_positions, seen_positions
    if pos[1] + 1 < len_chars:
        new_pos = (pos[0], pos[1] + 1, "l")  # from left
        if new_pos not in seen_positions and new_pos not in new_positions:
            new_positions.append(new_pos)
            seen_positions.append(new_pos)


def go_left(pos):
    global new_positions, seen_positions
    if pos[1] - 1 >= 0:
        new_pos = (pos[0], pos[1] - 1, "r")  # from right
        if new_pos not in seen_positions and new_pos not in new_positions:
            new_positions.append(new_pos)
            seen_positions.append(new_pos)


def go_up(pos):
    global new_positions, seen_positions
    if pos[0] - 1 >= 0:
        new_pos = (pos[0] - 1, pos[1], "b")  # from below
        if new_pos not in seen_positions and new_pos not in new_positions:
            new_positions.append(new_pos)
            seen_positions.append(new_pos)


def go_down(pos):
    global new_positions, seen_positions
    if pos[0] + 1 < len_lines:
        new_pos = (pos[0] + 1, pos[1], "a")  # from above
        if new_pos not in seen_positions and new_pos not in new_positions:
            new_positions.append(new_pos)
            seen_positions.append(new_pos)


while len(positions) > 0:
    new_positions = []
    for pos in positions:
        if file[pos[0]][pos[1]] == ".":
            if pos[2] == "l":
                go_right(pos)
            elif pos[2] == "r":
                go_left(pos)
            elif pos[2] == "a":
                go_down(pos)
            elif pos[2] == "b":
                go_up(pos)

        elif file[pos[0]][pos[1]] == "/":
            if pos[2] == "l":
                go_up(pos)
            elif pos[2] == "r":
                go_down(pos)
            elif pos[2] == "a":
                go_left(pos)
            elif pos[2] == "b":
                go_right(pos)

        elif file[pos[0]][pos[1]] == "\\":
            if pos[2] == "l":
                go_down(pos)
            elif pos[2] == "r":
                go_up(pos)
            elif pos[2] == "a":
                go_right(pos)
            elif pos[2] == "b":
                go_left(pos)

        elif file[pos[0]][pos[1]] == "|":
            if pos[2] == "l" or pos[2] == "r":
                go_down(pos)
                go_up(pos)
            elif pos[2] == "a":
                go_down(pos)
            elif pos[2] == "b":
                go_up(pos)

        elif file[pos[0]][pos[1]] == "-":
            if pos[2] == "l":
                go_right(pos)
            elif pos[2] == "r":
                go_left(pos)
            elif pos[2] == "a" or pos[2] == "b":
                go_right(pos)
                go_left(pos)

    positions = new_positions

energized = []
for element in seen_positions:
    if (element[0], element[1]) not in energized:
        energized.append((element[0], element[1]))

print(len(energized))
