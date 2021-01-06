from turtle import Turtle, Screen
import pandas as pd


# # Screen setup
screen = Screen()
screen.title("U.S Guess the State")
image = "blank_states_img.gif"
screen.bgpic(image)


# Getting the states data
states_data = pd.read_csv("50_states.csv")
all_states = states_data.state.to_list()


right_guesses = []


while len(right_guesses) < 50:
    user_answer = screen.textinput(title=f"States correct {len(right_guesses)}/{len(states_data.state)}", prompt="Guess a state: ").title()


    if user_answer == "Exit":
        states_to_learn = [all_states.remove(guess) for guess in right_guesses if guess in all_states]
        states_to_learn.append(all_states)
        df = pd.DataFrame(states_to_learn)
        df.to_csv("states_to_learn.csv")
        break


    for state in states_data.state:
        if user_answer == state:
            if state not in right_guesses:
                right_guesses.append(user_answer)
            x_cor = states_data.x[states_data.state == state].max()
            y_cor = states_data.y[states_data.state == state].max()
            state_name = Turtle()
            state_name.penup()
            state_name.goto(x_cor, y_cor)
            state_name.hideturtle()
            state_name.write(state, align="center", font=("arial", 10, "normal"))
        
            




