import turtle
from turtle import Turtle, Screen
import pandas as pd

FONT = ("Courier", 7, "normal")
ALIGNMENT = "center"

screen = Screen()
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)


def write_state(state, x, y):
    tim = Turtle()
    tim.hideturtle()
    tim.penup()
    tim.color("black")
    tim.goto(x=x, y=y)
    tim.write(arg=state, move=False, align=ALIGNMENT, font=FONT)


data = pd.read_csv("50_states.csv")
state_list = data["state"].to_list()
guessed_state = []

while len(guessed_state) < 50:

    state_input = (turtle.textinput(f"{len(guessed_state)}/50 States Correct", "Enter the name of State")).title()

    if state_input == "Exit":
        missed_state = [state for state in state_list if state not in guessed_state]
        pd.DataFrame(missed_state).to_csv("missed_state2")
        break

    if state_input in state_list:
        if state_input in guessed_state:
            continue
        else:
            guessed_state.append(state_input)

        state_data = data[data.state == state_input]
        state = state_data.state.item()
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)
        write_state(state, x_cor, y_cor)
