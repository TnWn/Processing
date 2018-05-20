import datetime
import math

canvas_size = 1400
#COLOR_LIST =[[233, 217, 229], [129, 176, 178], [168, 193, 200], [151, 166, 117], [234, 155, 103], [255, 220, 127]]
COLOR_LIST = [[315, 27, 88], [193, 23, 72], [356, 19, 71], [172, 63, 78], [192, 82, 33], [40, 4, 86],
            [182, 24, 60], [115, 34, 87], [77, 22, 65], [36, 42, 78], [44, 100, 75], [44, 20, 53],
            [219, 21, 70], [324, 10, 38], [32, 84, 40], [220, 45, 84], [231, 54, 97], [66, 22, 43],
            [144, 19, 38]]
BACKGROUND_COLOR = [17, 3, 45]

def setup():
    size(canvas_size,canvas_size)
    strokeWeight(1)
    strokeJoin(BEVEL)
    colorMode(HSB, 360, 100, 100)
    smooth()
    frameRate(30)
    background(BACKGROUND_COLOR[0], BACKGROUND_COLOR[1], BACKGROUND_COLOR[2])

#Make the points for the circle, then call drawCircle to draw using point_list
#ARGS: iterator - sets the size of the circle, larger iterator = larger circle
def createCircle(iterator):
    point_list = []
    radius = (iterator * iterator * 200)
    for x in range(-canvas_size , canvas_size , 1):
        y = sqrt(radius - x ** 2)
        if not math.isnan(y):
            point_list.append([x,y])
    for x in range(canvas_size , -canvas_size , -1):
        y = -sqrt(radius  - x ** 2)
        if not math.isnan(y):
            point_list.append([x,y])
    for i in range(0, int((iterator/5)) + 5):
        drawCircle(point_list,iterator)

def drawCircle(point_list, iterator):
    random_color = int(random(0,len(COLOR_LIST)))
    stroke(COLOR_LIST[random_color][0], COLOR_LIST[random_color][1], (COLOR_LIST[random_color][2] - 5))
    fill(COLOR_LIST[random_color][0], COLOR_LIST[random_color][1], COLOR_LIST[random_color][2])
    random_max = int(random(1,len(point_list)))
    random_max = random_max / iterator
    stroke_weight = 5
    beginShape()
    for j in range(0, random_max):
        if (j == 0):
            vertex(0,0)
        vertex(point_list[j][0], point_list[j][1])
    endShape(CLOSE)
    rotate(random(0,6.3))

def draw():
    translate(canvas_size/2, canvas_size/2)
    for x in range(40,0,-1):
        createCircle(x)
    noLoop()
    mouseClicked()

def mouseClicked():
    print "END"
    time = datetime.datetime.now().strftime("%d_%m_%H_%M_%S")
    print time
    fileName = "/pics/" + time + ".jpg"
    print fileName
    save(fileName)

    noLoop()
