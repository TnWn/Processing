import datetime

canvas_size = 1000

def setup():
    size(canvas_size,canvas_size)
    strokeWeight(10)
    background(255)
    smooth()
    frameRate(30)
    background(20,20,20)
    rand_color = color_set[int(random(0,9))]
    stroke(rand_color[0], rand_color[1], rand_color[2])

x= random(200,800)
y= random(200,800)
px= random(200,800)
py= random(200,800)
color_set = [[158,91,178], [255,233,181], [232,156,255], [104,204,165], [100,178,148], [178,98,91], [240,255,148], [255,164,156], [104,152,204], [108,142,178]]

def draw():
    global x
    global y
    global px
    global py

    vel = int(random(0,10))
    dir = int(random(0,360))
    px = x
    py = y

    x+= cos(radians(dir))*vel
    y+= sin(radians(dir))*vel

    if ((x<0) or (x>1000) or (y<0) or (y>1000)):
        x= int(random(0,1000))
        y= int(random(0,1000))
        px= int(random(0,1000))
        py= int(random(0,1000))
        rand_color = color_set[int(random(0,9))]
        print rand_color
        stroke(rand_color[0], rand_color[1], rand_color[2])

    line(px,py,x,y)

    dir+=random(-30,30)

def mouseClicked():
    print "END"
    time = datetime.datetime.now().strftime("%d_%m_%H_%M")
    print time
    fileName = "/pics/" + time + ".jpg"
    print fileName
    save(fileName)
    noLoop()
