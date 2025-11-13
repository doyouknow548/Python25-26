from myFunction import*
from random import randint
turtle.colormode(255)
turtle.bgcolor("black")

num = randint(10, 100)
i=randint(5, 10)
for times in range( num ):
    border = ("white")
    fill = ("white")
    circle(5, border, fill )
    x = randint(-350,350)
    y = randint(-350, 350)
    jump(x,y)

for times in range( i ):
 c1=("yellow")
 c2=("yellow")
 bob.fillcolor(c2)
 bob.begin_fill()
 star(50,144,c1,c2)
 bob.end_fill()
 x = randint(-400,400)
 y = randint(-400, 400)
 jump(x,y)


home()
bob.width(5)
for times in range(245):
    color=(times+10, times,200)
    polygon(100,4,color)
    bob.left(120)
    bob.forward(times-10)


