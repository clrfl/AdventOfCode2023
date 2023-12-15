f = open("input.txt", "r")
spheres = []
squares = []
add_one = lambda a: a + 1
do_nothing = lambda a: a
sub_one = lambda a: a - 1

for idx, line in enumerate(f.readlines()):
    for col, char in enumerate(line.strip()):
        if char == "O":
            spheres.append((idx, col))
        elif char == "#":
            squares.append((idx, col))

len_f = idx + 1
len_c = col + 1


def tilt(spheres_to_tilt, line_op, col_op):
    tilted_spheres = []
    for sphere in spheres_to_tilt:
        line_id = sphere[0]
        col_id = sphere[1]

        while (line_op(line_id), col_op(col_id)) not in squares and (
                line_op(line_id), col_op(col_id)) not in tilted_spheres:
            if line_op(line_id) < 0 or col_op(col_id) < 0 or line_op(line_id) >= len_f or col_op(col_id) >= len_c:
                break
            line_id = line_op(line_id)
            col_id = col_op(col_id)
        tilted_spheres.append((line_id, col_id))
    return tilted_spheres


def tilt_cycle(spheres_input):
    spheres_north = tilt(spheres_input, sub_one, do_nothing)
    spheres_north.sort()
    spheres_west = tilt(spheres_north, do_nothing, sub_one)
    spheres_west.sort(reverse=True)
    spheres_south = tilt(spheres_west, add_one, do_nothing)
    spheres_south.sort(reverse=True)
    spheres_east = tilt(spheres_south, do_nothing, add_one)
    spheres_east.sort()
    return spheres_east


def find_match(spheres):
    old_spheres = []
    i = 1
    dct = {}
    while spheres != old_spheres:
        old_spheres = spheres
        spheres = tilt_cycle(spheres)
        dct[i] = spheres
        for j in range(1, i):
            if i != j and dct[i] == dct[j]:
                print(i, j)
                return i, j, dct
        i += 1


i, j, dct = find_match(spheres)
target_iteration = 1000000000 % (i - j)
while target_iteration <= j:
    target_iteration += (i - j)

spheres = dct[target_iteration]

summe = 0
for sphere in spheres:
    summe += (len_f - sphere[0])
print(summe)
# terminates in 163 seconds, but with the right solution
