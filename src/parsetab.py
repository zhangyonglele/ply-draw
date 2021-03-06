
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULDIVrightUMINUSCOLOR COMMA COMMENT CONSTNUMBER DIV DRAW ERRTOKEN FOR FROM FUNC ID IS LBRACKET MINUS MUL NONTOKEN ORIGIN PI PLUS POWER QUIT RBRACKET ROT SCALE SEMICO SIZE STEP T TOstatement : Tstatement : expressionstatement : QUITstatement : ORIGIN IS LBRACKET expression COMMA expression RBRACKETstatement : SCALE IS LBRACKET expression COMMA expression RBRACKETstatement : ROT IS expressionstatement : FOR T FROM expression TO expression STEP expressionstatement : DRAW LBRACKET expression COMMA expression RBRACKETexpression : PIexpression : CONSTNUMBERexpression : Texpression : LBRACKET expression RBRACKETexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression MUL expression\n                  | expression DIV expressionexpression : MINUS expression %prec UMINUSexpression : expression POWER expressionexpression : FUNC LBRACKET expression RBRACKET'
    
_lr_action_items = {'T':([0,6,9,13,15,16,17,18,19,24,26,28,34,36,38,44,46,47,48,56,],[2,22,25,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'QUIT':([0,],[4,]),'ORIGIN':([0,],[5,]),'SCALE':([0,],[7,]),'ROT':([0,],[8,]),'FOR':([0,],[9,]),'DRAW':([0,],[10,]),'PI':([0,6,13,15,16,17,18,19,24,26,28,34,36,38,44,46,47,48,56,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'CONSTNUMBER':([0,6,13,15,16,17,18,19,24,26,28,34,36,38,44,46,47,48,56,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'LBRACKET':([0,6,10,13,14,15,16,17,18,19,20,23,24,26,28,34,36,38,44,46,47,48,56,],[6,6,26,6,28,6,6,6,6,6,34,36,6,6,6,6,6,6,6,6,6,6,6,]),'MINUS':([0,2,3,6,11,12,13,15,16,17,18,19,21,22,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,56,57,],[13,-11,16,13,-9,-10,13,13,13,13,13,13,16,-11,13,13,-17,13,-13,-14,-15,-16,16,13,-12,13,16,13,16,16,16,16,16,13,-19,13,13,13,16,16,16,16,13,16,]),'FUNC':([0,6,13,15,16,17,18,19,24,26,28,34,36,38,44,46,47,48,56,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'$end':([1,2,3,4,11,12,22,27,29,30,31,32,33,35,37,45,53,54,55,57,],[0,-1,-2,-3,-9,-10,-11,-17,-13,-14,-15,-16,-18,-12,-6,-19,-8,-4,-5,-7,]),'PLUS':([2,3,11,12,21,22,27,29,30,31,32,33,35,37,39,40,41,42,43,45,49,50,51,52,57,],[-11,15,-9,-10,15,-11,-17,-13,-14,-15,-16,15,-12,15,15,15,15,15,15,-19,15,15,15,15,15,]),'MUL':([2,3,11,12,21,22,27,29,30,31,32,33,35,37,39,40,41,42,43,45,49,50,51,52,57,],[-11,17,-9,-10,17,-11,-17,17,17,-15,-16,17,-12,17,17,17,17,17,17,-19,17,17,17,17,17,]),'DIV':([2,3,11,12,21,22,27,29,30,31,32,33,35,37,39,40,41,42,43,45,49,50,51,52,57,],[-11,18,-9,-10,18,-11,-17,18,18,-15,-16,18,-12,18,18,18,18,18,18,-19,18,18,18,18,18,]),'POWER':([2,3,11,12,21,22,27,29,30,31,32,33,35,37,39,40,41,42,43,45,49,50,51,52,57,],[-11,19,-9,-10,19,-11,-17,-13,-14,-15,-16,19,-12,19,19,19,19,19,19,-19,19,19,19,19,19,]),'IS':([5,7,8,],[20,23,24,]),'RBRACKET':([11,12,21,22,27,29,30,31,32,33,35,40,45,49,50,51,],[-9,-10,35,-11,-17,-13,-14,-15,-16,-18,-12,45,-19,53,54,55,]),'COMMA':([11,12,22,27,29,30,31,32,33,35,39,41,42,45,],[-9,-10,-11,-17,-13,-14,-15,-16,-18,-12,44,46,47,-19,]),'TO':([11,12,22,27,29,30,31,32,33,35,43,45,],[-9,-10,-11,-17,-13,-14,-15,-16,-18,-12,48,-19,]),'STEP':([11,12,22,27,29,30,31,32,33,35,45,52,],[-9,-10,-11,-17,-13,-14,-15,-16,-18,-12,-19,56,]),'FROM':([25,],[38,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,6,13,15,16,17,18,19,24,26,28,34,36,38,44,46,47,48,56,],[3,21,27,29,30,31,32,33,37,39,40,41,42,43,49,50,51,52,57,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> T','statement',1,'p_statement_var','test.py',40),
  ('statement -> expression','statement',1,'p_statement_exp','test.py',44),
  ('statement -> QUIT','statement',1,'p_statement_quit','test.py',47),
  ('statement -> ORIGIN IS LBRACKET expression COMMA expression RBRACKET','statement',7,'p_statement_origin','test.py',52),
  ('statement -> SCALE IS LBRACKET expression COMMA expression RBRACKET','statement',7,'p_statement_scale','test.py',57),
  ('statement -> ROT IS expression','statement',3,'p_statement_rot','test.py',62),
  ('statement -> FOR T FROM expression TO expression STEP expression','statement',8,'p_statement_draw','test.py',67),
  ('statement -> DRAW LBRACKET expression COMMA expression RBRACKET','statement',6,'p_statement_drawp','test.py',76),
  ('expression -> PI','expression',1,'p_expression_const','test.py',93),
  ('expression -> CONSTNUMBER','expression',1,'p_expression_number','test.py',97),
  ('expression -> T','expression',1,'p_expression_var','test.py',101),
  ('expression -> LBRACKET expression RBRACKET','expression',3,'p_expression_bucket','test.py',105),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','test.py',109),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','test.py',110),
  ('expression -> expression MUL expression','expression',3,'p_expression_binop','test.py',111),
  ('expression -> expression DIV expression','expression',3,'p_expression_binop','test.py',112),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','test.py',123),
  ('expression -> expression POWER expression','expression',3,'p_expression_pow','test.py',128),
  ('expression -> FUNC LBRACKET expression RBRACKET','expression',4,'p_expression_funx','test.py',132),
]
