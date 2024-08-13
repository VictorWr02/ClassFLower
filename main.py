import turtle
#=============================#
class Flower:
    # Description of the flower
    def __init__(self, age, height):
        self.age = age
        self.height = height

    def life(self):
        # Format the flower information
        return f"Age: {self.age} weeks, Height: {self.height} cm"
#==========================================================================#

print('hello world')

def display_text(text, turtle_obj, x, y):
    # Move the turtle to the specified position
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    # Write the text in black
    turtle_obj.color("black")
    turtle_obj.write(text, font=("Arial", 16, "normal"))


def display_dot(turtle_obj, x, y, height):
    # Move the turtle to the specified position for the dot
    turtle_obj.penup()
    turtle_obj.goto(x + 250, y)  # Adjust x to position the dot next to the text
    turtle_obj.pendown()

    # Set the color based on the height
    if height > 7:
        turtle_obj.color("green")
    else:
        turtle_obj.color("red")

    if height == 7:
        turtle_obj.color("grey")

    # Draw the dot
    turtle_obj.dot(15)  # Size of the dot


# Create Turtle screen and object
screen = turtle.Screen()
screen.title("Flowers Graphics")

t = turtle.Turtle()
t.hideturtle()

# Create flower objects
Flower1 = Flower(2, 10)
Flower2 = Flower(2, 6.5)
Flower3 = Flower(2, 5)
Flower4 = Flower(2, 14)
Flower5 = Flower(2, 7)


# Display flower information and dot on the screen
display_text(Flower1.life(), t, -200, 100)
display_dot(t, -200, 100, Flower1.height)

display_text(Flower2.life(), t, -200, 60)
display_dot(t, -200, 60, Flower2.height)

display_text(Flower3.life(), t, -200, 20)
display_dot(t, -200, 20, Flower3.height)

display_text(Flower4.life(), t, -200, -20)
display_dot(t, -200, -20, Flower4.height)

display_text(Flower5.life(), t, -200, -60)
display_dot(t, -200,  -60, Flower5.height)

# Keep the window open until closed by the user
turtle.done()

