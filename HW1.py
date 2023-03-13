Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle
>>> tao.pen()
{'shown': True, 'pendown': True, 'pencolor': 'black', 'fillcolor': 'black', 'pensize': 1, 'speed': 3, 'resizemode': 'noresize', 'stretchfactor': (1.0, 1.0), 'shearfactor': 0.0, 'outline': 1, 'tilt': 0.0}
>>> tao.bgcolor('#151B54')
>>> tao.color('#3090C7')
>>> tao.pensize(7)
>>> tao.penup()
>>> tao.pendown()
>>> for i in range(8):
...     tao.left(45)
...     tao.circle(200,180)
... 
...     
>>> 
>>> tao.penup()
>>> tao.goto(-400,0)
>>> tao.pendown()
>>> for i in range(8):
...     tao.left(45)
...     tao.circle(200,180)
... 
...     
>>> tao.penup()
>>> tao.goto(400,0)
>>> tao.pendown()
>>> for i in range(8):
...     tao.left(45)
...     tao.circle(200,180)
... 
...     
>>> tao.penup()
>>> tao.goto(0,400)
>>> tao.goto(0,-400)
>>> tao.pendown()
>>> for i in range(8):
...     tao.left(45)
...     tao.circle(200,180)
... 
...     
>>> tao.penup()
>>> tao.goto(-400,-400)
>>> tao.pendown()
>>> for i in range(8):
...     tao.left(45)
...     tao.circle(200,180)
... 
...     
>>> tao.penup()
>>> tao.goto(400,-400)
>>> tao.pendown()
>>> for i in range(8):
...     tao.left(45)
...     tao.circle(200,180)
... 
...     
