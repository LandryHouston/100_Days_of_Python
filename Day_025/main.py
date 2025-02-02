import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(width=750, height=515)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")

correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        missing_states = []
        for state in data['state'].values:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv", index=False, header=False)
        break
    if answer_state in data['state'].values and answer_state not in correct_guesses:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data['state'].item(), align='center')
        correct_guesses.append(answer_state)