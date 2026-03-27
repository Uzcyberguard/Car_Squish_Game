from turtle import Turtle, Screen
from Road import Road2
from cars import Cars
screen = Screen()


screen.setup(width=800, height=640)
screen.bgcolor("gray25")


gif_files = [f"car{i}.gif" for i in range(1, 16)]
screen.register_shape("road.gif")

for pic in gif_files:
    screen.addshape(pic)


road = Road2()
cars = Cars(gif_files)


screen.tracer(0)

car = Turtle()
car.shape(gif_files[8])
car.penup()
car.setheading(90)
car.goto(0,-250)
screen.tracer(1)

go_r=False
go_l=False

def go_right():
    global go_r
    go_r=True
def go_left():
    global go_l
    go_l = True

def stop_right():
    global go_r
    go_r = False
def stop_left():
    global go_l
    go_l = False





screen.listen()

screen.onkeypress(fun=go_right,key="d")
screen.onkeyrelease(fun = stop_right,key="d" )
screen.onkeypress(fun=go_left,key= "a")
screen.onkeyrelease(fun = stop_left,key="a" )

screen.tracer(0)
cars.create_rand_cars()
screen.tracer(1)

n = 0

def game():


   global n
   road.move()
   #=============================
   screen.tracer(0)
   #================================
   for k in cars.moving_cars:
       k.forward(6)
   global go_r,go_l
   if go_r and car.xcor()<250:
       car.goto(car.xcor() + 6, car.ycor())
   if go_l and car.xcor()>-250:
       car.goto(car.xcor() - 6, car.ycor())
    #==========================================
   screen.tracer(1)
   #=====================================

   screen.tracer(0)
   # =======================================================

   for cr in cars.moving_cars:
       if abs(cr.xcor() - car.xcor()) < 25 and abs(cr.ycor() - car.ycor()) < 55:
           # turtle.bye()
           return
       if cr.ycor()<-400:

           cars.moving_cars.remove(cr)
           del cr
   #         ==================================================
   n += 1
   if n > 60:

       cars.create_rand_cars()

       n = 0
   screen.tracer(1)
   screen.ontimer(game,15)
game()




screen.exitonclick()