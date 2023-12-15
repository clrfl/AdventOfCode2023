f = open("input.txt", "r").read().strip().split(",")


def hash_algo(string):
    val = 0
    for char in string:
        val = ((val + ord(char)) * 17) % 256
    return val


summe = 0
dct = {}

for entry in f:
    if "-" in entry:
        entry = entry[:-1]
        box = dct.get(hash_algo(entry), [])
        for lens in box:
            if lens[0] == entry:
                box.remove(lens)
                dct[hash_algo(entry)] = box
                break

    elif "=" in entry:
        entry = entry.split("=")
        focallength = entry[1]
        entry = entry[0]
        box = dct.get(hash_algo(entry), [])

        for i in range(len(box) + 1):

            if i == len(box):
                box.append((entry, focallength))
            else:
                lens = box[i]
                if lens[0] == entry:
                    box[i] = (entry, focallength)
                    break
        dct[hash_algo(entry)] = box

summe = 0
for box_id in dct:
    box = dct[box_id]
    for idx, entry in enumerate(box):
        summe += (box_id + 1) * (idx + 1) * int(entry[1])

print(summe)
