from cmu_112_graphics import *


def redrawAll(app,canvas):
    canvas.create_line(400,0,0,400,fill='black')

def appStarted(app):
    pass

runApp(width=700, height=400)