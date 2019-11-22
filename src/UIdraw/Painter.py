import turtle as turtle
from module import Draw
import math

class Painter:

    ####################################################
    ## function: 绘图入口函数
    ## return: null
    ####################################################
    def paint_2(self,location_x,location_y):
        turtle.down()
        turtle.goto(location_x,location_y)
        turtle.up()

    def init_position(self,origin = Draw.OriginPoint(0,0)):
        turtle.up()
        turtle.goto(origin.x_axis_begin,origin.y_axis_begin)
    
    def to_begin(self,location_x,location_y):
        turtle.up()
        turtle.goto(location_x,location_y)
