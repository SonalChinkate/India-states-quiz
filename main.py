import turtle
import pandas
from turtle import Turtle
# from PIL import Image

screen = turtle.Screen()
# img = Image.open("india-map-outlines_img.jpg")
# img.save("IndiaOutline.gif")
screen.title("India States Game")
image = "India_outline_map.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("28_states.csv")
tim = Turtle()
tim.hideturtle()
tim.penup()

state_list = data["state"].to_list()
data_dict  = data.to_dict()
# print(data_dict["state"])
correct_answers = list()
# print(state_list)
# def get_mouse_on_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_on_click_coor)
# turtle.mainloop()
while len(correct_answers) != 28: 
    answer_state = screen.textinput(title=f"Score: {len(correct_answers)} / 28",prompt="What's another state name?").title()
    if answer_state in state_list:
        for key in data_dict["state"]:
            if data_dict["state"][key] == answer_state:
                k = key
        x_pos = data_dict["x"][k]
        y_pos = data_dict["y"][k]
        tim.goto(x=x_pos,y=y_pos)
        tim.write(f"{answer_state}","Courier",align="center")
        if answer_state in correct_answers:
            continue
        else:
            correct_answers.append(answer_state)
    else:
        continue

screen.exitonclick()

