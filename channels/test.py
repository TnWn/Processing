import datetime
import math

canvas_size = 5000
#COLOR_LIST = [[179, 68, 11], [177, 47, 71], [147, 56, 108], [101, 70, 123], [59, 75, 113], [47, 72, 88]]
COLOR_LIST = [[76, 0, 207], [196, 142, 0], [191, 28, 0], [1, 197, 201], [67, 199, 0], [0, 66, 207], [183, 196, 0], [0, 199, 126], [207, 0, 143]]
BACKGROUND_COLOR = [10,10,10]
MAX_POINTS = 100
STROKE = 8

def setup():
    size(canvas_size,canvas_size)
    noFill()
    smooth()
    frameRate(30)
    background(BACKGROUND_COLOR[0], BACKGROUND_COLOR[1], BACKGROUND_COLOR[2])
    colorMode(RGB, 255, 255, 255, 1.0)

    strokeWeight(STROKE)
    strokeJoin(BEVEL)
    strokeCap(ROUND)

def createPoints():
    point_list = []
    for i in range(0,MAX_POINTS):
        randx = int(random(0 - 1000, canvas_size + 1000))
        randy = int(random(0 - 1000, canvas_size + 1000))
        point_list.append([randx,randy])
    for k in range(0,40):
        point_list = average_points(point_list)
        if (k>19) and (k % 2 == 0) :
            print k
            draw_lines(point_list)

def draw_lines(point_list):
    for i in range(0,len(point_list)-3):
        stroke(255, 0, 0, 0.4)
        curve(point_list[i][0], point_list[i][1], point_list[i+1][0], point_list[i+1][1], point_list[i+2][0], point_list[i+2][1], point_list[i+3][0], point_list[i+3][1])
        stroke(0, 255, 0, 0.4)
        curve(point_list[i][0] + STROKE*3, point_list[i][1], point_list[i+1][0]+ STROKE*3, point_list[i+1][1], point_list[i+2][0]+ STROKE*3, point_list[i+2][1], point_list[i+3][0]+ STROKE*3, point_list[i+3][1])
        stroke(0, 0, 255, 0.4)
        curve(point_list[i][0] + STROKE*6, point_list[i][1], point_list[i+1][0]+ STROKE*6, point_list[i+1][1], point_list[i+2][0]+ STROKE*6, point_list[i+2][1], point_list[i+3][0]+ STROKE*6, point_list[i+3][1])
        stroke(255, 255, 255, 0.4)
        curve(point_list[i][0] + STROKE*9, point_list[i][1], point_list[i+1][0]+ STROKE*9, point_list[i+1][1], point_list[i+2][0]+ STROKE*9, point_list[i+2][1], point_list[i+3][0]+ STROKE*9, point_list[i+3][1])
        #connect end with start
        if (i == len(point_list)-4):
            stroke(255, 0, 0, 0.4)
            curve(point_list[i+1][0], point_list[i+1][1], point_list[i+2][0], point_list[i+2][1], point_list[0][0], point_list[0][1], point_list[1][0], point_list[1][1])
            stroke(0, 255, 0, 0.4)
            curve(point_list[i+1][0] + STROKE*3, point_list[i+1][1], point_list[i+2][0]+ STROKE*3, point_list[i+2][1], point_list[0][0]+ STROKE*3, point_list[0][1], point_list[1][0]+ STROKE*3, point_list[1][1])
            stroke(0, 0, 255, 0.4)
            curve(point_list[i+1][0] + STROKE*6, point_list[i+1][1], point_list[i+2][0]+ STROKE*6, point_list[i+2][1], point_list[0][0]+ STROKE*6, point_list[0][1], point_list[1][0]+ STROKE*6, point_list[1][1])
            stroke(255, 255, 255, 0.4)
            curve(point_list[i+1][0] + STROKE*9, point_list[i+1][1], point_list[i+2][0]+ STROKE*9, point_list[i+2][1], point_list[0][0]+ STROKE*9, point_list[0][1], point_list[1][0]+ STROKE*9, point_list[1][1])

def average_points(list):
    new_list = []
    for j in range(0,len(list)-1):
        new_list_x = ((list[j][0] + list[j + 1][0])/2)
        new_list_y = ((list[j][1] + list[j + 1][1])/2)
        new_list.append([new_list_x, new_list_y])
    return new_list

noiseScale = 0.02
def draw():
    for x in range(0, canvas_size, 10):
        for y in range(0, canvas_size, 10):
            noiseVal = noise(x, y)
            fill(noiseVal * 255)
            stroke(noiseVal * 255)
            ellipse(x, y, 10, 10)
    noFill()
    createPoints()
    noLoop()
    mouseClicked()
    background(0)

def mouseClicked():
    print "END"
    time = datetime.datetime.now().strftime("%d_%m_%H_%M_%S")
    print time
    fileName = "/pics/" + time + ".jpg"
    print fileName
    save(fileName)

    noLoop()
