import numpy as np

f = open("input.txt", "r").read()
maps = f.split("\n\n")


def symm(arr, line_low, line_high_diff=1):
    if line_low == len(arr) - 1:  # line_high out of bounds
        return False

    line_high = line_low + line_high_diff
    if (arr[line_low] == arr[line_high]).all():
        if line_low == 0 or line_high == len(arr) - 1:
            return True
        else:
            return symm(arr, line_low - 1, line_high_diff + 2)
    else:
        return False


def symm2(arr, line_low, line_high_diff=1):
    if line_low == len(arr) - 1:  # line_high out of bounds
        return False

    line_high = line_low + line_high_diff
    amount = sum(arr[line_low] != arr[line_high])
    if amount <= 1:
        if line_low == 0 or line_high == len(arr) - 1:
            return True
        else:
            if amount == 0:
                return symm2(arr, line_low - 1, line_high_diff + 2)
            else:
                return symm2(arr, line_low - 1, line_high_diff + 2)
    else:
        return False


summe = 0

def findsym(m):
    m = m.strip().split("\n")
    for i, el in enumerate(m):
        m[i] = [x for x in el]
    m = np.array(m)

    sym = False
    for line in range(len(m)):
        sym = True if symm(m, line) else sym
        if sym:
            return line, True # horizontal = True
    if not sym:
        m = np.transpose(m)
        for line in range(len(m)):
            sym = True if symm(m, line) else sym
            if sym:
                return line, False


for m in maps:
    forbidden_line_id, horizontal = findsym(m)

    m = m.strip().split("\n")
    for i, el in enumerate(m):
        m[i] = [x for x in el]
    m = np.array(m)

    sym = False
    for line in range(len(m)):
        if horizontal and line == forbidden_line_id:
            continue
        sym = True if symm2(m, line) else sym
        if sym:
            summe += 100 * (line + 1)
            break
    if not sym:
        m = np.transpose(m)
        for line in range(len(m)):
            if (not horizontal) and line == forbidden_line_id:
                continue
            sym = True if symm2(m, line) else sym
            if sym:
                summe += (line + 1)
                break

# Please don't judge, I got frustrated with this type of task, and decided to write functional
# yet ugly code to get it done quickly. At least it worked first try without debugging ¯\_(ツ)_/¯

print(summe)
