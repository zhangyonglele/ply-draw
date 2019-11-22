import math as math

class Draw:

    #启动画图变量迭代位置
    val_origin = 0.0
    #启动画图变量迭代终点
    val_final = 0.0

    #定义旋转角度
    rot = 0

    #定义x放大倍数
    x_scale = 0
    #定义y放大倍数
    y_scale = 0

    #定义步长
    step = 0.0

    #变量x启用的函数类型(数字即为常量型)
    x_func_type = 'liner'
    #变量y启用的函数类型
    y_func_type = 'liner'

    def __init__(self,val_origin = 0,val_final = 0,
                    rot = 0,x_scale = 1,y_scale = 1,step = 1,
                    x_func_type = 'liner',y_func_type = 'liner'):
        self.val_origin = val_origin
        self.val_final = val_final
        self.rot = rot
        self.x_scale = x_scale
        self.y_scale = y_scale
        self.step = step
        self.x_func_type = x_func_type
        self.y_func_type = y_func_type 


class OriginPoint:
    #定义横坐标位置
    x_axis_begin = 0.0
    #定义纵坐标位置
    y_axis_begin = 0.0

    def __init__(self,x_axis_begin = 0,y_axis_begin = 0):
        self.x_axis_begin = x_axis_begin
        self.y_axis_begin = y_axis_begin

