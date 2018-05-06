import datetime
import math

canvas_size = 5000
#COLOR_LIST = [[179, 68, 11], [177, 47, 71], [147, 56, 108], [101, 70, 123], [59, 75, 113], [47, 72, 88]]
COLOR_LIST = [[76, 0, 207], [196, 142, 0], [191, 28, 0], [1, 197, 201], [67, 199, 0], [0, 66, 207], [183, 196, 0], [0, 199, 126], [207, 0, 143]]
BACKGROUND_COLOR = [20,20,20]


def setup():
    size(canvas_size,canvas_size)
    strokeWeight(5)
    strokeJoin(BEVEL)
    noFill()
    smooth()
    frameRate(30)
    background(BACKGROUND_COLOR[0], BACKGROUND_COLOR[1], BACKGROUND_COLOR[2])

def createCircle(iterator):
    point_list = []
    radius = 400 + (iterator * iterator * 200)
    for x in range(-canvas_size , canvas_size ,5):
        y = sqrt(radius - x ** 2)
        if not math.isnan(y):
            point_list.append([x,y])


    for x in range(canvas_size , -canvas_size ,-5):
        y = -sqrt(radius  - x ** 2)
        if not math.isnan(y):
            point_list.append([x,y])

    drawCircle(point_list,iterator)

def drawCircle(point_list, iterator):
    random_color = int(random(0,len(COLOR_LIST)))
    stroke(COLOR_LIST[random_color][0], COLOR_LIST[random_color][1], COLOR_LIST[random_color][2])
    random_min = int(random(len(point_list)/50, len(point_list)/3))
    random_max = int(random(len(point_list)/2, len(point_list)/3))
    stroke_weight = int(random(10,20))

    for j in range(random_min, random_max):
        '''
        #50% chance of line from origin to curve
        if ((j == random_min) and (random(0,10) >= 5)):
            strokeWeight(int(random(1,5)))

            line(point_list[j][0], point_list[j][1],point_list[j+1][0], point_list[j+1][1])
            line(0,0,point_list[j][0], point_list[j][1])
        #50% chance of line from origin to curve
        if ((j == random_max-1) and (random(0,10) >= 5)):
            strokeWeight(int(random(1,5)))

            line(point_list[j+1][0], point_list[j+1][1],point_list[j+2][0], point_list[j+2][1],)
            line(0,0,point_list[j+2][0], point_list[j+2][1])
        '''

        #strokeWeight(int(random(5,15)))
        stroke_weight += int(random(0,4))
        strokeWeight(stroke_weight)
        curve(point_list[j][0], point_list[j][1],point_list[j+1][0], point_list[j+1][1], point_list[j+2][0], point_list[j+2][1], point_list[j+3][0], point_list[j+3][1])
        #save_image(j,iterator)
    rotate(random(0,6.3))


def clearCenter():
    fill(BACKGROUND_COLOR[0], BACKGROUND_COLOR[1], BACKGROUND_COLOR[2])
    noStroke()
    ellipse(0,0,30,30)

def draw():
    translate(canvas_size/2, canvas_size/2)
    for x in range(0,150):
        createCircle(x)
    clearCenter()
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
