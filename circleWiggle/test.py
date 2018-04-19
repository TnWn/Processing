import datetime
import math

canvas_size = 1000
grid_colors = [[225,90,80], [225,60,60], [194,100,100], [21,75,100], [12,90,80], [60,4,100]]

def setup():
    size(canvas_size,canvas_size)
    strokeWeight(5)
    noFill()
    smooth()
    frameRate(30)
    background(20,20,20)

def createCircle(iterator):
    point_list = []
    #make circles have more even spacing
    radius = 1000 + ((iterator * 30000) / 2)
    for x in range(-canvas_size, canvas_size,5):
        y = sqrt(radius - x ** 2)
        if not math.isnan(y):
            random_x = random(-2,2)
            random_y = random(-2,2)
            x += random_x
            y += random_y
            point_list.append([x,y])

    for x in range(canvas_size, -canvas_size,-5):
        y = -sqrt(radius  - x ** 2)
        if not math.isnan(y):
            random_x = random(-2,2)
            random_y = random(-2,2)
            x += random_x
            y += random_y
            point_list.append([x,y])

    limit = 0
    for x in range(-canvas_size, canvas_size,5):
        y = sqrt(radius - x ** 2)
        if not math.isnan(y):
            limit += 1
            random_x = random(10,20)
            random_y = random(10,20)
            x += random_x
            y += random_y
            point_list.append([x,y])
        if (limit == 10):
            break

    print point_list
    rotate(random(0,6.3))
    drawCircle(point_list)


def drawCircle(point_list):
    random_color = int(random(0,len(grid_colors)))
    stroke(grid_colors[random_color][0], grid_colors[random_color][1], grid_colors[random_color][2])
    for j in range(0,len(point_list)-3):
        curve(point_list[j][0], point_list[j][1],point_list[j+1][0], point_list[j+1][1], point_list[j+2][0], point_list[j+2][1], point_list[j+3][0], point_list[j+3][1])

def draw():
    translate(canvas_size/2, canvas_size/2)
    for x in range(0,20):
        createCircle(x)
    noLoop()

def mouseClicked():
    print "END"
    time = datetime.datetime.now().strftime("%d_%m_%H_%M")
    print time
    fileName = "/pics/" + time + ".jpg"
    print fileName
    save(fileName)
    noLoop()
