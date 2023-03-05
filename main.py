from turtle import Turtle, Screen

import pandas

turtle1 = Turtle()
turtle2 = Turtle()
screen = Screen()
screen.title("U.S States Map")
image = "blank_states_img.gif"
screen.addshape(image)
turtle1.shape(image)

game_is_on = True
turn = 0
count = 0
while game_is_on:
    answer_text = screen.textinput(title=f"Guess the states, {turn}/60", prompt="What's another state name").title()
    turn = turn + 1
    print(answer_text)
    data = pandas.read_csv('50_states.csv')
    new_list = data['state'].to_list()
    # fetching the data from csv file
    if answer_text == "Exit":
        break
    for a in new_list:
        if answer_text in a:
            count = count + 1
            first = data[data.state == answer_text]
            xcor = int(first.x)
            second = data[data.state == answer_text]
            ycor = int(second.y)
            turtle2.color('black')
            turtle2.penup()
            turtle2.hideturtle()
            turtle2.goto(xcor, ycor)
            turtle2.write(answer_text, move=False, align='center', font=('Arial', 7, 'normal'))

        elif answer_text not in a:
            pass

    if turn == 60:
        game_is_on = False
    if answer_text in new_list:
        new_list.remove(answer_text)
    new_data = pandas.DataFrame(new_list)
    new_data.to_csv('states to learn.csv')




