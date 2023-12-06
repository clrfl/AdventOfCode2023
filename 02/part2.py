f = open("input.txt", "r")
sum = 0

for line in f.readlines():

    dict = {"blue": 0, "red": 0, "green": 0}

    line = line.strip()[5:]
    sep = line.find(":")
    line = line[sep+2:]

    games = line.split(";")

    for game in games:
        game = game.strip()

        turns = game.split(",")

        for turn in turns:

            turn = turn.strip()
            turn = turn.split(" ")
            amount = int(turn[0])
            colorname = turn[1]

            dict[colorname] = max(dict[colorname], amount)

    sum += dict["blue"] * dict["red"] * dict["green"]

print(sum)