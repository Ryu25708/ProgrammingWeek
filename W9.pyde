balloons = []

class Balloon:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def display(self):
        fill(255, 100, 150)
        ellipse(self.x, self.y, self.r, self.r)
        line(self.x, self.y + self.r / 2,
             self.x, self.y + self.r / 2 + 40)


def setup():
    size(1000, 1000)

    x_coords = [100, 200, 400, 500, 600]
    y_coords = [900, 850, 600, 700, 950]

    i = 0
    while i < len(x_coords):
        balloons.append(Balloon(x_coords[i], y_coords[i], 50))
        i = i + 1

    noLoop()


def draw():
    background(255)

    i = 0
    while i < len(balloons):
        balloons[i].display()
        i = i + 1
