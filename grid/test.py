import datetime

canvas_size = 1000

def setup():
    size(canvas_size,canvas_size)
    strokeWeight(1)
    background(255)
    smooth()
    frameRate(30)
    background(200,150,150)

#add variation in hole shapes
def hole():
    noStroke()
    c = color(200,150,150)
    fill(c)
    for y in range(0,5):
        ellipse(random(0,canvas_size), random(0,canvas_size), random(100,500), random(100,500))

def grid(x):
    stroke(1)
    for x in range(0,canvas_size, canvas_size/x):
        line(x, 0, x, canvas_size)
        line(0, x, canvas_size, x)

def draw():
    for x in range(0,10):
        hole()
        grid(int(random(0,100)))
        #hole()
    noLoop()

def mouseClicked():
    print "END"
    time = datetime.datetime.now().strftime("%d_%m_%H_%M")
    print time
    fileName = "/pics/" + time + ".jpg"
    print fileName
    save(fileName)

    noLoop()
