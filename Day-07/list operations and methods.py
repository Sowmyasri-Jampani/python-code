Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s='Python Programming'
>>> s,startswith('p')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s,startswith('p')
NameError: name 'startswith' is not defined
>>> s.startswith('p')
False
>>> s.startswith('P')
True
>>> s.startswith("Pyt")
True
>>> s.endswith("img")
False
>>> s.endswith("ing")
True
>>> 's'.islower()
True
>>> 'U'.isupper()
True
>>> 'codegnan@'.isalpha()
False
>>> 'code12'.isalpha()
False
>>> 'code'.isalpha()
True
>>> 'code123'.isalnum()
True
>>> 'code@123'.isalnum()
False
>>> 'code'.isalnum()
True
>>> '123'.isalnum()
True
>>> s
'Python Programming'
>>> s.istitle()
True
>>> 'myvar'.isidentifier()
True
>>> 'my@var'.isidentifier()
False
>>> ' '.isspace()
True
>>> '      hello'.isspace()
False
>>> '1234'.isdecimal()
True
>>> '1234'.isdigit()
True
>>> '1234'.isnumeric()
True
>>> 'a b c d'.split()
['a', 'b', 'c', 'd']
>>> 'a,b,c,d'.split()
['a,b,c,d']
>>> 'a,b,c,d'.split(',')
['a', 'b', 'c', 'd']
>>> 'a-b-c-d'.split('-')
['a', 'b', 'c', 'd']
>>> 'a-b-c-d'.split('-',2)
['a', 'b', 'c-d']
>>> 'a-b-c-d'.rsplit('-')
['a', 'b', 'c', 'd']
>>> 'a-b-c-d'.rsplit('-',2)
['a-b', 'c', 'd']
>>> s="""
hello
world
python
"""
>>> s
'\nhello\nworld\npython\n'
>>> s.splitlines()
['', 'hello', 'world', 'python']
>>> l=['a','b','c','d']
>>> '-'.join(l)
'a-b-c-d'
>>> '@'.join(l)
'a@b@c@d'
>>> '*'.join(1)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    '*'.join(1)
TypeError: can only join an iterable
>>> '*'.join(l)
'a*b*c*d'
>>> '_'.join(l)
'a_b_c_d'
>>> ''.join(l)
'abcd'
>>> s
'\nhello\nworld\npython\n'
>>> s='a-b-c-d'
>>> s.partition('b')
('a-', 'b', '-c-d')
>>> 'python.py'.partition('.')
('python', '.', 'py')
>>> 'pyt.hon.py'.partition('.')
('pyt', '.', 'hon.py')
>>> 'pyt.hon.py'.rpartition('.')
('pyt.hon', '.', 'py')
>>> ('pyt.hon', '.', 'py')
('pyt.hon', '.', 'py')
>>> s="hello"
>>> s.encode()
b'hello'
>>> t="Hello 😊"
>>> s.encode()
b'hello'
>>> t.encode()
b'Hello \xf0\x9f\x98\x8a'
>>> 
KeyboardInterrupt
>>> b'Hello \xf0\x9f\x98\x8a'.decode()
'Hello 😊'
>>> l=[]
>>> l=list()
>>> l=list()
>>> l=[1,2,3]
>>> l=list([1,2,3,4])
>>> 1
1
>>> l
[1, 2, 3, 4]
>>> type(l)
<class 'list'>
>>> #mut ord dup het dyn
>>> l=[1,1,1]
>>> l
[1, 1, 1]
>>> l=[1,12.3,3+5j,"str",[1,2],(1,2),{1,2},{1:2},False,None]
>>> l
[1, 12.3, (3+5j), 'str', [1, 2], (1, 2), {1, 2}, {1: 2}, False, None]
>>> #concatination
>>> [1,2,3]+[4,5,6]
[1, 2, 3, 4, 5, 6]
>>> #repetetion
>>> [1,2,3]*5
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> l
[1, 12.3, (3+5j), 'str', [1, 2], (1, 2), {1, 2}, {1: 2}, False, None]
>>> l=['python','java','c','flask','mysql','aws']
>>> l
['python', 'java', 'c', 'flask', 'mysql', 'aws']
>>> #indexing
>>> l[0]
'python'
>>> l[-1]
'aws'
>>> l[-2]
'mysql'
>>> l[2]
'c'
>>> l[3]
'flask'
>>> l[4]
'mysql'
>>> #slicing
>>> l
['python', 'java', 'c', 'flask', 'mysql', 'aws']
>>> l[:3]
['python', 'java', 'c']
>>> l[-3:]
['flask', 'mysql', 'aws']
>>> l[2:5]
['c', 'flask', 'mysql']
>>> l[1::2]
['java', 'flask', 'aws']
>>> #membership
>>> l
['python', 'java', 'c', 'flask', 'mysql', 'aws']
>>> 'java' in l
True
>>> 'c++' in l
False
>>> 'c' not in l'
SyntaxError: EOL while scanning string literal
>>> 'c' not in l
False
>>> 'web' not in s
True
>>> 'web' not in l
True
>>> len(l)
6
>>> sorted(l)
['aws', 'c', 'flask', 'java', 'mysql', 'python']
>>> max(l)
'python'
>>> min(l)
'aws'
>>> l
['python', 'java', 'c', 'flask', 'mysql', 'aws']
>>> id(l)
2133082251968
>>> l[1]
'java'
>>> l[1]='html'
>>> l
['python', 'html', 'c', 'flask', 'mysql', 'aws']
>>> id(l)
2133082251968
>>> l[2]='c++'
>>> l
['python', 'html', 'c++', 'flask', 'mysql', 'aws']
>>> l[3]='css'
>>> l
['python', 'html', 'c++', 'css', 'mysql', 'aws']
>>> 