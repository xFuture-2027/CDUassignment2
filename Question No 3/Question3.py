import turtle   # Import turtle module for drawing shapes


# This function draws one edge using recursion
def draw_edge(length, depth):

    # Base case: if depth is 0, just draw a straight line
    if depth == 0:
        turtle.forward(length)

    # Recursive case: modify the line
    else:
        # Divide the line into three equal parts
        length = length / 3

        # Draw the first part
        draw_edge(length, depth - 1)

        # Turn right to start the inward triangle
        turtle.right(60)
        draw_edge(length, depth - 1)

        # Turn left to complete the triangle shape
        turtle.left(120)
        draw_edge(length, depth - 1)

        # Turn right again and draw the last part
        turtle.right(60)
        draw_edge(length, depth - 1)


# This function draws the full polygon
def draw_polygon(sides, length, depth):

    # Calculate the turning angle for the polygon
    angle = 360 / sides

    # Draw each side of the polygon
    for _ in range(sides):
        draw_edge(length, depth)   # Draw one recursive edge
        turtle.right(angle)        # Turn for the next side


# Take input from the user
sides = int(input("Enter the number of sides: "))
length = int(input("Enter the side length: "))
depth = int(input("Enter the recursion depth: "))

# Turtle settings
turtle.speed(0)        # Fast drawing
turtle.hideturtle()    # Hide the turtle cursor
turtle.penup()         # Lift pen to move without drawing
turtle.goto(-length / 2, length / 2)  # Move to starting position
turtle.pendown()       # Start drawing

# Draw the pattern
draw_polygon(sides, length, depth)

# Keep window open
turtle.done()
