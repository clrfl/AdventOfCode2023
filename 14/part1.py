f = open("input.txt", "r")
spheres = []
squares = []
north_spheres = []

for idx,line in enumerate(f.readlines()):
    for col,char in enumerate(line.strip()):
        if char == "O":
            spheres.append((idx,col))
        elif char == "#":
            squares.append((idx,col))

len_f = idx + 1

for sphere in spheres:
    line_id = sphere[0]
    col_id = sphere[1]
    while (line_id-1, col_id) not in squares and (line_id-1, col_id) not in north_spheres:
        if line_id-1 < 0:
            break
        line_id -= 1
    north_spheres.append((line_id,col_id))

summe = 0
for sphere in north_spheres:
    summe += (len_f - sphere[0])

print(summe)