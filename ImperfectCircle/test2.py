
def setup():
    size(1000,1000)
    background(20,20,20)
    strokeWeight(4)

def mousePressed():
    noLoop()

def draw():
    for x in range(0,800,20):

        seed = random(0,100)
        fill(20,20,20,15)
        stroke(255,255,255)
        y = 500 - sqrt(-x ** 2 + 1000 * x - 240000)
        test = random(0,4)
        if (test > 2):
            triangle(x,y, x+seed, y+seed, x-seed, y-seed)
        else:
            ellipse(x,y,y - seed, x - seed)
        fill(255,255,255)
        ellipse(x,y,x/100,x/100)

        seed = random(0,100)
        fill(20,20,20,15)
        stroke(255,255,255)
        y = sqrt((-x ** 2) + (1000 * x) - 240000) + 500
        test = random(0,4)
        if (test > 2):
            triangle(x,y, x+seed, y+seed, x-seed, y-seed)
        else:
            ellipse(x,y,y - seed, x - seed)
        fill(255,255,255)
        ellipse(x,y,x/100,x/100)

    noLoop()
