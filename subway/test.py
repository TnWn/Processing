import datetime

canvas_size = 1200

def setup():
    size(canvas_size, canvas_size)
    background(80,80,80)

def draw_line():
    oldx = int(random(1,11)) * 100
    oldy = int(random(1,11)) * 100
    stationList = []
    for x in range(0,10):    # number of stations

        newx = 0
        newy = 0

        while ((newx < 100) or (newx > 1100) or (newy < 100) or (newy > 1100) or ([oldx,oldy] in stationList)):     #bounding boxes
            print [oldx,oldy] in stationList
            print stationList
            randomx = int(random(-2,2)) * 100
            randomy = int(random(-2,2)) * 100
            print randomx, randomy

            newx = oldx + randomx
            newy = oldy + randomy
            print newx, newy

        line(oldx, oldy, newx, newy)
        ellipse(oldx, oldy, 20, 20)
        print [oldx,oldy] in stationList
        stationList.append([oldx, oldy])
        print oldx, oldy, newx, newy

        oldx = newx
        oldy = newy

    print stationList


def draw():

    for x in range(100,1100,100):
        for y in range(100,1100,100):
            ellipse(x,y,10,10)

    draw_line()

    '''
    time = datetime.datetime.now().strftime("%d_%m_%H_%M_%S")
    print time
    fileName = "/pics/" + time + ".jpg"
    print fileName
    save(fileName)
    '''
    noLoop()
