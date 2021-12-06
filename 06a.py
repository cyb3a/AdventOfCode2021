fish = list(map(int, open('input/06.txt').readline().strip().split(',')))


class FishCounter:
    all_fish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    def __init__(self, fish: list):
        for f in fish:
            self.all_fish[f] += 1

    def new_day(self):
        new_fish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        for k, v in self.all_fish.items():
            if k == 0 and v > 0:
                new_fish[6] += v
                new_fish[8] += v
            elif k > 0:
                new_fish[k - 1] += v
        print(self.all_fish)
        print(new_fish)
        self.all_fish = new_fish


fc = FishCounter(fish)
for d in range(80):
    fc.new_day()

print(sum(fc.all_fish.values()))
