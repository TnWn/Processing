import datetime

def setup():
    size(1000,1000)
    background(20,20,20)

def mousePressed():
    noLoop()

def createCircles(x,y):
    #rotate(HALF_PI)
    fill(20,20,20,2)
    stroke(240,240,240)
    strokeWeight(20)
    ellipse(x,y,y,x)
    fill(255,255,255)
    if ( x%15 == 0):
        strokeWeight(2)
        stroke(255,255,255)
        fill(255,255,255)
        #line(x,y,y,x)
        ellipse(x,y,(x**2)/50000,(x**2)/50000)

def draw():

    for j in range(0,360):
        translate((width/2),(height/2));
        rotate(radians(j));
        translate(-(width/2),-(height/2))

        for x in range(0,800):
            y = 500 - sqrt(-x ** 2 + 1000 * x - 240000)
            createCircles(x,y)

            y = sqrt((-x ** 2) + (1000 * x) - 240000) + 500
            createCircles(x,y)


        time = datetime.datetime.now().strftime("%d_%m_%H_%M")
        print time
        fileName = "/pics/animation3/" + "test" + str(j).zfill(3) + ".jpg"
        print fileName
        save(fileName)
        clear()

    noLoop()
