
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftDIGITMIleftLOALPHAUPALPHAUPALPHA LOALPHA DIGIT CTL CR LF CRLF SP HT MI QUOTATION COLONmessage : message statement\n               | statement\n               statement : expression COLON expression crlf\n                  | expression SP expression crlf\n                  | expression crlf\n                  | crlf\n                  expression : expression alpha\n                  | expression DIGITexpression : expression MI expressionexpression : alpha alpha\n                  | alpha DIGIT\n                  | DIGIT\n                  alpha : LOALPHA\n            | UPALPHAcrlf : CR LF\n            | CRLF'
    
_lr_action_items = {'LF':([5,],[11,]),'DIGIT':([0,1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[1,-12,-14,-6,-2,13,1,15,-13,-16,-15,-10,-11,-1,-8,1,1,1,-5,-7,15,-9,15,-4,-3,]),'SP':([1,2,8,9,12,13,15,20,22,],[-12,-14,16,-13,-10,-11,-8,-7,-9,]),'MI':([1,2,8,9,12,13,15,20,21,22,23,],[-12,-14,17,-13,-10,-11,-8,-7,17,-9,17,]),'COLON':([1,2,8,9,12,13,15,20,22,],[-12,-14,18,-13,-10,-11,-8,-7,-9,]),'CRLF':([0,1,2,3,4,7,8,9,10,11,12,13,14,15,19,20,21,22,23,24,25,],[10,-12,-14,-6,-2,10,10,-13,-16,-15,-10,-11,-1,-8,-5,-7,10,-9,10,-4,-3,]),'UPALPHA':([0,1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[2,-12,-14,-6,-2,2,2,2,-13,-16,-15,-10,-11,-1,-8,2,2,2,-5,-7,2,2,2,-4,-3,]),'CR':([0,1,2,3,4,7,8,9,10,11,12,13,14,15,19,20,21,22,23,24,25,],[5,-12,-14,-6,-2,5,5,-13,-16,-15,-10,-11,-1,-8,-5,-7,5,-9,5,-4,-3,]),'LOALPHA':([0,1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[9,-12,-14,-6,-2,9,9,9,-13,-16,-15,-10,-11,-1,-8,9,9,9,-5,-7,9,9,9,-4,-3,]),'$end':([3,4,7,10,11,14,19,24,25,],[-6,-2,0,-16,-15,-1,-5,-4,-3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'alpha':([0,6,7,8,16,17,18,21,22,23,],[6,12,6,20,6,6,6,20,20,20,]),'message':([0,],[7,]),'expression':([0,7,16,17,18,],[8,8,21,22,23,]),'crlf':([0,7,8,21,23,],[3,3,19,24,25,]),'statement':([0,7,],[4,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> message","S'",1,None,None,None),
  ('message -> message statement','message',2,'p_message_term','tpc_analyser.py',11),
  ('message -> statement','message',1,'p_message_term','tpc_analyser.py',12),
  ('statement -> expression COLON expression crlf','statement',4,'p_statement_term','tpc_analyser.py',26),
  ('statement -> expression SP expression crlf','statement',4,'p_statement_term','tpc_analyser.py',27),
  ('statement -> expression crlf','statement',2,'p_statement_term','tpc_analyser.py',28),
  ('statement -> crlf','statement',1,'p_statement_term','tpc_analyser.py',29),
  ('expression -> expression alpha','expression',2,'p_expression_string','tpc_analyser.py',39),
  ('expression -> expression DIGIT','expression',2,'p_expression_string','tpc_analyser.py',40),
  ('expression -> expression MI expression','expression',3,'p_expression_uuid','tpc_analyser.py',44),
  ('expression -> alpha alpha','expression',2,'p_expression_term','tpc_analyser.py',48),
  ('expression -> alpha DIGIT','expression',2,'p_expression_term','tpc_analyser.py',49),
  ('expression -> DIGIT','expression',1,'p_expression_term','tpc_analyser.py',50),
  ('alpha -> LOALPHA','alpha',1,'p_alpha_term','tpc_analyser.py',58),
  ('alpha -> UPALPHA','alpha',1,'p_alpha_term','tpc_analyser.py',59),
  ('crlf -> CR LF','crlf',2,'p_crlf_term','tpc_analyser.py',63),
  ('crlf -> CRLF','crlf',1,'p_crlf_term','tpc_analyser.py',64),
]
