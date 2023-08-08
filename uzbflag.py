import turtle as flag

uzb = flag.Screen()
uzb.setup(1000, 600)
uzb.bgcolor('white')

text = flag.Turtle()
text.speed(0)
text.hideturtle()

def write(message, pos, color, font_size):
    x, y = pos
    text.color(color)
    text.penup()
    text.goto(x, y)
    text.pendown()
    style = ('Courier', font_size, 'bold')
    text.write(message, font=style)
write('Instagram : ABDUJALIL.DEV',(-330, 30), 'blue',40)
write('YouTube : ABDUJALIL GROUP',(-350, -30), 'blue',40)

flag.speed(4)
flag.color('white')
flag.penup()
flag.setposition(-500, 300)
flag.pendown()

hight_main = 195
width_main = 1000

def main(color):
    flag.color(color)
    flag.fillcolor(color)
    flag.begin_fill()
    flag.forward(width_main)
    flag.right(90)
    flag.forward(hight_main)
    flag.right(90)
    flag.forward(width_main)
    flag.right(180)
    flag.end_fill()

hight_mid = 10
width_mid = 1000

def middle(color):
    flag.color(color)
    flag.fillcolor(color)
    flag.begin_fill()
    flag.forward(width_mid)
    flag.right(90)
    flag.forward(hight_mid)
    flag.right(90)
    flag.forward(width_mid)
    flag.right(180)
    flag.end_fill()

main("#4169E1")
middle("#CF0921")
main("#FFFFFF")
middle("#CF0921")
main("#188637")

#moon
def moon(size):
    flag.color('white')
    flag.right(90)
    flag.penup()
    flag.goto(-435, 202.5)
    flag.pendown()
    flag.fillcolor('white')
    flag.begin_fill()
    flag.circle(size)
    flag.end_fill()

    flag.penup()
    flag.goto(-410, 202.5)
    flag.fillcolor('#4169E1')
    flag.begin_fill()
    flag.circle(size-8)
    flag.end_fill()
    flag.left(90)

moon(70)

#STAR

def star(size):
    flag.penup()
    flag.goto(-180,255)
    flag.pendown()
    for uz in range(12):
        if uz == 3:
            flag.penup()
            flag.goto(-240, 205)
            flag.pendown()
        elif uz == 7:
            flag.penup()
            flag.goto(-300, 155)
            flag.pendown()
        flag.fillcolor('white')
        flag.begin_fill()
        for uzb in range(5):
            flag.forward(size)
            flag.right(144)
        flag.end_fill()
        flag.penup()
        flag.forward(60)
        flag.pendown()

star(30)
flag.hideturtle()

list_color = ["#FFD700", "#FF69B4", "#ff0000", "#8470FF", "#888B00", "#6959CD","#808000","#FFFF00","#EE9A00"]
for uz in range(50):
    for u in range(1, 9 ):
        write('I LOVE UZBEKISTAN ♡', (-430,20), list_color[u], 40)
        write('@Abdujalil.DEV', (-370,-100), list_color[u], 60)

flag.done()

