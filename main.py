from turtle import Turtle, Screen
import pandas

SCORE = 0


# # Screen setup
screen = Screen()
screen.title("U.S Guess the State")
image = "blank_states_img.gif"
screen.bgpic(image)


# # # Getting the states data
states_data = pandas.read_csv("50_states.csv")


is_game_on = True
while is_game_on:
    user_answer = screen.textinput(title=f"States correct {SCORE}/{len(states_data.state)}", prompt="Guess a state: ").lower()
    for state in states_data.state:
        if user_answer == state.lower():
            # increase score, get state coordinates, goto coordinates
            SCORE += 1
            x_cor = states_data.x[states_data.state == state].max()
            y_cor = states_data.y[states_data.state == state].max()
            state_name = Turtle()
            state_name.penup()
            state_name.goto(x_cor, y_cor)
            state_name.write(state, align="center", font=("arial", 10, "normal"))
            



screen.exitonclick()

