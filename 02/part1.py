f = open("input.txt", "r")
sum = 0

for line in f.readlines():
    possible = True

    line = line.strip()[5:]
    sep = line.find(":")
    id = line[:sep]
    line = line[sep + 2:]

    games = line.split(";")

    for game in games:
        game = game.strip()

        dict = {"blue": 0, "red": 0, "green": 0}

        turns = game.split(",")

        for turn in turns:
            turn = turn.strip()
            turn = turn.split(" ")
            amount = turn[0]
            colorname = turn[1]

            dict[colorname] += int(amount)

        if dict["blue"] > 14 or \
                dict["red"] > 12 or \
                dict["green"] > 13:
            possible = False

    if possible:
        sum += int(id)

print(sum)
