import turtle
bob=turtle.Turtle()
#bob.speed(0)
turtle.tracer(0)


def circle(radius, border_color, fill_color):
  bob.pencolor(border_color)
  bob.fillcolor(fill_color)
  bob.begin_fill()
  bob.circle(radius)
  bob.end_fill()

def star(dist,sides,c1,c2):
  for times in range(5):
   bob.color(c1)
   bob.fillcolor(c2)
   bob.forward(dist)
   bob.left(sides)

def polygon(dist,sides,color):
  angle=360/sides
  for times in range(sides):
    bob.color(color)
    bob.forward(dist)
    bob.left(angle)
    
def jump(x,y):
  bob.penup()
  bob.goto(x,y)
  bob.pendown()
  
def comet(c, distance, angle):
  bob.color(c)
  for times in range(10):
    bob.pensize(times / 2)
    bob.forward(distance)
    bob.left(angle)

def home():
  bob.penup()
  bob.home()
  #moves turtle to origin (0,0) & resets start orientation
  bob.pendown()
