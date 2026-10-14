class Balloon:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def show(self):
        print("Position:", self.x, self.y, "Radius:", self.r)

    def move(self):
        self.y = self.y - 2


class EsBalloon(Balloon):
    def __init__(self, x, y, r):
        super().__init__(x, y, r)
        self.change = 1

    def expand_shrink(self):
        self.r = self.r + self.change

        if self.r >= 60:
            self.change = -1
        elif self.r <= 30:
            self.change = 1

    def move(self):
        super().move()
        self.expand_shrink()


balloons = []
balloons.append(Balloon(100, 900, 50))
balloons.append(EsBalloon(200, 850, 50))

step = 0

while step < 10:
    print("Step", step + 1)
    i = 0

    while i < len(balloons):
        print("Balloon", i + 1)
        balloons[i].move()
        balloons[i].show()
        i = i + 1

    print()
    step = step + 1