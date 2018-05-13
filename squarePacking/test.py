import datetime

'''
NOTES HERE:
    set a list of RGB colors as a color library to randomly select from rather than just pastels
    SET CANVAS COLOR AS ONE OF THE COLORS
'''

class Circle(object):
    def __init__(self, x, y, r):  # Object constructor
        self.x = x
        self.y = y
        self.r = r
    def display(self):  # Display method
        noStroke()
        #colorMode(HSB, 360, 100, 100)
        #tester = int(random(0,len(COLOR_LIST)))
        #fill(COLOR_LIST[tester][0], COLOR_LIST[tester][1], COLOR_LIST[tester][2])
        fill(COLOR_LIST[1][0], COLOR_LIST[1][1], COLOR_LIST[1][2])
        rect(self.x, self.y, 2*self.r, 2*self.r)
    def collides(self, c):
        if (abs(self.x - c.x) < (self.r + MARGIN)) or (abs(self.y - c.y) < (self.r + MARGIN)):
            return True
        #if (dist(self.x, self.y, c.x, c.y,) < ((self.r * 2)+ c.r + MARGIN)):
        #    return True
        return False

def setup():
    size(CANVAS_SIZE, CANVAS_SIZE)
    background(255, 255, 245)
    current_radius = RADIUS_MAX

def isValidCircle(new_circle):
    testx = new_circle.x + (new_circle.r)
    testy = new_circle.y + (new_circle.r)
    testx1 = new_circle.x - (new_circle.r)
    testy1 = new_circle.y - (new_circle.r)
    if ((testx1 < SQUARE_MARGIN) or (testx > CANVAS_SIZE - SQUARE_MARGIN) or (testy1 < SQUARE_MARGIN) or (testy > CANVAS_SIZE - SQUARE_MARGIN)):
        return False
    for c in circles:
        if(new_circle.collides(c)):
            return False
    return True

failed_tries = 0
circles = []
MARGIN = 0         #user specified margin between the circles
SQUARE_MARGIN = 100
CANVAS_SIZE = 2000
RADIUS_MAX = 300
RADIUS_MIN = 2
current_radius = RADIUS_MAX
COLOR_LIST = [[225,90,80], [225,60,60], [194,100,100], [21,75,100], [12,90,80], [60,4,100]]

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
        if (failed_tries > 32 * 1024 / (current_radius * (current_radius / 2))):
            current_radius /= 2
            if (current_radius < RADIUS_MIN):
                time = datetime.datetime.now().strftime("%d_%m_%H_%M")
                print time
                fileName = "/pics/" + time + ".jpg"
                print fileName
                save(fileName)
                print "DONE"
                noLoop()
