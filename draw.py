import turtle

def draw_square(t):
    for j in range(1,25):
        for i in range(1,5):
            t.forward(100)
            t.right(90)
        t.right(15)


def draw_art():
    window=turtle.Screen()
    window.bgcolor("red")

    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(8)

    draw_square(brad)
    window.exitonclick()
'''
    pp=turtle.Turtle()
    pp.shape("arrow")
    pp.color("blue")
    pp.circle(100)
'''



draw_art()
