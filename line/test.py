import datetime

canvas_size = 1000
margin = 200

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
dir = random(0,360)

def draw():
    global x
    global y
    global px
    global py
    global dir

    vel = int(random(0,10))
    px = x
    py = y

    x+= cos(radians(dir))*vel
    y+= sin(radians(dir))*vel
    if ((y<margin) or (y>canvas_size-margin)):
        rand_color = color_set[int(random(0,9))]
        stroke(rand_color[0], rand_color[1], rand_color[2])
        print dir
        dir = -dir + random(-90,90)
        x+= (cos(radians(dir))*vel)
        y+= (sin(radians(dir))*vel)
        print x, y
    elif ((x<margin) or (x>canvas_size-margin)):
        rand_color = color_set[int(random(0,9))]
        stroke(rand_color[0], rand_color[1], rand_color[2])
        print dir
        dir = dir - (180 + random(-90,90))
        x+= (cos(radians(dir))*vel)
        y+= (sin(radians(dir))*vel)
        print x, y

    line(px,py,x,y)

    #dir += random(-5,5)

def mouseClicked():
    print "END"
    time = datetime.datetime.now().strftime("%d_%m_%H_%M")
    print time
    fileName = "/pics/" + time + ".jpg"
    print fileName
    save(fileName)
    noLoop()
