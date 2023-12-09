f = open("input.txt", "r")
summe = 0


def analyze(line):
    depth = 0
    depths = {depth: line}
    while True:
        if list(depths[depth]) == [0] * len(depths[depth]):
            break
        depth += 1
        values = []
        for i in range(len(depths[depth - 1]) - 1):
            values.append(int(depths[depth - 1][i + 1]) - int(depths[depth - 1][i]))
        depths[depth] = values
    return depths, depth


def value(line):
    depths, depth = analyze(line)

    val = 0
    while depth != 0:
        depth -= 1
        val = int(depths[depth][-1]) + val

    print(depths)
    print(depth)

    return val


for line in f.readlines():
    summe += value(line.strip().split(" "))

print("--")
print(summe)
