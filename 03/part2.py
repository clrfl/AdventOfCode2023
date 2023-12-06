f = open("input.txt", "r")
file = f.readlines()

sum = 0

filesize = len(file)


def greedy_number(line, start):
    end = start
    while end < len(line) and line[end].isnumeric():
        end += 1
    while start >= 0 and line[start].isnumeric():
        start -= 1

    return int(line[start + 1:end])


def fetch_numbers(lineID, gear_char, explore):
    numbers = []
    # Line 0
    if "00" in explore and "01" in explore and "02" in explore:  # 000
        numbers.append(greedy_number(file[lineID - 1], gear_char))
    elif "00" in explore and "01" not in explore and "02" in explore:  # 0_0
        numbers.append(greedy_number(file[lineID - 1], gear_char - 1))
        numbers.append(greedy_number(file[lineID - 1], gear_char + 1))
    elif "00" in explore:
        numbers.append(greedy_number(file[lineID - 1], gear_char - 1))
    elif "01" in explore:
        numbers.append(greedy_number(file[lineID - 1], gear_char))
    elif "02" in explore:
        numbers.append(greedy_number(file[lineID - 1], gear_char + 1))

    # Line 1
    if "10" in explore:
        numbers.append(greedy_number(file[lineID], gear_char - 1))
    if "12" in explore:
        numbers.append(greedy_number(file[lineID], gear_char + 1))

    # Line 2
    if "20" in explore and "21" in explore and "22" in explore:  # 000
        numbers.append(greedy_number(file[lineID + 1], gear_char))
    elif "20" in explore and "21" not in explore and "22" in explore:  # 0_0
        numbers.append(greedy_number(file[lineID + 1], gear_char - 1))
        numbers.append(greedy_number(file[lineID + 1], gear_char + 1))
    elif "20" in explore:
        numbers.append(greedy_number(file[lineID + 1], gear_char - 1))
    elif "21" in explore:
        numbers.append(greedy_number(file[lineID + 1], gear_char))
    elif "22" in explore:
        numbers.append(greedy_number(file[lineID + 1], gear_char + 1))

    return numbers


def count_distinct_numbers(explore):
    sum = 0

    # Line 0
    if "00" in explore and "01" in explore and "02" in explore:  # 000
        sum += 1
    elif "00" in explore and "01" not in explore and "02" in explore:  # 0_0
        sum += 2
    elif "00" in explore or "01" in explore or "02" in explore:
        sum += 1

    # Line 1
    if "10" in explore:
        sum += 1
    if "12" in explore:
        sum += 1

    # Line 2
    if "20" in explore and "21" in explore and "22" in explore:  # 000
        sum += 1
    elif "20" in explore and "21" not in explore and "22" in explore:  # 0_0
        sum += 2
    elif "20" in explore or "21" in explore or "22" in explore:
        sum += 1

    return sum


def gear_explore(lineID, gear_char):
    line = file[lineID]
    lineLen = len(line)
    explore_coordinates = []
    # 00 01 02
    # 10 *  12
    # 20 21 22

    if lineID > 0:
        if gear_char > 0:
            if file[lineID - 1][gear_char - 1].isnumeric():
                explore_coordinates.append("00")
        if gear_char < lineLen:
            if file[lineID - 1][gear_char + 1].isnumeric():
                explore_coordinates.append("02")
    if lineID < len(file):
        if gear_char > 0:
            if file[lineID + 1][gear_char - 1].isnumeric():
                explore_coordinates.append("20")
        if gear_char < lineLen:
            if file[lineID + 1][gear_char + 1].isnumeric():
                explore_coordinates.append("22")
    if gear_char > 0:
        if file[lineID][gear_char - 1].isnumeric():
            explore_coordinates.append("10")
    if gear_char < lineLen:
        if file[lineID][gear_char + 1].isnumeric():
            explore_coordinates.append("12")
    if lineID > 0:
        if file[lineID - 1][gear_char].isnumeric():
            explore_coordinates.append("01")
    if lineID < len(file):
        if file[lineID + 1][gear_char].isnumeric():
            explore_coordinates.append("21")

    if not count_distinct_numbers(explore_coordinates) == 2:
        return 0
    numbers = fetch_numbers(lineID, gear_char, explore_coordinates)

    return numbers[0] * numbers[1]


for i in range(len(file)):
    line = file[i]
    j = 0

    for j in range(len(line)):

        if line[j] == "*":
            sum += gear_explore(i, j)

print(sum)
