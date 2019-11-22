from lex import lex 
import ply.yacc as yacc
from UIdraw import Painter
from module import Draw
import turtle as turtle
import math
import time

#生成词法分析表
m = lex.MyLex()
m.build()
lexer = m.lexer


###########################################################################

#生成标识符表
names = { }
names['x'] = 0
names['y'] = 0 
names['T'] = 0
names['DRAW_FLAG'] = 0

#生成原点和图型对象
draw = Draw.Draw()
origin = Draw.OriginPoint()
painter = Painter.Painter()
#获取生成的token
tokens = lex.MyLex().tokens

#####################
#词法分析单元

precedence = (
    ('left','PLUS','MINUS'),
    ('left','MUL','DIV'),
    ('right','UMINUS'),
    )

def p_statement_var(t):
    'statement : T'
    names['T'] = 0

def p_statement_exp(t):
    'statement : expression'

def p_statement_quit(t):
    'statement : QUIT'
    quit()


def p_statement_origin(t):
    '''statement : ORIGIN IS LBRACKET expression COMMA expression RBRACKET'''
    origin.x_axis_begin = t[4]
    origin.y_axis_begin = t[6]

def p_statement_scale(t):
    'statement : SCALE IS LBRACKET expression COMMA expression RBRACKET'
    draw.x_scale = t[4]
    draw.y_scale = t[6]

def p_statement_rot(t):
    'statement : ROT IS expression'
    draw.rot = t[3]
    print('ROT is',draw.rot)

def p_statement_draw(t):
    'statement : FOR T FROM expression TO expression STEP expression'
    draw.val_origin = t[4]
    draw.val_final = t[6]
    draw.step = t[8]
    names['T'] = draw.val_origin
    names['DRAW_FLAG'] = 5
    
    
def p_statement_drawp(t):
    'statement : DRAW LBRACKET expression COMMA expression RBRACKET'
    print("t[3]=",t[3],"t[5]=",t[5])
    if (names['T'] == draw.val_origin):
        a = 'there is nothin you can find, hello boy'
        painter.to_begin(t[3] * draw.x_scale * math.cos(draw.rot) +
                        t[5] * draw.y_scale * math.sin(draw.rot) + origin.x_axis_begin
                    ,   t[5] * draw.y_scale * math.cos(draw.rot) - 
                        t[3] * draw.x_scale * math.sin(draw.rot) + origin.y_axis_begin)
    else :
        painter.paint_2(t[3] * draw.x_scale * math.cos(draw.rot) +
                        t[5] * draw.y_scale * math.sin(draw.rot) + origin.x_axis_begin
                    ,   t[5] * draw.y_scale * math.cos(draw.rot) - 
                        t[3] * draw.x_scale * math.sin(draw.rot) + origin.y_axis_begin)

#########################################################################

def p_expression_const(t):
    'expression : PI'
    t[0] = math.pi

def p_expression_number(t):
    'expression : CONSTNUMBER'
    t[0] = t[1]

def p_expression_var(t):
    'expression : T'
    t[0] = names['T']

def p_expression_bucket(t):
    'expression : LBRACKET expression RBRACKET'
    t[0] = t[2]

def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MUL expression
                  | expression DIV expression'''
    if t[2] == '+'  : 
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*': 
        t[0] = t[1] * t[3]
    elif t[2] == '/': 
        t[0] = t[1] / t[3]

def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]


def p_expression_pow(t):
    'expression : expression POWER expression'
    t[0] = pow(t[1],t[3])

def p_expression_funx(t):
    'expression : FUNC LBRACKET expression RBRACKET'
    if t[1] == 'COS':
        t[0] = math.cos(t[3])
    elif t[1] == 'SIN':
        t[0] = math.sin(t[3])
    elif t[1] == 'TAN':
        t[0] = math.tan(t[3])






###########################################################################
#生成词法分析表
parser = yacc.yacc()

while True:
    try:
        s = input('var > ')   # Use raw_input on Python 2
    except EOFError:
        break
    if names['DRAW_FLAG'] < 1:
        parser.parse(s)
    else :
        begin = draw.val_origin 
        painter.init_position(origin)
        while begin < draw.val_final:
            parser.parse(s)
            print(begin)
            begin += draw.step
            names['T'] += draw.step
        names['DRAW_FLAG'] = 0
        print("DRAW_FLAG turns to ",names['DRAW_FLAG'])




'''测试代码：
ROT IS PI/4
FOR T FROM 0 TO 100 STEP 1
DRAW (0,T)'''



#流程：
#STEP1:首先词法分析
#STEP2:然后语法分析
#       其中，先根据分析结果生成Draw对象和OriginPoint对象
#       然后根据结果画图
