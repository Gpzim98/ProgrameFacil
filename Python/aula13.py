Tuplas ()

>>> a = 10
>>> a[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not subscriptable
>>> b = 1,2,3,4
>>> type(b)
<class 'tuple'>
>>> c = (1,2,3)
>>> type(c)
<class 'tuple'>
>>> b = 1,2,3,4,('asdf',2,'a'), 1.2,'asd'
>>> type(b)
<class 'tuple'>
>>> b
(1, 2, 3, 4, ('asdf', 2, 'a'), 1.2, 'asd')
>>> b[0]
1
>>> b[4]
('asdf', 2, 'a')
>>> b[4][0]
'asdf'
>>> dir(b)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> b = (2,2,3,4,'asd', (1,2), 'asd')
>>> b.count('asd')
2
>>> b.index((1,2))
5
>>> b.count('asda')
0
>>> b.index((1,2,2))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: tuple.index(x): x not in tuple
>>> if b.count('asda'):
...    print(b[b.index('asda')])
... 
>>> if b.count('asd'):
...    print(b[b.index('asd')])
... 
asd
>>> for i in b:
...    print(i)
... 
2
2
3
4
asd
(1, 2)
asd

>>> i = 0
>>> while i < len(b):
...    print(b[i])
...    i = i+1
... 
2
2
3
4
asd
(1, 2)
asd
