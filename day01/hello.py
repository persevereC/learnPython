'''
print('hello python1')
print('hello python2')
print('hello python3')
import sys
print(sys.version_info)

'''

from turtle import*


def nose(x,y):#鼻子
    penup()#提起笔
    goto(x,y)#定位
    pendown()#落笔，开始画
    setheading(-30)#将乌龟的方向设置为to_angle/为数字（0-东、90-北、180-西、270-南）
    begin_fill()#准备开始填充图形
    a=0.4
    for i in range(120):
        if 0<=i<30 or 60<=i<90:
            a=a+0.08
            left(3) #向左转3度
            forward(a) #向前走a的步长
        else:
            a=a-0.08
            left(3)
            forward(a)
    end_fill()#填充完成

    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    pendown()
    pencolor(255,155,192)#画笔颜色
    setheading(10)
    begin_fill()
    circle(5)
    color(160,82,45)#返回或设置pencolor和fillcolor
    end_fill()

    penup()
    setheading(0)
    forward(20)
    pendown()
    pencolor(255,155,192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160,82,45)
    end_fill()


def head(x,y):#头
    color((255,155,192),"pink")
    penup()
    goto(x,y)
    setheading(0)
    pendown()
    begin_fill()
    setheading(180)
    circle(300,-30)
    circle(100,-60)
    circle(80,-100)
    circle(150,-20)
    circle(60,-95)
    setheading(161)
    circle(-300,15)
    penup()
    goto(-100,100)
    pendown()
    setheading(-30)
    a=0.4
    for i in range(60):
        if 0<=i<30 or 60<=i<90:
            a=a+0.08
            lt(3) #向左转3度
            fd(a) #向前走a的步长
        else:
            a=a-0.08
            lt(3)
            fd(a)
    end_fill()


def ears(x,y): #耳朵
    color((255,155,192),"pink")
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50,50)
    circle(-10,120)
    circle(-50,54)
    end_fill()

    penup()
    setheading(90)
    forward(-12)
    setheading(0)
    forward(30)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50,50)
    circle(-10,120)
    circle(-50,56)
    end_fill()


def eyes(x,y):#眼睛
    color((255,155,192),"white")
    penup()
    setheading(90)
    forward(-20)
    setheading(0)
    forward(-95)
    pendown()
    begin_fill()
    circle(15)
    end_fill()

    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()

    color((255,155,192),"white")
    penup()
    seth(90)
    forward(-25)
    seth(0)
    forward(40)
    pendown()
    begin_fill()
    circle(15)
    end_fill()

    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()


def cheek(x,y):#腮
    color((255,155,192))
    penup()
    goto(x,y)
    pendown()
    setheading(0)
    begin_fill()
    circle(30)
    end_fill()


def mouth(x,y): #嘴
    color(239,69,19)
    penup()
    goto(x,y)
    pendown()
    setheading(-80)
    circle(30,40)
    circle(40,80)


def setting():          #参数设置
    pensize(4)
    hideturtle()        #使乌龟无形（隐藏）
    colormode(255)      #将其设置为1.0或255.随后 颜色三元组的r，g，b值必须在0 .. cmode范围内
    color((255,155,192),"pink")
    setup(840,500)
    speed(10)


def main():
    setting()           #画布、画笔设置
    nose(-100,100)      #鼻子
    head(-69,167)       #头
    ears(0,160)         #耳朵
    eyes(0,140)         #眼睛
    cheek(80,10)        #腮
    mouth(-20,30)       #嘴
    done()


if __name__ == '__main__':
	main()

'''

Python的优点:。
  简单和明确，做一件事只有一种方法。
  学习曲线低，与其他很多语言比上手更容易。
  开放源代码，拥有强大的社区和生态圈。
  解释型语言，完美的平台可移植性。
  支持两种主流的编程范式，可以使用面向对象和函数式编程。
  可扩展性和可嵌入性，可以调用C/C++代码也可以在C/C++中调用。
  代码规范程度高，可读性强，适合有代码洁癖和强迫症的人群。

Python的缺点:
  执行效率低下，因此计算密集型任务可以由C/C++编写。
  代码无法加密，但是现在的公司很多都不是卖软件而是卖服务，这个问题慢慢会淡化。
  在开发时可以选择的框架太多，有选择的地方就有错误。

Python的应用领域:
  目前Python在云基础设施、DevOps、网络爬虫开发、数据分析挖掘、机器学习等领域都有着广泛的应用，
  因此也产生了服务器开发、数据接口开发、自动化运维、科学计算和数据可视化、聊天机器人开发、图像识别和处理等一系列的职位

'''