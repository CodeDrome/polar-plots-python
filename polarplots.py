import turtle
import math


def main():

    print("--------------------")
    print("| codedrome.com    |")
    print("| Polar Plots with |")
    print("| Turtle Graphics  |")
    print("--------------------\n")

    # Uncomment this line to make drawing
    # a lot faster or change the argument
    # to any value. Default is 10ms.
    turtle.delay(0)

    draw_axes(150)

    #plot("circle", 120, 0, 360, circle_function)
    #plot("cardioid", 75, 0, 360, cardioid_function)
    #plot("spiral", 100, 0, 2880, spiral_function)
    plot("rose", 150, 0, 360, rose_function)

    turtle.hideturtle()

    # This stops the window closing after drawing is finished
    turtle.exitonclick()


def draw_axes(radius):

    """
    Draw lines from the origin every
    15 degrees with the angles labelled.
    """

    FONT_SIZE = 8
    FONT = ("Arial", FONT_SIZE, "bold")

    width = radius * 2 + 100
    height = radius * 2 + 100

    turtle.title("Polar Plot")

    turtle.screensize(canvwidth=width, canvheight=height)
    turtle.setup(width=width + 40, height=height + 40)
    turtle.shape("turtle")

    degree_label_radius = radius + 16

    turtle.pencolor(0.0, 0.0, 1.0)

    for degrees in range(0, 360, 15):

        radians = math.radians(degrees)

        turtle.penup()
        turtle.home()

        turtle.pendown()
        turtle.goto(math.cos(radians) * radius, math.sin(radians) * radius)

        turtle.penup()
        turtle.goto(math.cos(radians) * degree_label_radius,
                    math.sin(radians) * degree_label_radius)

        turtle.goto(turtle.position()[0], turtle.position()[1] - FONT_SIZE)

        turtle.pendown()
        turtle.write(str(degrees) + u'\u00B0', align='center', font=FONT)


def plot(title, radius, start_degrees, end_degrees, function):

    """
    Draw a polar plot with the given radius
    from/to the given angles.

    The plot positions are calculated by
    the supplied function.

    Any function can be used but it must
    have these arguments:
        radians - the current angle
        radius - in pixels
    and return a dictionary with:
        x - coordinate in pixels
        y - coordinate in pixels
    """

    turtle.title(title)

    turtle.pensize(2)
    turtle.pencolor(1.0, 0.0, 0.0)
    turtle.penup()

    for degrees in range(start_degrees, end_degrees + 1):

        radians = math.radians(degrees)

        pos = function(radians, radius)
        turtle.goto(pos["x"], pos["y"])

        turtle.pendown()


def circle_function(radians, radius):

    """
    Calculate the coordinates of the
    edge of the circle at the given angle.
    """

    return {"x": math.cos(radians) * radius,
            "y": math.sin(radians) * radius}


def cardioid_function(radians, radius):

    """
    Calculate the distance from the origin
    for the given angle, then calculate
    its coordinates.
    """

    distance = (1 + math.cos(radians)) * radius

    return {"x": math.cos(radians) * distance,
            "y": math.sin(radians) * distance}


def spiral_function(radians, radius):

    """
    Calculate the distance from the origin
    for the given angle, then calculate
    its coordinates.

    a - the rotation of the spiral
    b - distance between lines
    """

    a = 1
    b = 3

    distance = a + b * radians

    return {"x": math.cos(radians) * distance,
            "y": math.sin(radians) * distance}


def rose_function(radians, radius):

    """
    Calculate the distance from the origin
    for the given angle, then calculate
    its coordinates.

    I'm not going to tell you what n does!
    Find out for yourself :)
    """

    n = 6

    distance = math.sin(radians * n) * radius

    return {"x": math.cos(radians) * distance,
            "y": math.sin(radians) * distance}


main()
