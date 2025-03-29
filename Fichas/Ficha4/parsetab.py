
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALFANUM NUM PA PF VIRGlista : PA elementos PFlista : PA PFelementos : elementos VIRG elementoelementos : elementoelemento : NUMelemento : ALFANUM'
    
_lr_action_items = {'PA':([0,],[2,]),'$end':([1,4,8,],[0,-2,-1,]),'PF':([2,3,5,6,7,10,],[4,8,-4,-5,-6,-3,]),'NUM':([2,9,],[6,6,]),'ALFANUM':([2,9,],[7,7,]),'VIRG':([3,5,6,7,10,],[9,-4,-5,-6,-3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'lista':([0,],[1,]),'elementos':([2,],[3,]),'elemento':([2,9,],[5,10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> lista","S'",1,None,None,None),
  ('lista -> PA elementos PF','lista',3,'p_lista_elementos','Ficha4.py',36),
  ('lista -> PA PF','lista',2,'p_lista_PA_PF','Ficha4.py',40),
  ('elementos -> elementos VIRG elemento','elementos',3,'p_elementos_vir','Ficha4.py',44),
  ('elementos -> elemento','elementos',1,'p_elementos_elemento','Ficha4.py',48),
  ('elemento -> NUM','elemento',1,'p_elemento_num','Ficha4.py',53),
  ('elemento -> ALFANUM','elemento',1,'p_elemento_alfanum','Ficha4.py',58),
]
