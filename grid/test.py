import datetime

canvas_size = 1000
rand_min = 50
rand_neg = -250
rand_max = 250
margin = 100
bgc = color(255, 255, 245)
grid_colors = [[225,90,80], [225,60,60], [194,100,100], [21,75,100], [12,90,80], [60,4,100]]

def setup():
    size(canvas_size,canvas_size)
    frameRate(30)
    background(bgc)
    strokeCap(ROUND)
    strokeCap(ROUND)
    smooth(4)

def hole():
    noStroke()
    fill(bgc)
    for y in range(0,10):
        random_shape = int(random(0.5,4.5))
        if (random_shape == 1):
            ellipse(random(0,canvas_size), random(0,canvas_size), random(rand_min, rand_max), random(rand_min, rand_max))
        if (random_shape == 2):
            rect(random(0,canvas_size), random(0,canvas_size), random(rand_min, rand_max), random(rand_min, rand_max),random(10,50))
        if (random_shape == 3):
            random_x = random(0,canvas_size)
            random_y = random(0,canvas_size)
            triangle(random_x, random_y, random_x + random(rand_neg , rand_max), random_y + random(rand_neg , rand_max), random_x + random(rand_neg , rand_max), random_y + random(rand_neg , rand_max))
        if (random_shape == 4):
            random_x = random(0,canvas_size)
            random_y = random(0,canvas_size)
            quad(random_x, random_y, random_x + random(rand_neg , rand_max), random_y + random(rand_neg , rand_max), random_x + random(rand_neg , rand_max), random_y + random(rand_neg , rand_max), random_x + random(rand_neg , rand_max), random_y + random(rand_neg , rand_max))

def grid(x):
    strokeWeight(random(0.1,1.5))
    random_color = int(random(0,len(grid_colors)))
    stroke(grid_colors[random_color][0], grid_colors[random_color][1], grid_colors[random_color][2])
    rotate(random(0,6.3))
    for x in range(-canvas_size, canvas_size, canvas_size/x):
        wiggle = random(-30,30)
        line(x + wiggle, 0 + wiggle, x + wiggle, canvas_size + wiggle)
        line(0 + wiggle, x + wiggle, canvas_size + wiggle, x + wiggle)

def draw():
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
