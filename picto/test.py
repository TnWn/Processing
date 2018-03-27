import datetime

def setup():
    size(1200,1200)
    background(20,20,20)

def drawLines():

    stroke(255,255,255)
    strokeWeight(20)
    strokeJoin(ROUND)
    strokeCap(ROUND)

    size = 50
    test = []
    color_set = [[178,27,60],[255,250,162],[255,93,128],[54,163,204],[56,145,178]]

    oldx = int(random(1,3)) * 300
    print oldx
    oldy = int(random(1,3)) * 300
    print oldy
    for i in range(0,10):

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

        fill(20,20,20)

        rand_color = color_set[int(random(0,4))]
        print rand_color
        stroke(rand_color[0], rand_color[1], rand_color[2])

        print c
        x = c[0]
        y =  c[1]
        shape = int(random(6))
        if (shape == 0):
            ellipse(x,y,(size*4),(size*4))
        elif (shape == 1):
            rect(x-(size*2),y-(size*2),(size*4),(size*4))
        elif (shape == 2):
            triangle(x-(size*2),y+(size*2),x+(size*2),y+(size*2),x,y-(size*2))
        elif (shape == 3):
            ellipse(x,y,(size*3),(size*3))
        elif (shape == 4):
            rect(x-(size*1.5),y-(size*1.5),(size*3),(size*3))
        elif (shape == 5):
            triangle(x-(size*1.5),y+(size*1.5),x+(size*1.5),y+(size*1.5),x,y-(size*1.5))
        elif (shape == 6):
            #do nothing
            print "nothing"

def draw():
    drawLines()

    time = datetime.datetime.now().strftime("%d_%m_%H_%M")
    print time
    fileName = "/pics/" + time + ".jpg"
    print fileName
    save(fileName)
    noLoop()
