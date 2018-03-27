#java -jar processing-py.jar mouse_follow.py
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
        colorMode(HSB, 360, 100, 100)
        tester = int(random(0,len(COLOR_LIST)))
        fill(COLOR_LIST[tester][0], COLOR_LIST[tester][1], COLOR_LIST[tester][2]);  #set a list of RGB colors as a color library to randomly select from rather than just pastels //SET CANVAS COLOR AS ONE OF THE COLORS
        ellipse(self.x, self.y, 2*self.r, 2*self.r)
    def display_BG(self):  # Display method
        noStroke()
        colorMode(HSB, 360, 100, 100)
        tester = int(random(0,len(COLOR_LIST_BG)))
        fill(COLOR_LIST_BG[tester][0], COLOR_LIST_BG[tester][1], COLOR_LIST_BG[tester][2]);  #set a list of RGB colors as a color library to randomly select from rather than just pastels //SET CANVAS COLOR AS ONE OF THE COLORS
        ellipse(self.x, self.y, 2*self.r, 2*self.r)
    def collides(self, c):
        if (dist(self.x, self.y, c.x, c.y,) < (self.r + c.r + MARGIN)):
            return True
        return False

def setup():
    size(CANVAS_SIZE, CANVAS_SIZE)
    background(255, 255, 245)

    '''
    background(18,34,178)
    for x in range(0,2000):
        new_circle = Circle(random(width),random(height), random(RADIUS_MAX,200))
        new_circle.display_BG()
    '''

    current_radius = RADIUS_MAX

def isValidCircle(new_circle):
    #if (dist(new_circle.x + (current_radius / 2), new_circle.y + (current_radius / 2), width/2, height/2) > 300): #if more than 400 units away from middle of canvas, try again
    testx = new_circle.x + (new_circle.r)
    testy = new_circle.y + (new_circle.r)
    testx1 = new_circle.x - (new_circle.r)
    testy1 = new_circle.y - (new_circle.r)
    #if ((testx1 < SQUARE_MARGIN) or (testx > CANVAS_SIZE - SQUARE_MARGIN) or (testy1 < SQUARE_MARGIN) or (testy > CANVAS_SIZE - SQUARE_MARGIN)):
    #if ((dist(new_circle.x, new_circle.y, 1000, 1000) > 925)):
    #if ((testx1 < 200) or ((testx > 950) and (testx1 < 1050)) or (testx > 1800)):
    #if ( ((testx1 < 50) or (testy1 < 50)) or ((testx > 950) and (testx1 < 1050)) or ((testx > 1850) or (testy > 1850)) ):
    if (((testx1 < 50) or (testy1 < 50)) or ((testx > 500) and (testx1 < 550))  or ((testx > 1000) and (testx1 < 1050)) or ((testx > 1500) and (testx1 < 1550)) or ((testx > 2000) or (testy > 2000))):
        return False
    if ((dist(testx, testy, random(800,1200), random(800,1200)) > 700) and
    (dist(testx, testy, random(600,1400), random(600,1400)) > 600) and
    (dist(testx, testy, random(600,1400), random(600,1400)) > 500) and
    (dist(testx, testy, random(400,1600), random(400,1600)) > 300) and
    (dist(testx, testy, random(300,1700), random(300,1700)) > 200) and
    (dist(testx, testy, random(200,1800), random(200,1800)) > 100)):
        return False
    for c in circles:
        if(new_circle.collides(c)):
            return False
    return True

failed_tries = 0
circles = []
MARGIN = 10         #user specified margin between the circles
SQUARE_MARGIN = 100
CANVAS_SIZE = 2000
RADIUS_MAX = 150
RADIUS_MIN = 2
current_radius = RADIUS_MAX
COLOR_LIST = [[225,90,80], [225,60,60], [194,100,100], [21,75,100], [12,90,80], [60,4,100]]
#COLOR_LIST = [[59,75,100], [53,75,91], [47,70,100], [41,75,91], [35,75,100]]    #[234,90,70]
COLOR_LIST_BG = [[255,99,75], [250,99,79], [218,99,79], [207,100,79], [191,100,75]]

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
