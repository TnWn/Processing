import datetime

canvas_size = 1000
rand_min = 100
rand_neg = -300
rand_max = 300
margin = 100
c = color(144, 180, 187)

#figure out background & line color scheme
def setup():
    size(canvas_size,canvas_size)
    strokeWeight(1)
    background(255)
    smooth()
    frameRate(30)
    background(c)

#rounded edges on shapes?
def hole():
    noStroke()
    fill(c)
    for y in range(0,6):
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

def grid(x):
    rotate(int(random(0,360)))
    stroke(int(random(1,5)))
    #for x in range(0 - margin, canvas_size + margin, canvas_size/x):
    for x in range(-canvas_size, canvas_size, canvas_size/x):
        wiggle = random(-30,30)
        line(x + wiggle, 0 + wiggle, x + wiggle, canvas_size + wiggle)
        line(0 + wiggle, x + wiggle, canvas_size + wiggle, x + wiggle)

def draw():
    '''
    for x in range(0,1000):
        print x
        hole()
        grid(int(random(1,100)))
    '''
    for x in range(0,5000):
        print x
        hole()
        grid(int(random(1,100)))
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
