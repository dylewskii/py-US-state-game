from turtle import Turtle, Screen
import pandas

# Create the screen with a blank image of the US map
screen = Screen()
screen.title("US States")
image = "blank_states_img.gif"
screen.addshape(image)
turt = Turtle()
turt.shape(image)


# csv
states_data = pandas.read_csv("50_states.csv")
# lists
states_list = states_data["state"].to_list()
x_coors, y_coors = states_data["x"].to_list(), states_data["y"].to_list()
xy_coors = zip(x_coors, y_coors)
# dicts
states_dict = dict(zip(states_list, xy_coors))

# keep track of score and correct guesses
score = 0
correct_guesses = []

# Ask the user to guess a state
answer = screen.textinput(title=f"Score: {score}/50", prompt="Name a state: (Q to quit)").title()

while len(correct_guesses) != 50:
    if answer == "Q" or answer == "q":
        states_to_learn = [i for i in states_list if i not in correct_guesses]
        df = pandas.DataFrame(states_to_learn)
        df.to_csv("States Left to Learn.csv")
        break
    elif answer not in states_list or answer in correct_guesses:
        pass
    else:
        t = Turtle()
        t.hideturtle()
        t.penup()
        score += 1
        correct_guesses.append(answer)
        xy = states_dict[answer]
        t.setpos(x=xy[0], y=xy[1])
        t.write(f"{answer}")

    answer = screen.textinput(title=f"Score: {score}/50", prompt="Name a state: ").title()

if score == 50:
    turt.write(f"Wow! You guessed all 50 states. Score: {score}/50")
else:
    turt.write(f"Game over. Score: {score}/50")

screen.mainloop()
