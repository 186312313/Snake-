import turtle
import time
import random


#زمان تأخير
delay = 0.1

#امتياز
score = 0
high_score = 0


# تنظیم صفحه
wn = turtle.Screen()
wn.title("snake game")
wn.bgcolor("grey")
wn.setup(width=600, height=600)
wn.tracer(0)  # خاموش کردن انیمیشن صفحه برای بهبود کارایی




# ایجاد مار
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("purple")
head.penup()
head.goto(0,0)  
head.direction = "stop"

#غذاي مار
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
food.goto(0,100)

segments = []

#قلم
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0 High score:0" , align = "center" , font=("Courier" , 24 , "normal"))


#تابع حرکت مار

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"


    
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# کلیدها
wn.listen()
wn.onkeypress(go_up, " w ")    # حرکت به سمت بالا با کلید W
wn.onkeypress(go_down, " s ")  # حرکت به سمت پایین با کلید S
wn.onkeypress(go_left, " a ")   # حرکت به سمت چپ با کلید A
wn.onkeypress(go_right, " d ")  # حرکت به سمت راست با کلید D

        

#حلقه اصلي بازي
while True:
    wn.update()

    #بررسي برخورد با ديواره ها
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #پنهان کردن
        for segment in segments:
            segment.goto(1000,1000)

        #پاک کردن بخش هاي ليست
        segments.clear()


        #بررسي مجدد امتياز
        score = 0

        #بررسي مجدد تأخير
        delay=0.1

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score , high_score), align="center" , font=("Courier" , 24 , "normal"))


    #بررسي برخورد با غذا
    if head.distance(food) < 20:
        #حرکت تصادفي غذا
        x = random.randint(-290 , 290)
        y = random.randint(-290 , 290)
        food.goto(x , y)

        #اضافه کردن به بخش ها
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("pink")
        new_segment.penup()
        segments.append(new_segment)


        #کوتاه کردن تأخير
        delay -= 0.001


        #افزايش امتياز
        score+=10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score , high_score), align="center" , font=("Courier" , 24 , "normal"))

    #قسمت هاي انتهايي را به ترتيب معکوس حرکت مي دهيم
    for index in range(len(segments)-1 , 0 , -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x , y)
        
    #حرکت بخش 0 به جايي که سر است
    if len(segments) >0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x , y)

    move()

    #بررسي برخورد سر با قسمت هاي بدن مار
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            #پنهان کردن
            for segment in segments:
                segment.goto(1000,1000)

            #پاک کردن بخش هاي ليست
            segments.clear()



            #بررسي مجدد امتياز
            score = 0


            #بررسي مجدد تأخير
            delay=0.1

            #بروزرساني نمايش امتياز
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score , high_score), align="center" , font=("Courier" , 24 , "normal"))


            
    time.sleep(delay)




wn.mainloop()

