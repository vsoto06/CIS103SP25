import turtle


my_turtle = turtle.Turtle()
my_turtle.speed(0)  


def draw_circle(x, y, radius, color):
   
    my_turtle.penup()
    my_turtle.goto(x, y - radius)
    my_turtle.pendown()
    my_turtle.fillcolor(color)
    my_turtle.begin_fill()
    my_turtle.circle(radius)
    my_turtle.end_fill()

def draw_rectangle(x, y, width, height, color):
    """Draws a filled rectangle at the specified position with the given width, height, and color."""
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.fillcolor(color)
    my_turtle.begin_fill()
    for _ in range(2):
        my_turtle.forward(width)
        my_turtle.right(90)
        my_turtle.forward(height)
        my_turtle.right(90)
    my_turtle.end_fill()


def draw_triangle(x, y, size, color):
    """Draws an equilateral triangle at the specified position with the given size and color."""
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.fillcolor(color)
    my_turtle.begin_fill()
    for _ in range(3):
        my_turtle.forward(size)
        my_turtle.right(120)
    my_turtle.end_fill()


face_color = "green"
draw_circle(0, 0, 100, face_color)  


left_eye_color = "red"
right_eye_color = "blue"
draw_circle(-30, 60, 20, left_eye_color)  
draw_circle(30, 60, 20, right_eye_color)  

draw_rectangle(-50, -30, 100, 10, "yellow")  

draw_triangle(0, -45, 30, "black")  


turtle.done()


