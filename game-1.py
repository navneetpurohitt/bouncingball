import random 
import turtle
wn = turtle.Screen()
wn.bgcolor("black")
wn.tracer(0)
wn.title("Bouncing ball simulator")
balls = []
for _ in range(100):
    balls.append(turtle.Turtle())
colors=["red","blue","white","orange","purple","tomato"]

for ball in balls:
    x = random.randint(-290,290)
    y = random.randint(200,400)
    ball.shape("circle")
    ball.penup()
    ball.speed(0)
    ball.color(random.choice(colors))
    ball.goto(x,y)
    
    ball.dy = 0
    ball.dx = random.randint(-3,3)

    gravity = 0.1


while(True):
    wn.update()
    for ball in balls:

        ball.dy -=gravity

        ball.sety(ball.ycor()+ball.dy)
        ball.setx(ball.xcor()+ball.dx)
        if(ball.xcor()> 300):
            ball.dx *=-1
        if(ball.xcor()< -300):
            ball.dx *=-1
        
        # check for a bounce
        if ball.ycor()< -300:
            ball.dy *= -1













wn.mainloop()