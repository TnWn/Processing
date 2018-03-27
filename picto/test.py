import datetime

def setup():
    size(1200,1200)
    background(80,80,80)

def drawLines():

    stroke(255,255,255)
    strokeJoin(ROUND)
    strokeCap(ROUND)

    size = 50
    test = []
    color_set = [[178,88,86],[255,255,144],[255,146,144],[115,167,204],[101,146,178]]
    strokeWeight(20)

    oldx = int(random(1,3)) * 300
    print oldx
    oldy = int(random(1,3)) * 300
    print oldy
    for i in range(0,6):

        rand_color = color_set[int(random(0,4))]
        print rand_color
        stroke(rand_color[0], rand_color[1], rand_color[2])

        print i
        randx = int(random(1,4))
        randx = randx * 300
        print randx
        randy = int(random(1,4))
        randy = randy * 300
        print randy
        line(oldx,oldy,randx,randy)
        oldx = randx
        oldy = randy
        temp = [randx,randy]
        if temp in test:
            print "ALREADY EXISTS"
        else:
            test.append([randx,randy])

    for c in test:

        fill(80,80,80)

        rand_color = color_set[int(random(0,4))]
        print rand_color
        stroke(rand_color[0], rand_color[1], rand_color[2])
        strokeWeight(15)

        print c
        x = c[0]
        y =  c[1]
        shape = int(random(7))

        #Large size
        if (shape == 0):
            ellipse(x,y,(size*4),(size*4))
        elif (shape == 1):
            rect(x-(size*2),y-(size*2),(size*4),(size*4))
        elif (shape == 2):
            triangle(x-(size*2),y+(size*2),x+(size*2),y+(size*2),x,y-(size*2))
        #medium size
        elif (shape == 3):
            ellipse(x,y,(size*2),(size*2))
        elif (shape == 4):
            rect(x-(size*1.5),y-(size*1.5),(size*3),(size*3))
        elif (shape == 5):
            triangle(x-(size*1.5),y+(size*1.5),x+(size*1.5),y+(size*1.5),x,y-(size*1.5))
        #small size
        elif (shape == 5):
            ellipse(x,y,(size*0.5),(size*0.5))
        elif (shape == 6):
            rect(x-(size*0.5),y-(size*0.5),(size),(size))
        elif (shape == 7):
            #do nothing
            print "nothing"

def draw():

    drawLines()

    time = datetime.datetime.now().strftime("%d_%m_%H_%M_%S")
    print time
    fileName = "/pics/" + time + ".jpg"
    print fileName
    save(fileName)

    noLoop()
