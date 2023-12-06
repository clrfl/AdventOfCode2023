from typing import List


class Idpair:
    def __init__(self, start, length):
        self.start = int(start)
        self.length = int(length)

    def translate(self, translation_map):
        for entry in translation_map:
            tr_map = entry.split(" ")
            if len(tr_map) != 3:
                continue

            tr_start = int(tr_map[1])
            tr_end = tr_start + int(tr_map[2])

            translate = int(tr_map[0]) - tr_start

            # if Idpair starts in range
            if self.length > 0:
                if tr_start <= self.start < tr_end:
                    # if Idpair fully lies within range
                    if (self.start + self.length) <= tr_end:
                        self.start = self.start + translate
                        break

                    # Idpair only starts in range
                    else:
                        old_length = self.length
                        self.length = tr_end - self.start
                        self.start = self.start + translate
                        return [Idpair(tr_end, old_length - self.length)]

                # only end lies within range
                elif tr_start < self.start + self.length <= tr_end:
                    old_start = self.start
                    old_length = self.length
                    self.length = self.start + self.length - tr_start
                    self.start = tr_start + translate
                    return [Idpair(old_start, old_length - self.length)]

                # range covered
                elif self.start <= tr_start < tr_end <= self.start + self.length:
                    prefix_range = Idpair(self.start, tr_start - self.start)
                    suffix_range = Idpair(tr_end, self.start + self.length - tr_end)
                    self.length = tr_end - tr_start
                    self.start = tr_start + translate
                    return [prefix_range, suffix_range]
        return None


class IdPairList:
    def __init__(self, ids: List[Idpair]):
        self.ids = ids

    def translate(self, translation_map):
        for element in self.ids:
            result = element.translate(translation_map)
            if result != None:
                for res in result:
                    self.ids.append(res)


hello = IdPairList([])
f = open("input.txt", "r")
file = f.read().split("\n\n")
seeds = file[0].split(" ")[1:]

i = 0
while i < len(seeds):
    seedpair = Idpair(seeds[i], seeds[i + 1])
    hello.ids.append(seedpair)
    i += 2

seed_to_soil = file[1].split("\n")[1:]
soil_to_fertilizer = file[2].split("\n")[1:]
fertilizer_to_water = file[3].split("\n")[1:]
water_to_light = file[4].split("\n")[1:]
light_to_temperature = file[5].split("\n")[1:]
temperature_to_humidity = file[6].split("\n")[1:]
humidity_to_location = file[7].split("\n")[1:]

hello.translate(seed_to_soil)
hello.translate(soil_to_fertilizer)
hello.translate(fertilizer_to_water)
hello.translate(water_to_light)
hello.translate(light_to_temperature)
hello.translate(temperature_to_humidity)
hello.translate(humidity_to_location)

mini = float("inf")
for element in hello.ids:
    mini = min(element.start, mini)
print(mini)
