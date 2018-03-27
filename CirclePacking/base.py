#java -jar processing-py.jar mouse_follow.py

class Circle(object):
    def __init__(self, x, y, r):  # Object constructor
        self.x = x
        self.y = y
        self.r = r
    def display(self):  # Display method
        noStroke()
        colorMode(HSB, 360, 100, 100);
        fill(280 + random(-10, 10), 100, 100);
        ellipse(self.x, self.y, 2*self.r, 2*self.r)
    def collides(self, c):
        if (dist(self.x, self.y, c.x, c.y,) < (self.r + c.r + MARGIN)):
            return True
        return False

def setup():
    size(500,500)
    background(255)
    current_radius = RADIUS_MAX

def isValidCircle(new_circle):
    if (dist(new_circle.x, new_circle.y, width/2, height/2) > 200):
        return False
    for c in circles:
        if(new_circle.collides(c)):
            return False
    return True

failed_tries = 0
circles = []
MARGIN = 10         #user specified margin between the circles
RADIUS_MAX = 16
RADIUS_MIN = 2
current_radius = 16

def draw():
    global failed_tries
    global current_radius
    print "FAILED TRIES:"
    print failed_tries
    print "~~~~~~~~~~~~~~~~~~~~~~~"
    print "CURRENT RADIUS"
    print current_radius
    print "------------------------"
    new_circle = Circle(random(width),random(height), current_radius)
    if (isValidCircle(new_circle)):
        new_circle.display()
        circles.append(new_circle)
    else:
        failed_tries += 1
        if (failed_tries > 32 * 1024 / current_radius):
            current_radius /= 2
            if (current_radius < RADIUS_MIN):
                print "DONE"
                noLoop()
