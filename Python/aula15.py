d = {key: value, key: value, key:value}

>>> d = {'nome': 'Fulano', 'idade':18}
>>> d
{'idade': 18, 'nome': 'Fulano'}
>>> d['idade']
18
>>> d['nome']
'Fulano'
>>> d[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0
>>> d['salary'] = 5000
>>> d
{'salary': 5000, 'idade': 18, 'nome': 'Fulano'}
>>> dir(d)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> d.values()
dict_values([5000, 18, 'Fulano'])
>>> d.keys()
dict_keys(['salary', 'idade', 'nome'])
>>> dic2 = {'rua': 'rua tal', 'bairoo': 'Bairro x'}
>>> d.update(dic2)
>>> d
{'rua': 'rua tal', 'salary': 5000, 'idade': 18, 'bairoo': 'Bairro x', 'nome': 'Fulano'}
>>> dic2 = {'rua': 'rua tal', 'bairoo': 'Bairro x', 'nome': 'Ciclano'}
>>> d.update(dic2)
>>> d
{'salary': 5000, 'rua': 'rua tal', 'bairoo': 'Bairro x', 'nome': 'Ciclano', 'idade': 18}
>>> d
{'salary': 5000, 'rua': 'rua tal', 'bairoo': 'Bairro x', 'nome': 'Ciclano', 'idade': 18}
>>> d.setdefaul('Cicleno', 'Nao encontrado')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'setdefaul'
>>> d.setdefault('Cicleno', 'Nao encontrado')
'Nao encontrado'
>>> d
{'salary': 5000, 'Cicleno': 'Nao encontrado', 'rua': 'rua tal', 'bairoo': 'Bairro x', 'nome': 'Ciclano', 'idade': 18}
>>> d.setdefault('Ciclano', 'Nao encontrado')
'Nao encontrado'
>>> d
{'salary': 5000, 'Cicleno': 'Nao encontrado', 'rua': 'rua tal', 'bairoo': 'Bairro x', 'nome': 'Ciclano', 'idade': 18, 'Ciclano': 'Nao encontrado'}
>>> d.setdefault('nome', 'Nao encontrado')
'Ciclano'
>>> d.popitem('rua')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: popitem() takes no arguments (1 given)
>>> d.popitem()
('salary', 5000)
>>> d
{'Cicleno': 'Nao encontrado', 'rua': 'rua tal', 'bairoo': 'Bairro x', 'nome': 'Ciclano', 'idade': 18, 'Ciclano': 'Nao encontrado'}
>>> dir(d)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> d.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pop expected at least 1 arguments, got 0
>>> d
{'Cicleno': 'Nao encontrado', 'rua': 'rua tal', 'bairoo': 'Bairro x', 'nome': 'Ciclano', 'idade': 18, 'Ciclano': 'Nao encontrado'}
>>> d.pop('Cicleno')
'Nao encontrado'
>>> d
{'rua': 'rua tal', 'bairoo': 'Bairro x', 'nome': 'Ciclano', 'idade': 18, 'Ciclano': 'Nao encontrado'}
>>> d.keys()
dict_keys(['rua', 'bairoo', 'nome', 'idade', 'Ciclano'])
>>> d.items()
dict_items([('rua', 'rua tal'), ('bairoo', 'Bairro x'), ('nome', 'Ciclano'), ('idade', 18), ('Ciclano', 'Nao encontrado')])
>>> d.get('nome')
'Ciclano'
>>> d.get('salary')
>>> d['nome']
'Ciclano'
>>> d['salary']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'salary'
>>> d.get('salary', '404')
'404'
>>> d.get('salary', 1000)
1000
>>> help(dict.fromkeys)

>>> d.fromkeys([1,2,3], 'x')
{1: 'x', 2: 'x', 3: 'x'}
>>> d
{'rua': 'rua tal', 'bairoo': 'Bairro x', 'nome': 'Ciclano', 'idade': 18, 'Ciclano': 'Nao encontrado'}
>>> dict.fromkeys([1,2,3], 'x')
{1: 'x', 2: 'x', 3: 'x'}
>>> dir(d)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> d.copy()
{'rua': 'rua tal', 'idade': 18, 'Ciclano': 'Nao encontrado', 'bairoo': 'Bairro x', 'nome': 'Ciclano'}
>>> d
{'rua': 'rua tal', 'bairoo': 'Bairro x', 'nome': 'Ciclano', 'idade': 18, 'Ciclano': 'Nao encontrado'}
>>> d.clear()
>>> d
{}
>>> 

>>> d = {1:'um', 2:'dois'}
>>> d
{1: 'um', 2: 'dois'}
>>> for i in d:
...    print(i)
... 
1
2
>>> for i in d.ites():
...    print(i)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'ites'
>>> for i in d.items():
...    print(i)
... 
(1, 'um')
(2, 'dois')
>>> d.items()
dict_items([(1, 'um'), (2, 'dois')])
>>> for i in d.items():
...    print(i[1])
... 
um
dois
