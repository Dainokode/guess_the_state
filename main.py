from turtle import Turtle, Screen


# Screen setup
screen = Screen()
screen.title("U.S Guess the State")
image = "blank_states_img.gif"
screen.bgpic(image)


user_answer = screen.textinput(title="Guess the state", prompt="Guess a state: ")


screen.exitonclick()