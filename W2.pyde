
def setup():
    size(500, 500)
x = 100
def draw_balloon(x, y):
    fill(255, 100, 150)
    ellipse(x, y, 100, 100)
    stroke(0)
    line(x, y + 50, x, y + 200)
def draw():
    global x
    background(255)
    draw_balloon(x, 200)
    x += 2
    if x > 550:
        x = -50
