#required libraries
import turtle
import time
import random
#game page
wn = turtle.Screen()
wn.title("snake game")
wn.bgcolor("white")
wn.setup(600, 600)
wn.tracer(0)
#speed control
delay = 0.1
score = 0
high_score = 0
#snake head
head = turtle.Turtle()
colors = random.choice(['red', 'green', 'black', 'yellow', 'pink', 'brown', 'orange', 'purple'])
head.shape("square")
head.color(colors)
head.penup()
head.goto(0, 0)
head.direction = "stop"
#food
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black', 'yellow', 'pink', 'orange', 'purple'])
shaps = random.choice(['triangle', 'square', 'circle'])
food.shape(shaps)
food.color(colors)
food.penup()
food.goto(0, 100)
#score
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 , high Score : 0",align = "center", font = ("candara", 24, "bold"))
#move snake
def go_up():
    if head.direction != "down" :
        head.direction = "up"
def go_down():
    if head.direction != "up" :
        head.direction = "down"
def go_left():
    if head.direction != "right" :
        head.direction = "left"
def go_right():
    if head.direction != "left" :
        head.direction = "right"
#move snake head
def move ():
    if head.direction == "up" :
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down" :
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left" :
        x = head.xcor ()
        head.setx(x-20)
    if head.direction == "right" :
        x = head.xcor()
        head.setx(x+20)
#keys for control the snake
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
#snake body
segments = []
#ring for update the game
while True :
    wn.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290 :
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        #reset the game
        for segment in segments :
            segment.goto(1000, 1000)
        segment.clear()
        score = 0
        pen.clear() 
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
        delay = 0.1
    #snake body
    if head.distance(food) < 20 :
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        colors = random.choice(['red', 'green', 'black', 'yellow', 'pink', 'brown', 'orange', 'purple'])
        new_segment.color(colors)
        new_segment.penup()
        segments.append(new_segment)
        #new score
        delay -= 0.001
        score += 10
        if score > high_score :
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
        #move food
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
    #move snake
    for index in range (len(segments)-1, 0, -1):
        #previous position of snake
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    #hit the snake head with snake body
    for segment in segments:    
        if segment.distance(head) < 20:
            time.sleep(1) 
            head.goto(0, 0) 
            head.direction = "Stop"
            #remove the snake body
            for segment in segments:    
                segment.goto(1000, 1000) 
            segments.clear() 
            score = 0  
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
            delay = 0.1   
    time.sleep(delay)
wn.mainloop()
    
