import turtle as t
import random

screen = t.Screen()

is_on = False
colors = ["red","yellow","green","blue","orange"]

screen.setup(width=500,height=400)
user_input = (screen.textinput(title="Make your bet",prompt="On which colored turtle are you betting on?")).lower()

if user_input:
    is_on = True

all_turtles = []
y = -100
for i in range(0,5):
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.pu()
    new_turtle.setpos(-230,y)
    y += 50
    all_turtles.append(new_turtle)
    
while is_on:
    for i in range(0,len(all_turtles)):
        all_turtles[i].forward(random.randint(1,10))
        xpos = all_turtles[i].pos()
        if int(xpos[0]) >= 230:
            is_on = False
            col = all_turtles[i].color()
            if (col[0] == user_input):
                print(f"You won the bet. The {col[0]} turtle won the race.")
                break
            else:
                print(f"You lost the bet. The {col[0]} color turtle won the race.")
                break
                
screen.exitonclick()