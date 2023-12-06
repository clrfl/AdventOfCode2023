class Seeds:
    def __init__(self, ids):
        self.ids = ids

    def translate(self, translationMap):
        for i in range(len(self.ids)):
            seed = self.ids[i]
            for entry in translationMap:
                trMap = entry.split(" ")
                if int(trMap[1]) <= int(seed) <= int(trMap[1]) + int(trMap[2]):
                    self.ids[i] = int(seed) - int(trMap[1]) + int(trMap[0])
                    break


f = open("input.txt", "r")
file = f.read().split("\n\n")

seeds = file[0].split(" ")[1:]

seed_to_soil = file[1].split("\n")[1:]
soil_to_fertilizer = file[2].split("\n")[1:]
fertilizer_to_water = file[3].split("\n")[1:]
water_to_light = file[4].split("\n")[1:]
light_to_temperature = file[5].split("\n")[1:]
temperature_to_humidity = file[6].split("\n")[1:]
humidity_to_location = file[7].split("\n")[1:]

hello = Seeds(seeds)
hello.translate(seed_to_soil)
hello.translate(soil_to_fertilizer)
hello.translate(fertilizer_to_water)
hello.translate(water_to_light)
hello.translate(light_to_temperature)
hello.translate(temperature_to_humidity)
hello.translate(humidity_to_location)

print(min(hello.ids))
