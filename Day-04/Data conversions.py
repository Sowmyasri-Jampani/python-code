Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> int(a)
10
>>> float(a)
10.0
>>> complex(a)
(10+0j)
>>> str(a)
'10'
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
>>> bool(a)
True
>>> b=10.2
>>> int(b)
10
>>> complex(b)
(10.2+0j)
>>> list(b)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
>>> tuple(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
>>> set(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
>>> dict(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
>>> str(b)
'10.2'
>>> bool(b)
True
>>> c=10.3+1j
>>> int(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(c)
TypeError: can't convert complex to int
>>> float(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    float(c)
TypeError: can't convert complex to float
>>> list(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
>>> tuple(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
>>> set(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
>>> dict(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
>>> bool(c)
True
>>> d="codegnan"
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int(d)
ValueError: invalid literal for int() with base 10: 'codegnan'
>>> float(d)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    float(d)
ValueError: could not convert string to float: 'codegnan'
>>> complex(d)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    complex(d)
ValueError: complex() arg is a malformed string
>>> list(d)
['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
>>> tuple(d)
('c', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
>>> set(d)
{'e', 'c', 'o', 'd', 'g', 'a', 'n'}
>>> dict(d)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    dict(d)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> bool(d)
True
>>> l=[1,2,3,4]
>>> int(l)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> int(l)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> float(l)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a number, not 'list'
>>> complex(l)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
>>> tuple(l)
(1, 2, 3, 4)
>>> set(l)
{1, 2, 3, 4}
>>> dict(l)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(l)
True
>>> str(l)
'[1, 2, 3, 4]'
>>> t=(1,2,3)
>>> int(t)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'tuple'
>>> float(t)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a number, not 'tuple'
>>> complex(t)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
>>> str(t)
'(1, 2, 3)'
>>> list(t)
[1, 2, 3]
>>> set(t)
{1, 2, 3}
>>> dict(t)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(t)
True
>>> s={1,2,3}
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'set'
>>> float(s)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a number, not 'set'
>>> complex(s)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'set'
>>> str(s)
'{1, 2, 3}'
>>> list(s)
[1, 2, 3]
>>> tuple(s)
(1, 2, 3)
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    dict(s)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(s)
True
>>> e={1:2,3:4,5:6}
>>> int(e)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    int(e)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'dict'
>>> float(e)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    float(e)
TypeError: float() argument must be a string or a number, not 'dict'
>>> complex(e)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    complex(e)
TypeError: complex() first argument must be a string or a number, not 'dict'
>>> str(e)
'{1: 2, 3: 4, 5: 6}'
>>> list(e)
[1, 3, 5]
>>> tuple(e)
(1, 3, 5)
>>> set(e)
{1, 3, 5}
>>> bool(e)
True
>>> g=8
>>> g
8
>>> 