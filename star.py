import turtle

from pyparsing import col

t=turtle.Turtle()
s=turtle.Screen()
t.speed(10)

s.bgcolor("black")

col=("blue","yellow","red","white")
c=0

for i in range (50):
    t.forward(i*10)
    t.right(144)
    t.color(col[c])
    if c==3:
        c=0
    else:
        c+=1