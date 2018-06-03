Listas []

Python 3.5.2+ (default, Sep 22 2016, 12:18:14) 
[GCC 6.2.0 20160914] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = [1,2,3]
>>> type(a)
<class 'list'>
>>> help(list)

>>> a
[1, 2, 3]
>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> a
[1, 2, 3]
>>> a.append(4)
>>> a
[1, 2, 3, 4]
>>> b = a.copy()
>>> b
[1, 2, 3, 4]
>>> c = a
>>> c
[1, 2, 3, 4]
>>> a
[1, 2, 3, 4]
>>> a.append(1)
>>> a.count(1)
2
>>> a,b
([1, 2, 3, 4, 1], [1, 2, 3, 4])
>>> b = ['um', 'dois', 'tres']
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 1, 'um', 'dois', 'tres']
>>> a = [1,2,3,4]
>>> a.append(b)
>>> a
[1, 2, 3, 4, ['um', 'dois', 'tres']]
>>> a.index(4)
3
>>> a
[1, 2, 3, 4, ['um', 'dois', 'tres']]
>>> a.insert(3, 'Novo valor')
>>> a
[1, 2, 3, 'Novo valor', 4, ['um', 'dois', 'tres']]
>>> a.pop()
['um', 'dois', 'tres']
>>> a
[1, 2, 3, 'Novo valor', 4]
>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> a
[1, 2, 3, 'Novo valor', 4]
>>> a.remove('Novo valor')
>>> a
[1, 2, 3, 4]
>>> c = a.remove(4)
>>> c
>>> a
[1, 2, 3]
>>> a.reverse()
>>> a
[3, 2, 1]
>>> a.sort()
>>> a
[1, 2, 3]
>>> b = ['c', 'd', 'b', 'a']
>>> b
['c', 'd', 'b', 'a']
>>> b.sort()
>>> b
['a', 'b', 'c', 'd']
>>> b.clear()
>>> b
[]
>>> a
[1, 2, 3]
>>> c
>>> b
[]
>>> a
[1, 2, 3]
>>> l
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'l' is not defined
>>> a
[1, 2, 3]
>>> for i in a:
...    print(i)
... 
1
2
3
>>> a[0]
1
>>> a[1]
2
>>> a[10]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> len(a)
3
>>> a
[1, 2, 3]
