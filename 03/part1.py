f = open("input.txt", "r")
file = f.readlines()

sum = 0


def test_validity(lineID, charstart, length):
    tested_chars = []
    valid = False
    for i in range(lineID - 1, lineID + 2):
        for j in range(charstart - 1, charstart + length + 1):
            try:
                tested_chars.append(file[i][j])
            except:
                pass
    for char in tested_chars:
        if not char.isnumeric() and char != "." and char != "\n":
            valid = True
    return valid


def get_length(lineId, charstart):
    line = file[lineId][charstart:]
    length = 0
    while line[0].isnumeric():
        line = line[1:]
        length += 1
    return length


for i in range(len(file)):
    line = file[i]
    j = 0

    while j < len(line):
        if line[j].isnumeric():
            leng = get_length(i, j)

            if test_validity(i, j, leng):
                sum += int(line[j:j + leng])

            while line[j].isnumeric():
                j += 1
        else:
            j += 1

print(sum)
