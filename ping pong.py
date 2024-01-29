import turtle

#creating background

z= turtle.Screen()
z.title("pong")
z.bgcolor("grey")
z.setup(width=800,height=800)

#creating first paddle

blocka = turtle.Turtle()
blocka.shape("square")
blocka.speed(0)
blocka.shapesize(stretch_wid=6,stretch_len=1)
blocka.color("black")
blocka.penup()
blocka.goto(-385,0)       
         
#creating second paddle

blockb = turtle.Turtle()
blockb.shape("square")
blockb.speed(-0)
blockb.shapesize(stretch_wid=6,stretch_len=1)
blockb.color("black")
blockb.penup()
blockb.goto(378,0)

#creating a ball

ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.speed(0)
ball.shapesize(stretch_wid=1,stretch_len=1)
ball.penup()

#score
scorea =0
scoreb =0

#adding scoreboard

s = turtle.Turtle()
s.shape("circle")
s.penup()
s.speed(0)
s.goto(-270,350)
s.hideturtle()
s.color("maroon")
s.write("Player left:0 Player right:0", font=("courier",20,"bold"))

# defining functions for paddles

def blockaup():
    y = blocka.ycor()
    y += 15
    blocka.sety(y)
    
def blockadown():
    y = blocka.ycor()
    y -= 15
    blocka.sety(y)
    
def blockbup():
    y = blockb.ycor()
    y += 15
    blockb.sety(y)
    
def blockbdown():
    y = blockb.ycor()
    y -= 15
    blockb.sety(y)
    
#using keyboard to move paddles and ball
    
z.listen()
z.onkeypress(blockaup,"w")
z.onkeypress(blockadown,"s")
z.onkeypress(blockbup,"Up")
z.onkeypress(blockbdown,"Down")
ball.speedx = 4
ball.speedy = 4    
while True:
     z.update()
    
     ball.setx(ball.xcor() + ball.speedx)
     ball.sety(ball.ycor() + ball.speedy)

     if ball.ycor()>370:
         ball.sety(370)
         ball.speedy *= -1
         
     if ball.ycor()<-370:
         ball.sety(-370)
         ball.speedy *= -1
     
     if ball.xcor() > 388:
         ball.goto(0,0)
         ball.speedx *= -1
         scorea +=1
         s.clear()
         s.write("Player left:{} Player right:{}".format(scorea,scoreb), font=("courier",20,"bold"))
     
     if ball.xcor() < -388:
         ball.goto(0,0)
         ball.speedx *= -1
         scoreb +=1
         s.clear()
         s.write("Player left:{} Player right:{}".format(scorea,scoreb), font=("courier",20,"bold"))
     

              
# ball and paddle collision

     if ball.xcor() > 350 and (ball.ycor() < blockb.ycor() + 70 and ball.ycor() > blockb.ycor() -70):
         ball.speedx *= -1
     
     if ball.xcor() < -350 and (ball.ycor() < blocka.ycor() + 70 and ball.ycor() > blocka.ycor() -70):
         ball.speedx *= -1




         

         
         
         
         
         
         