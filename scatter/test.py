import datetime

canvas_size = 5000
border = 200
max_points = 100

def setup():
    size(canvas_size,canvas_size)
    background(20,20,20)

    strokeWeight(4)
    strokeJoin(BEVEL)
    strokeCap(ROUND)

def scatter_points():
    point_list = []
    for i in range(0,max_points):
        randx = int(random(0, canvas_size))
        randy = int(random(0, canvas_size))
        point_list.append([randx,randy])
    return point_list

def draw_lines(point_list):
    noFill()
    #COLOR_LIST = [[212, 255, 228], [165, 225, 204], [118, 195, 184], [66, 166, 167], [0, 136, 151], [0, 107, 136]]
    COLOR_LIST = [[179, 68, 11], [177, 47, 71], [147, 56, 108], [101, 70, 123], [59, 75, 113], [47, 72, 88]]
    temp = ((len(point_list) - 3) / 6)
    for j in range(0,len(point_list)-3):
        if (j < temp):
            stroke(COLOR_LIST[0][0], COLOR_LIST[0][1], COLOR_LIST[0][2])
        elif (j < (temp * 2)):
            stroke(COLOR_LIST[1][0], COLOR_LIST[1][1], COLOR_LIST[1][2])
        elif (j < (temp * 3)):
            stroke(COLOR_LIST[2][0], COLOR_LIST[2][1], COLOR_LIST[2][2])
        elif (j < (temp * 4)):
            stroke(COLOR_LIST[3][0], COLOR_LIST[3][1], COLOR_LIST[3][2])
        elif (j < (temp * 5)):
            stroke(COLOR_LIST[4][0], COLOR_LIST[4][1], COLOR_LIST[4][2])
        elif (j < (temp * 6)):
            stroke(COLOR_LIST[5][0], COLOR_LIST[5][1], COLOR_LIST[5][2])
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
    average_point_list = points
    for i in range(0,100):
        print average_point_list
        if ((i > 3) and (i % 2 == 0)):
            draw_lines(average_point_list)
        average_point_list = average_points(average_point_list)
    noLoop()
    time = datetime.datetime.now().strftime("%d_%m_%H_%M_%S")
    fileName = "/pics/" + time + ".jpg"
    print fileName
    save(fileName)
    print "SAVED"
