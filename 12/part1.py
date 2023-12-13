f = open("input.txt")
summe = 0


def matches(text, numbers):
    states = "."
    for nr in numbers:
        for i in range(int(nr)):
            states += "#"
        states += "."

    states_dict = {0: 1}
    new_dict = {}
    for char in text:
        for state in states_dict:
            if char == "?":
                if state + 1 < len(states):
                    new_dict[state + 1] = new_dict.get(state + 1, 0) + states_dict[state]
                if states[state] == ".":
                    new_dict[state] = new_dict.get(state, 0) + states_dict[state]

            elif char == ".":
                if state + 1 < len(states) and states[state + 1] == ".":
                    new_dict[state + 1] = new_dict.get(state + 1, 0) + states_dict[state]
                if states[state] == ".":
                    new_dict[state] = new_dict.get(state, 0) + states_dict[state]

            elif char == "#":
                if state + 1 < len(states) and states[state + 1] == "#":
                    new_dict[state + 1] = new_dict.get(state + 1, 0) + states_dict[state]

        states_dict = new_dict
        new_dict = {}

    return states_dict.get(len(states) - 1, 0) + states_dict.get(len(states) - 2, 0)


for idx, line in enumerate(f.readlines()):
    line = line.strip().split(" ")
    text = line[0]
    numbers = line[1].split(",")

    summe += matches(text, numbers)

print(summe)
