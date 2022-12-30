import turtle
import math

def draw_polygon(turtle, count_of_corner, lenght_of_line):
    possitions= []
    turtle.pendown()
    for number in range(count_of_corner):
        possitions.append(turtle.pos())
        turtle.fd(lenght_of_line)
        if number + 1 < count_of_corner:
            turtle.right(360 / count_of_corner)
    return possitions

def count_center(possitions):
    x = 0.0
    y = 0.0
    for vector in possitions:
        x += vector[0]
        y += vector[0]
    x /= len(possitions)
    y /= len(possitions)
    return (x,y)
def count_angle(now_pos,center):

    x_sum = now_pos[0] - center[0]
    y_sum = now_pos[1] - center[1]
    return math.atan2(y_sum,x_sum) * 180 / math.pi

if __name__ == '__main__':
    tommy = turtle.Turtle()
    tommy.shape("turtle")
    tommy.speed(300)
    lenght = 100
    count_of_corner = int(input('Введите количество углов\n'))

    possitions = draw_polygon(tommy, count_of_corner, lenght)
    center = count_center(possitions)
    center = (center[0],-center[1])

    default_angle = (count_of_corner-2)*180/count_of_corner

    for corner in range(count_of_corner):
        angle = count_angle(tommy.pos(),center)
        tommy_head = tommy.heading()
        tommy.setheading(angle)
        tommy.fd(lenght * 2 / 3)
        tommy.left(default_angle/2)
        draw_polygon(tommy, count_of_corner, lenght / count_of_corner)
        tommy.setheading(-(180 - angle))
        tommy.fd(lenght * 2 / 3)
        tommy.setheading(tommy_head)
        tommy.right(360 / count_of_corner)
        tommy.fd(lenght/2)
        tommy.left(default_angle+90-default_angle/2)
        draw_polygon(tommy, count_of_corner, lenght / count_of_corner)
        tommy.setheading(tommy_head)
        tommy.right(360/count_of_corner)
        tommy.fd(lenght / 2)


    input('Press ENTER to exit')

