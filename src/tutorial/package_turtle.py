import turtle as t 
import random


# References 
# Turtle color : https://trinket.io/docs/colors
#  Random walk : https://en.wikipedia.org/wiki/Random_walk



tur = t.Turtle()
tur.pensize(15)
tur.speed(0)

directions = [0,90,180,270]
colors = ['olive', 'dark green', 'crimson', 'blue violet', 'khaki', 'blue', 'dim gray']


# draw a shape
def draw_shapes(no_of_sides):
    angle = 360/no_of_sides

    for _ in range(no_of_sides):
        tur.forward(100)
        tur.right(angle)

for s in range(3,11):
    draw_shapes(s)



def random_walk(no_of_steps):
    for _ in range(no_of_steps):
        tur.color(random.choice(colors))
        tur.forward(30)
        tur.setheading(random.choice(directions))

if __name__ == "__main__":
    random_walk(4)


