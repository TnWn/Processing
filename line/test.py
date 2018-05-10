import datetime

X_CANVAS_SIZE = 1000
Y_CANVAS_SIZE = 3000
X_MARGIN = 300
Y_MARGIN = 50

def setup():
    size(X_CANVAS_SIZE, Y_CANVAS_SIZE)
    strokeWeight(2)
    background(255)
    smooth()
    frameRate(5000)
    background(20,20,20)
    colorMode(HSB, 1, 1 ,1)

x= random(X_MARGIN,X_CANVAS_SIZE-X_MARGIN)
y= random(Y_MARGIN,Y_CANVAS_SIZE-Y_MARGIN)
px= random(X_MARGIN,X_CANVAS_SIZE-X_MARGIN)
py= random(Y_MARGIN,Y_CANVAS_SIZE-Y_MARGIN)
dir = random(0,360)
limit = 0
takeImage = 0
h = 0
s = 0.1
b = 0.1

def incrementColor():
    global h
    global s
    global b
    if (h>1):
        h = 0
        if (s<0.8):
            s += 0.05
            b += 0.05
    else:
        h += 0.005
    stroke(h,s,b)

def drawLine():
    global x
    global y
    global px
    global py
    global dir
    global limit
    global takeImage
    vel = int(random(0,10))
    px = x
    py = y
    x+= cos(radians(dir))*vel
    y+= sin(radians(dir))*vel
    if ((y<Y_MARGIN) or (y>Y_CANVAS_SIZE-Y_MARGIN)):
        dir = -dir + random(-90,90)
        x+= (cos(radians(dir))*vel)
        y+= (sin(radians(dir))*vel)
        limit += 1
    if ((x<X_MARGIN) or (x>X_CANVAS_SIZE-X_MARGIN)):
        dir = dir - (180 + random(-90,90))
        x+= (cos(radians(dir))*vel)
        y+= (sin(radians(dir))*vel)
        limit += 1
    #how long the line can wander away from the boundaries
    if (limit > 300):
        x= random(X_MARGIN,X_CANVAS_SIZE-X_MARGIN)
        y= random(Y_MARGIN,Y_CANVAS_SIZE-Y_MARGIN)
        limit = 0
        takeImage += 1
        print takeImage
        if (takeImage > 3):
            saveImage()
            takeImage = 0
    line(px,py,x,y)

def draw():
    drawLine()
    incrementColor()

def saveImage():
    print "saving image"
    time = datetime.datetime.now().strftime("%d_%m_%H_%M_%S")
    print time
    fileName = "/pics/" + time + ".jpg"
    print fileName
    save(fileName)

def mouseClicked():
    saveImage()
    if (mouseButton == LEFT):
        print "END"
        noLoop()
