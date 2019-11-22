import ply.lex as lex


class MyLex:
    #这里通过py的反射机制，获取我创建的各个变量标识符
    tokens = ('COMMENT', 'ID', 'ORIGIN', 'SCALE', 'ROT', 'IS', 'TO', 'STEP',
              'DRAW', 'FOR', 'FROM', 'T', 'COLOR', 'SIZE', 'SEMICO',
              'LBRACKET', 'RBRACKET', 'COMMA', 'PLUS', 'MINUS', 'MUL', 'DIV',
              'POWER', 'FUNC', 'CONSTNUMBER', 'NONTOKEN', 'ERRTOKEN','PI','QUIT')

    #t_COMMENT  = r'//|--'  ##注释标记
    #t_ID      = r''
    t_ORIGIN   = r'ORIGIN'          ##用于设置原点偏移量
    t_SCALE    = r'SCALE'           ##设置横纵坐标比例
    t_ROT      = r'ROT'             ## 设置旋转角度
    t_IS       = r'IS'              ##关键字:是
    t_TO       = r'TO'              ##保留关键字
    t_STEP     = r'STEP'            ##步长
    t_DRAW     = r'DRAW'            ##画图关键字
    t_FOR      = r'FOR'             ##For循环
    t_FROM     = r'FROM'            ##FROM关键字
    t_T        = r'T'               ##变量识别
    t_COLOR    = r'COLOR'           ##没用
    t_SIZE     = r'SIZE'            ##没用
    t_SEMICO   = r';'               ##没用
    t_LBRACKET = r'\('              ##左括号
    t_RBRACKET = r'\)'              ##右括号
    t_COMMA    = r','               ##逗号
    t_PLUS     = r'\+'              ##加号
    t_MINUS    = r'-'               ##减号
    t_MUL      = r'\*'              ##乘号
    t_DIV      = r'/'               ##除号
    t_POWER    = r'POW'             ##没用
    t_FUNC     = r'TAN|COS|SIN'     ##函数识别
    t_PI       = r'PI'              ##PI常量
    t_QUIT     = r'QUIT'            ##退出关键字

    t_ignore = " \t"
    
    ##注释
    def t_COMMENT(self,t):
        r"(//|--).*"
        pass
    
    ##字面量
    def t_CONSTNUMBER(self,t):
        r'\d+'
        try:
            t.value = float(t.value)
        except ValueError:
            print("number value too large %d", t.value)
            t.value = 0
        return t

    ##新一行
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

    ##错误处理
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    ##创建字符表
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok: break
            print(tok)