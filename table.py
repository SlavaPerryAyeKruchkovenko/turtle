import turtle
import random

def draw_polygon(turtle, count_of_corner, lenght_of_line):
    turtle.pendown()
    for number in range(count_of_corner):
        turtle.fd(lenght_of_line)
        if number + 1 < count_of_corner:
            turtle.right(360/count_of_corner)

if __name__ == '__main__':
    tommy = turtle.Turtle()
    tommy.shape("turtle")
    tommy.speed(300)

    N = int(input('Введите N\n'))
    M = int(input('Введите M\n'))
    lenght = 40

    for val1 in range(N):
        for val2 in range(M):
            tommy.right(90)
            tommy.forward(lenght)
            tommy.left(180)
            tommy.forward(lenght)
            tommy.right(90)
            tommy.forward(lenght)
        tommy.right(90)
        tommy.forward(lenght)
        tommy.left(90)
        tommy.setx(0)

    tommy.penup()
    tommy.sety(-lenght/4)
    tommy.setx(lenght / 4)

    for val1 in range(N):
        for val2 in range(M):
            tommy.pendown()
            cornes = random.randrange(3,10)
            draw_polygon(tommy,cornes,lenght/cornes)
            tommy.penup()
            tommy.setheading(0)
            tommy.forward(lenght)
        tommy.setx(lenght / 4)
        tommy.setheading(270)
        tommy.forward(lenght)
        tommy.setheading(0)

    tommy.setx(0)
    tommy.sety(0)
    input('Press ENTER to exit')