f = open("input.txt", "r")
lines = f.readlines()

galaxies = []

double_lines = list(range(len(lines)))
double_columns = list(range(len(lines[0])))

for i in range(len(lines)):
    for j in range(len(lines[i])):
        char = lines[i][j]
        if char == "#":
            galaxies.append((i, j))
            if i in double_lines:
                double_lines.remove(i)
            if j in double_columns:
                double_columns.remove(j)


def dist(galaxy_a, galaxy_b):
    distance = abs(galaxy_a[0] - galaxy_b[0]) + abs(galaxy_a[1] - galaxy_b[1])
    for i in range(min(galaxy_a[0], galaxy_b[0]) + 1, max(galaxy_a[0], galaxy_b[0])):
        if i in double_lines:
            distance += 1E6 - 1
    for j in range(min(galaxy_a[1], galaxy_b[1]) + 1, max(galaxy_a[1], galaxy_b[1])):
        if j in double_columns:
            distance += 1E6 - 1
    return distance


total_distance = 0

for start in range(len(galaxies)):
    for target in range(start + 1, len(galaxies)):
        total_distance += dist(galaxies[start], galaxies[target])

print(int(total_distance))
