import datetime
import math

CANVAS_SIZE = 1000
PETRI_SIZE = (CANVAS_SIZE * 0.9)
generateList = []

def setup():
    size(CANVAS_SIZE, CANVAS_SIZE)
    background(255, 255, 255)

def drawPetriDish():
    strokeWeight(5)
    noFill()
    ellipse(0, 0, PETRI_SIZE, PETRI_SIZE)

def generate():
    x = random(-CANVAS_SIZE, CANVAS_SIZE)
    y = random(-CANVAS_SIZE, CANVAS_SIZE)
    r = random(10,50)
    while (dist(x, y, 0, 0) > ((PETRI_SIZE/2) - r)):
        x = random(-CANVAS_SIZE, CANVAS_SIZE)
        y = random(-CANVAS_SIZE, CANVAS_SIZE)
        r = random(50,100)
    fill(100, 255, 0, 50)
    noStroke()
    ellipse(x, y, r, r)
    generateList.append([x,y])

def grow():
    for i in generateList:
        print i
        for j in range(0,1000):
            x = i[0] + random(-10, 10)
            y = i[1] + random(-10, 10)
            r = random(10,50)
            while (dist(x, y, 0, 0) > ((PETRI_SIZE/2) - r)):
                x = random(-CANVAS_SIZE, CANVAS_SIZE)
                y = random(-CANVAS_SIZE, CANVAS_SIZE)
                r = random(50,100)
        ellipse(x, y, r, r)

def draw():
    translate( (CANVAS_SIZE/2), (CANVAS_SIZE/2) )
    for x in range(0,50):
        drawPetriDish()
        generate()
    grow()
    noLoop()

def mouseClicked():
    print "END"
    time = datetime.datetime.now().strftime("%d_%m_%H_%M_%S")
    print time
    fileName = "/pics/" + time + ".jpg"
    print fileName
    save(fileName)

    noLoop()
