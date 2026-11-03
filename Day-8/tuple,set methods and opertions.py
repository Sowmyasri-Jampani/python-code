Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[12,34,67,94,34,4,,32]
SyntaxError: invalid syntax
>>> l=[12,34,67,94,34,4,8,32]
>>> l
[12, 34, 67, 94, 34, 4, 8, 32]
>>> l.pop
<built-in method pop of list object at 0x000001AC957A6F40>
>>> l.pop()
32
>>> l.pop()
8
>>> l.pop()
4
>>> l.pop(0)
12
>>> l.pop(4)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    l.pop(4)
IndexError: pop index out of range
>>> l.pop(3)
34
>>> l
[34, 67, 94]
>>> l.remove(2)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    l.remove(2)
ValueError: list.remove(x): x not in list
>>> l.remove(94)
>>> l
[34, 67]
>>> dell[1]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    dell[1]
NameError: name 'dell' is not defined
>>> del l[1]
>>> l
[34]
>>> l.clear()
>>> l
[]
>>> l=[12,34,67,94,34,4,8,32]
>>> l.count(34)
2
>>> l.index(94)
3
>>> sorted(l)
[4, 8, 12, 32, 34, 34, 67, 94]
>>> l
[12, 34, 67, 94, 34, 4, 8, 32]
>>> l.sort()
>>> l
[4, 8, 12, 32, 34, 34, 67, 94]
>>> l.reverse()
>>> l
[94, 67, 34, 34, 32, 12, 8, 4]
>>> l.reverse=True)
SyntaxError: unmatched ')'
>>> l.sort(reverse=True)
>>> l
[94, 67, 34, 34, 32, 12, 8, 4]
>>> a=[1,2]
>>> c=a
>>> c
[1, 2]
>>> a is c
True
>>> c.append(3)
>>> c
[1, 2, 3]
>>> c.append(24)
>>> c
[1, 2, 3, 24]
>>> a
[1, 2, 3, 24]
>>> #0 0.0 ''[] () {} false
>>> l
[94, 67, 34, 34, 32, 12, 8, 4]
>>> any(l)
True
>>> all(l)
True
>>> l.append(0)
>>> l
[94, 67, 34, 34, 32, 12, 8, 4, 0]
>>> any(l)
True
>>> all(l)
False
>>> k=[0,0.0,'']
>>> any(k)
False
>>> all(l)
False
>>> k.append(l)
>>> k
[0, 0.0, '', [94, 67, 34, 34, 32, 12, 8, 4, 0]]
>>> any(k)
True
>>> all(k)
False
>>> l
[94, 67, 34, 34, 32, 12, 8, 4, 0]
>>> sum(l)
285
>>> #tuple
>>> #immutable orderd allowdulplicates heterogenous fixedsize
>>> t=()
>>> t=tuple()
>>> t=
SyntaxError: invalid syntax
>>> t=
SyntaxError: invalid syntax
>>> t=(1,2,3)
>>> t=tuple((1,2,3,4))
>>> t
(1, 2, 3, 4)
>>> type(t)
<class 'tuple'>
>>> t=1,2,3,4,5
>>> t
(1, 2, 3, 4, 5)
>>> t=(1)
>>> t
1
>>> t=(1,)
>>> t
(1,)
>>> t
(1,)
>>> t=(1,2,3,4,1,1,1,1)
>>> t
(1, 2, 3, 4, 1, 1, 1, 1)
>>> t=(1,1.1,'gju',[1,2,3],{1,2,3},(1,2),{1:1},false)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    t=(1,1.1,'gju',[1,2,3],{1,2,3},(1,2),{1:1},false)
NameError: name 'false' is not defined
>>> 
KeyboardInterrupt
>>> t=(1,1.1,'gju',[1,2,3],{1,2,3},(1,2),{1:1},False)
>>> T
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    T
NameError: name 'T' is not defined
>>> t
(1, 1.1, 'gju', [1, 2, 3], {1, 2, 3}, (1, 2), {1: 1}, False)
>>> #properties
>>> t=(1,2,3,4)
>>> t
(1, 2, 3, 4)
>>> a,b,c,d=t
>>> a
1
>>> b
2
>>> c
3
>>> d
4
>>> a,b,c=(1,2,3,4,5,5,6)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    a,b,c=(1,2,3,4,5,5,6)
ValueError: too many values to unpack (expected 3)
>>> a,b,c=(1,2,3)
>>> a
1
>>> a
1
>>> b
2
>>> c
3
>>> t
(1, 2, 3, 4)
>>> t=t=(1,1.1,'hjkl',[1,2,3],{1,2,3},(1,2),{1:1},False)
>>> len(t)
8
>>> t[3]
[1, 2, 3]
>>> t[3].append(1)
>>> t
(1, 1.1, 'hjkl', [1, 2, 3, 1], {1, 2, 3}, (1, 2), {1: 1}, False)
>>> #tuple operations
>>> a=(1,2,3,4,5)
>>> b=(7,8,9)
>>> a+b
(1, 2, 3, 4, 5, 7, 8, 9)
>>> a*2
(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
>>> a
(1, 2, 3, 4, 5)
>>> t
(1, 1.1, 'hjkl', [1, 2, 3, 1], {1, 2, 3}, (1, 2), {1: 1}, False)
>>> t[2]
'hjkl'
>>> t[-1]
False
>>> t[1:3]
(1.1, 'hjkl')
>>> t[::-4]
(False, [1, 2, 3, 1])
>>> t[:-4]
(1, 1.1, 'hjkl', [1, 2, 3, 1])
>>> 1 in t
True
>>> 10 not in t
True
>>> t[-2:]
({1: 1}, False)
>>> False not in t
False
>>> #tuple methods
>>> t
(1, 1.1, 'hjkl', [1, 2, 3, 1], {1, 2, 3}, (1, 2), {1: 1}, False)
>>> t=(94, 67, 34, 34, 32, 12, 8, 4, 25)
>>> t
(94, 67, 34, 34, 32, 12, 8, 4, 25)
>>> len(t)
9
>>> sorted(t)
[4, 8, 12, 25, 32, 34, 34, 67, 94]
>>> max(t)
94
>>> min(t)
4
>>> t.count(34)
2
>>> t.count(4)
1
>>> any(t)
True
>>> all(t)
True
>>> t
(94, 67, 34, 34, 32, 12, 8, 4, 25)
>>> sum(t)
310
>>> #set
>>> s={}
>>> type(s)
<class 'dict'>
>>> s=set()
>>> s={1,2,3,4}
>>> type(s)
<class 'set'>
>>> #unordered uniquevalues mutable heterogenous dynamicallysized-properties
>>> s={90,8,23,89,3,1,4}
>>> s
{1, 3, 4, 23, 8, 89, 90}
>>> s={1,1,1,1,1}
>>> s
{1}
>>> s=1,2,3,4
>>> s
(1, 2, 3, 4)
>>> s=12.4,3.4
>>> s
(12.4, 3.4)
>>> s=(3+4j)
>>> s
(3+4j)
>>> s=[1,2,3,4]
>>> s
[1, 2, 3, 4]
>>> s.add(1)
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    s.add(1)
AttributeError: 'list' object has no attribute 'add'
>>> s=set(1)
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    s=set(1)
TypeError: 'int' object is not iterable
>>> s.add(2+3j)
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    s.add(2+3j)
AttributeError: 'list' object has no attribute 'add'
>>> s
[1, 2, 3, 4]
>>> s={}
>>> s
{}
>>> s.add(1)
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    s.add(1)
AttributeError: 'dict' object has no attribute 'add'
>>> s={1,2,3}
>>> s
{1, 2, 3}
>>> s={23,4,1,56,66,98,3}
>>> s
{1, 66, 3, 4, 98, 23, 56}
>>> s={1,1,1,1,1}
>>> s
{1}
>>> s.add(1)
>>> s.add(1.3)
>>> s
{1, 1.3}
>>> s.add('sri')
>>> s
{1, 'sri', 1.3}
>>> s.add(3+9j)
>>> s
{1, (3+9j), 'sri', 1.3}
>>> s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    s.add([1,2,3])
TypeError: unhashable type: 'list'
>>> s.add((1,2,3))
>>> s
{1, 1.3, (1, 2, 3), 'sri', (3+9j)}
>>> s.add({1:1,2:2})
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    s.add({1:1,2:2})
TypeError: unhashable type: 'dict'
>>> s.add(True)
>>> s
{1, 1.3, (1, 2, 3), 'sri', (3+9j)}
>>> #set only allows immutable elements
>>> a={1,2,3,4}
>>> b={5,6,7,8}
>>> a
{1, 2, 3, 4}
>>> b
{8, 5, 6, 7}
>>> 4 in a
True
>>> 9 not in a
True
>>> a
{1, 2, 3, 4}
>>> b
{8, 5, 6, 7}
>>> a|b
{1, 2, 3, 4, 5, 6, 7, 8}
>>> a&b
set()
>>> a={1,2,3,4,5}
>>> a
{1, 2, 3, 4, 5}
>>> b
{8, 5, 6, 7}
>>> a&b
{5}
>>> a^b
{1, 2, 3, 4, 6, 7, 8}
>>> a-b
{1, 2, 3, 4}
>>> a
{1, 2, 3, 4, 5}
>>> b
{8, 5, 6, 7}
>>> a.isdisjoint(b)
False
>>> a.isdisjoint({99,100})
True
>>> a
{1, 2, 3, 4, 5}
>>> {5}.issubset(a)
True
>>> {100,99}.issubset(a)
False
>>> a.issubset(b)
False
>>> {1,2,3,4,5,6,7,8}.issuperset(a)
True
>>> 