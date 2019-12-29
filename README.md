# ply-draw
该项目简单编写了一个用于画图的程序，使用ply库来进行语法和词法分析，由于使用不熟练和对python的不了解，现在程序有很多bug，有机会以后再进行修改纠正。

## Quick Start
需要首先引入依赖：
```
pip install ply
```

启动test.py脚本，正常启动后显示：
```
var >
```
等待用户输入。


简单测试用例：
```
ORIGIN IS (0,0) //设置原点位置
ROT IS PI/4     //设置旋转角度(逆时针)
FOR T FROM 0 TO 100 STEP 1   //设置画图循环,t从0到100，步长为1
DRAW (0,T)   //画图


FOR T FROM 0 TO 2*PI STEP PI/50
DRAW (COS(T),SIN(T)) //画圆形

FOR T FROM -10 TO 10 STEP 1/5
DRAW (T*T,T)  //画二次函数

```

## 词法分析(lexical analysis)
该项目使用ply库中的lex部分进行编写，位于lex文件夹中。

## 语法分析(grammatical analysis)
该项目的语法分析使用ply库中的yacc部分进行编写，和程序主体共享test.py文件。

## UI部分
图型的基本数据信息在module文件夹中；画图部分使用python提供的turtle库，在UIdraw文件夹中。

## 目前支持情况
目前支持的库函数有：
```
COS()  //余弦函数
TAN()  //正切函数
SIN()  //正弦函数
QUIT   //退出程序关键字
```

目前支持的关键字及语法有
```
ORIGIN IS (expression,expression)   //定义原点坐标
ROT IS expression  //定义旋转角度
SCALE IS (expression,expression)   //定义X,Y轴的放大倍数
FOR T FROM expression TO expression STEP express  //循环，定义起始值，结束值，和循环步长
DRAW (expression,expression)   //绘图函数
```

## 程序当前问题
程序当前的循环支持并不是很好，for循环更像时先赋值，在将code block 中的程序反复编译的样子，必须要先执行for才能执行画图程序，虽然这属于编译的一种错误，但是程序的容错性和一些问题仍然能让程序继续进行下去。希望以后能进行修改，完善该程序。
