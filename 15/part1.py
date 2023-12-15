f = open("input.txt", "r").read().strip().split(",")


def hash_algo(string):
    val = 0
    for char in string:
        val = ((val + ord(char)) * 17) % 256
    return val


summe = 0
for entry in f:
    summe += hash_algo(entry)
print(summe)
