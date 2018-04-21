import datetime
import math

canvas_size = 1150
#grid_colors = [[3, 13, 41], [129, 180, 213], [7, 48, 105], [181, 0, 3], [155, 155, 155], [63, 71, 79], [72, 1, 8]]
grid_colors = [[218, 84, 70], [118, 153, 133], [115, 146, 153], [122, 107, 88]]


def setup():
    size(canvas_size,canvas_size)
    strokeWeight(5)
    noFill()
    smooth()
    frameRate(30)
    #background(182, 215, 213)
    background(219, 214, 201)

def createCircle(iterator):
    point_list = []
    radius = 400 + (iterator * iterator * 900)
    for x in range(-canvas_size , canvas_size ,5):
        y = sqrt(radius - x ** 2)
        if not math.isnan(y):
            random_x = random(-2,2)
            random_y = random(-2,2)
            x += random_x
            y += random_y
            point_list.append([x,y])


    for x in range(canvas_size , -canvas_size ,-5):
        y = -sqrt(radius  - x ** 2)
        if not math.isnan(y):
            random_x = random(-2,2)
            random_y = random(-2,2)
            x += random_x
            y += random_y
            point_list.append([x,y])

    limit = 0
    for x in range(-canvas_size , canvas_size ,5):
        y = sqrt(radius - x ** 2)
        if not math.isnan(y):
            limit += 1
            random_x = random(10,20)
            random_y = random(10,20)
            x += random_x
            y += random_y
            point_list.append([x,y])
        if (limit == 5):
            break

    rotate(random(0,6.3))
    drawCircle(point_list,iterator)


def drawCircle(point_list, iterator):
    random_color = int(random(0,len(grid_colors)))
    stroke(grid_colors[random_color][0], grid_colors[random_color][1], grid_colors[random_color][2])
    for j in range(0,len(point_list)-3):
        curve(point_list[j][0], point_list[j][1],point_list[j+1][0], point_list[j+1][1], point_list[j+2][0], point_list[j+2][1], point_list[j+3][0], point_list[j+3][1])
        save_image(j,iterator)

def draw():
    translate(canvas_size/2, canvas_size/2)
    for x in range(0,20):
        createCircle(x)
    noLoop()


time = datetime.datetime.now().strftime("%d_%m_%H_%M")

file_number = 0

def save_image(x, iterator):
    '''
    iterator *= 1000
    test = iterator + x
    test = str(test).zfill(8)
    '''
    #test = str(file_number).zfill(5)

    fileName = "/pics/" + time + "/" + str(iterator) + "/" + str(x) + ".jpg"
    print fileName
    save(fileName)

    '''
    global file_number
    file_number += 1
    '''
    noLoop()

def mouseClicked():
    print "END"
    time = datetime.datetime.now().strftime("%d_%m_%H_%M")
    print time
    fileName = "/pics/" + time + ".jpg"
    print fileName
    save(fileName)

    noLoop()
