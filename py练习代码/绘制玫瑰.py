
import turtle
import math

# 设置画布
turtle.bgcolor("white")
turtle.title("艳丽玫瑰花")

# 创建画笔
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

# 绘制渐变色玫瑰花瓣
a = 180  # 花瓣大小
k = 6    # 花瓣数
num_loops = 5  # 圈数

def get_color(theta):
    # 生成渐变色（红-紫-粉-橙-黄）
    from colorsys import hsv_to_rgb
    h = (theta % 360) / 360.0
    r, g, b = hsv_to_rgb(h, 0.8, 1)
    return (r, g, b)

turtle.colormode(1.0)
pen.up()
for theta in range(0, 360 * num_loops + 1):
    rad = math.radians(theta)
    r = a * math.sin(k * rad)
    x = r * math.cos(rad)
    y = r * math.sin(rad)
    pen.pencolor(get_color(theta))
    if theta == 0:
        pen.goto(x, y)
        pen.down()
    else:
        pen.goto(x, y)

# 绘制绿色花茎
pen.up()
pen.goto(0, 0)
pen.seth(-90)
pen.pensize(8)
pen.pencolor("#228B22")
pen.down()
pen.forward(220)

pen.hideturtle()
turtle.done()
