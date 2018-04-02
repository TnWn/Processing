import datetime

canvas_size = 1200
max = 900
min = 300

def setup():
    size(canvas_size, canvas_size)
    background(80,80,80)
    strokeWeight(20)
    strokeJoin(ROUND)
    strokeCap(ROUND)

def draw_line():
    oldx = int(random(3,9)) * 100
    oldy = int(random(3,9)) * 100
    stationList = []

    #Draw Lines
    for x in range(0,10):    # number of stations

        newx = 0
        newy = 0

        while ((newx < min) or (newx > max) or (newy < min) or (newy > max) or ([tempx,tempy] in stationList)):     #bounding boxes
            print [oldx,oldy] in stationList
            print stationList
            direction_seed = random(0,3)
            if (direction_seed <= 1):
                randomx = 0
                randomy = int(random(-2,2)) * 100
            elif (direction_seed <=2):
                randomx = int(random(-2,2)) * 100
                randomy = 0
            else:
                randomx = int(random(-2,2)) * 100
                randomy = int(random(-2,2)) * 100
            print randomx, randomy

            newx = oldx + randomx
            newy = oldy + randomy
            print newx, newy
            tempx = newx
            tempy = newy
            print ((newx < 100) or (newx > 1100) or (newy < 100) or (newy > 1100) or ([tempx,tempy] in stationList))

        line(oldx, oldy, newx, newy)
        #ellipse(oldx, oldy, 20, 20)
        print [oldx,oldy] in stationList
        stationList.append([oldx, oldy])
        print oldx, oldy, newx, newy
        oldx = newx
        oldy = newy

    #get the last one
    stationList.append([oldx, oldy])

    print stationList
    print len(stationList)

    #Draw stations
    for y in range(0,len(stationList)):
        stationx = stationList[y][0]
        stationy = stationList[y][1]
        ellipse(stationx, stationy , 10, 10)

def draw():

    '''
    for x in range(100,1100,100):
        for y in range(100,1100,100):
            ellipse(x,y,10,10)
    '''

    line_colors = [[225,90,80,50], [225,60,60,50], [194,100,100,50], [21,75,100,50], [12,90,80,50], [60,4,100,50]]

    for x in range(1,5):

        #stroke(line_colors[x][0],line_colors[x][1],line_colors[x][2],line_colors[x][3])
        stroke(line_colors[x][0],line_colors[x][1],line_colors[x][2])
        draw_line()

    '''
    time = datetime.datetime.now().strftime("%d_%m_%H_%M_%S")
    print time
    fileName = "/pics/" + time + ".jpg"
    print fileName
    save(fileName)
    '''
    noLoop()
