import datetime
import math

canvas_size = 1000
half_canvas = canvas_size/2
#grid_colors = [[225,90,80], [225,60,60], [194,100,100], [87,177,219], [12,90,80], [190,108,249], [239,244,201]]
grid_colors = [[245,245,245]]

def setup():
    size(canvas_size,canvas_size)
    strokeWeight(1)
    noFill()
    smooth()
    frameRate(30)
    background(20,20,20)

def createCircle(iterator):
    point_list = []
    #make circles have more even spacing
    radius = 1000 + ((iterator * 30000) / 20)    #/2
    for x in range(-half_canvas, half_canvas,5):
        y = sqrt(radius - x ** 2)
        if not math.isnan(y):
            random_x = random(-2,2)
            random_y = random(-2,2)
            x += random_x
            y += random_y
            point_list.append([x,y])


    for x in range(half_canvas, -half_canvas,-5):
        y = -sqrt(radius  - x ** 2)
        if not math.isnan(y):
            random_x = random(-2,2)
            random_y = random(-2,2)
            x += random_x
            y += random_y
            point_list.append([x,y])

    limit = 0
    for x in range(-half_canvas, half_canvas,5):
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

    print point_list
    rotate(random(0,6.3))
    drawCircle(point_list,iterator)


def drawCircle(point_list, iterator):
    random_color = int(random(0,len(grid_colors)))
    stroke(grid_colors[random_color][0], grid_colors[random_color][1], grid_colors[random_color][2])
    for j in range(0,len(point_list)-3):
        curve(point_list[j][0], point_list[j][1],point_list[j+1][0], point_list[j+1][1], point_list[j+2][0], point_list[j+2][1], point_list[j+3][0], point_list[j+3][1])
        #save_image(j,iterator)

def draw():
    translate(canvas_size/2, canvas_size/2)
    for x in range(0,400):    #18
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
