import datetime

canvas_size = 5000
border = 200
max_points = 100

def setup():
    size(canvas_size,canvas_size)
    background(20,20,20)

    stroke(255,255,255)
    strokeWeight(1)
    strokeJoin(BEVEL)
    strokeCap(ROUND)

def scatter_points():
    point_list = []
    for i in range(0,max_points):
        randx = int(random(border, canvas_size - border))
        randy = int(random(border, canvas_size - border))
        point_list.append([randx,randy])
    return point_list

def draw_lines(point_list):
    noFill()
    for j in range(0,len(point_list)-3):
        print point_list[j][0], point_list[j][1], point_list[j+1][0], point_list[j+1][1]
        #line(point_list[j][0], point_list[j][1], point_list[j+1][0], point_list[j+1][1])
        curve(point_list[j][0], point_list[j][1],point_list[j+1][0], point_list[j+1][1], point_list[j+2][0], point_list[j+2][1], point_list[j+3][0], point_list[j+3][1])

def average_points(list):
    new_list = []
    for j in range(0,len(list)-1):
        new_list_x = ((list[j][0] + list[j + 1][0])/2)
        new_list_y = ((list[j][1] + list[j + 1][1])/2)
        new_list.append([new_list_x, new_list_y])
    return new_list

def draw():
    points = scatter_points()
    print points
    draw_lines(points)
    average_point_list = average_points(points)
    for i in range(0,50):
        print average_point_list
        draw_lines(average_point_list)
        average_point_list = average_points(average_point_list)
    noLoop()
    time = datetime.datetime.now().strftime("%d_%m_%H_%M_%S")
    print time
    fileName = "/pics/" + time + ".jpg"
    print fileName
    save(fileName)
