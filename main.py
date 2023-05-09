import random
import turtle


window = turtle.Screen()
window.bgcolor("#DEFE28")
window.title("🐢🐢🐢🐢🐢🐢🐢")

#global variables
score = 0
gameOver = False
FONT = ("didot", 25, "bold")
grid = 10
b = window.window_height() / 2
a = window.window_width() / 2
i = [-20, -10, 0, 10, 20]
j = [20, 10, 0, -10, -20]
turtle_List = []
timer = turtle.Turtle()
scoreTurtle = turtle.Turtle()


def display_timer(time_limit):
    global gameOver
    timer.hideturtle()
    timer.penup()
    timer.goto(a*0.4, b*0.9)
    timer.color("#FC0089")
    timer.clear()
    if time_limit > 0:
        timer.clear()
        timer.write(arg=" Timer ⏰: {}".format(time_limit), align = "center", font=FONT) # displays the time limit
        window.ontimer(lambda : display_timer(time_limit - 1), 1000)
    else:
        gameOver = True
        timer.clear()
        hide_turtles()
        timer.write(arg="Sorry Game Over!", align="center",font=FONT)

def display_scoreTurtle():

    scoreTurtle.hideturtle()
    scoreTurtle.penup()
    scoreTurtle.goto(a*-0.4, b*0.9)
    scoreTurtle.color("#FC0089")
    scoreTurtle.write(arg="🐢Score: {}".format(score), align="center", font=FONT)


def make_turtle(x,y):
    tur = turtle.Turtle()

    def detect_click(x, y):
        global score
        score +=1
        scoreTurtle.clear()
        scoreTurtle.write(arg="🐢Score: {}".format(score), align="center", font=FONT)
        # print(x,y)

    tur.onclick(detect_click)
    tur.shape("turtle")
    tur.shapesize(2,2,3)
    tur.pencolor("DeepPink")
    tur.pensize(3)
    tur.fillcolor("pink")
    tur.penup()
    tur.goto(x *grid, y*grid)
    turtle_List.append(tur)


def display_turtle():
    for x in i:
        for y in j:
            make_turtle(x,y)


def hide_turtles():
    for tur in turtle_List:
        tur.hideturtle()


# recursive
def random_turtle():
    if not gameOver:
        hide_turtles()
        random.choice(turtle_List).showturtle()
        window.ontimer(random_turtle,500)


def gameStarter():
    turtle.tracer(0)

    display_scoreTurtle()
    display_timer(10)
    display_turtle()
    hide_turtles()
    random_turtle()

    turtle.tracer(1)


gameStarter()

turtle.mainloop()