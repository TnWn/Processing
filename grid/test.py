import datetime

canvas_size = 1000
rand_min = 100
rand_neg = -300
rand_max = 300
c = color(144, 180, 187)

def setup():
    size(canvas_size,canvas_size)
    strokeWeight(1)
    background(255)
    smooth()
    frameRate(30)
    background(c)

def hole():
    noStroke()
    fill(c)
    for y in range(0,5):
        random_shape = int(random(0.5,4.5))
        if (random_shape == 1):
            ellipse(random(0,canvas_size), random(0,canvas_size), random(rand_min, rand_max), random(rand_min, rand_max))
        if (random_shape == 2):
            rect(random(0,canvas_size), random(0,canvas_size), random(rand_min, rand_max), random(rand_min, rand_max))
        if (random_shape == 3):
            random_x = random(0,canvas_size)
            random_y = random(0,canvas_size)
            triangle(random_x, random_y, random_x + random(rand_neg , rand_max), random_y + random(rand_neg , rand_max), random_x + random(rand_neg , rand_max), random_y + random(rand_neg , rand_max))
        if (random_shape == 4):
            random_x = random(0,canvas_size)
            random_y = random(0,canvas_size)
            quad(random_x, random_y, random_x + random(rand_neg , rand_max), random_y + random(rand_neg , rand_max), random_x + random(rand_neg , rand_max), random_y + random(rand_neg , rand_max), random_x + random(rand_neg , rand_max), random_y + random(rand_neg , rand_max))

#maybe add variation to thickness & color. rotate grids?
def grid(x):
    stroke(1)
    for x in range(0,canvas_size, canvas_size/x):
        line(x, 0, x, canvas_size)
        line(0, x, canvas_size, x)

def draw():
    for x in range(0,1000):
        print x
        hole()
        grid(int(random(1,100)))
    noLoop()

def mouseClicked():
    print "END"
    time = datetime.datetime.now().strftime("%d_%m_%H_%M")
    print time
    fileName = "/pics/" + time + ".jpg"
    print fileName
    save(fileName)

    noLoop()
