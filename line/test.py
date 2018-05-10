import datetime

CANVAS_SIZE = 1000
X_MARGIN = 300
Y_MARGIN = 50

def setup():
    size(CANVAS_SIZE,CANVAS_SIZE)
    strokeWeight(2)
    background(255)
    smooth()
    frameRate(5000)
    background(20,20,20)
    colorMode(HSB, 1, 1 ,1)
    #rand_color = color_set[int(random(0,len(color_set)))]
    #stroke(rand_color[0], rand_color[1], rand_color[2])

x= random(X_MARGIN,CANVAS_SIZE-X_MARGIN)
y= random(Y_MARGIN,CANVAS_SIZE-Y_MARGIN)
px= random(X_MARGIN,CANVAS_SIZE-X_MARGIN)
py= random(Y_MARGIN,CANVAS_SIZE-Y_MARGIN)
#color_set = [[158,91,178], [255,233,181], [232,156,255], [104,204,165], [100,178,148], [178,98,91], [240,255,148], [255,164,156], [104,152,204], [108,142,178]]
#color_set = [[255,0,0], [250,0,0], [245,0,0], [240,0,0], [235,0,0]]
dir = random(0,360)
limit = 0
h = 0
s = 0
b = 0

def incrementColor():
    global h
    global s
    global b
    if (h>1):
        h = 0
        s += 0.1
        b += 0.1
    elif (s>1):
        s = 0
        b = 0
    else:
        h += 0.001
    stroke(h,s,b)

def drawLine():
    global x
    global y
    global px
    global py
    global dir
    global limit
    vel = int(random(0,10))
    px = x
    py = y
    x+= cos(radians(dir))*vel
    y+= sin(radians(dir))*vel
    if ((y<Y_MARGIN) or (y>CANVAS_SIZE-Y_MARGIN)):
        dir = -dir + random(-90,90)
        x+= (cos(radians(dir))*vel)
        y+= (sin(radians(dir))*vel)
        limit += 1
    if ((x<X_MARGIN) or (x>CANVAS_SIZE-X_MARGIN)):
        dir = dir - (180 + random(-90,90))
        x+= (cos(radians(dir))*vel)
        y+= (sin(radians(dir))*vel)
        limit += 1
    if (limit > 50):
        x= random(X_MARGIN,CANVAS_SIZE-X_MARGIN)
        y= random(Y_MARGIN,CANVAS_SIZE-Y_MARGIN)
        limit = 0
    line(px,py,x,y)

def draw():
    drawLine()
    incrementColor()

def mouseClicked():
    time = datetime.datetime.now().strftime("%d_%m_%H_%M")
    print time
    fileName = "/pics/" + time + ".jpg"
    print fileName
    save(fileName)
    if (mouseButton == LEFT):
        print "END"
        noLoop()
