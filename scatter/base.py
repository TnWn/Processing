circle_size = 50


class Clock(object):
    def __init__(self, x, y):  # Object constructor
        self.x = x
        self.y = y
    def display(self):  # Display method
        noStroke()
        colorMode(HSB, 360, 100, 100);
        fill(80 + random(-10, 10), 60, 50);
        ellipse(self.x, self.y, circle_size, circle_size)
        line(30, 20, 85, 75)

def setup():
    size(800,800)

def draw():
    for x in range(circle_size,800,67):
        for y in range(circle_size,800,12):
            new_clock = Clock(x,y)
            new_clock.display()
    noLoop()
