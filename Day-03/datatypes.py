Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> type(a)
<class 'int'>
>>> b=10.5
>>> type(b)
<class 'float'>
>>> c=3+4j
>>> type(c)
<class 'complex'>
>>> s="sowmya"
>>> type(s)
<class 'str'>
>>> l=[1,2,3,4]
>>> type(l)
<class 'list'>
>>> d=[1,2.3,"sri"]
>>> type(d)
<class 'list'>
>>> s="code"
>>> id(s)
2343958630128
>>> s
'code'
>>> s+='gnan'
>>> s
'codegnan'
>>> id(s)
2343960900272
>>> l
[1, 2, 3, 4]
>>> d
[1, 2.3, 'sri']
>>> d.append(25)
>>> d
[1, 2.3, 'sri', 25]
>>> id(d)
2343981258304
>>> t=(1,2,3,4)
>>> t=(1,1,1,1,)
>>> 
>>> t
(1, 1, 1, 1)
>>> t=(1,2.3)
>>> t
(1, 2.3)
>>> type(t)
<class 'tuple'>
>>> s={3,1234,34,34,34,1236789,1073,}
>>> s
{1073, 34, 3, 1234, 1236789}
>>> type(s)
<class 'set'>
>>> d={1:"one",2:[4,5.4,5],[5,8,6]}
SyntaxError: invalid syntax
>>> D={1:"one",2:4,3:[1,2,3],5:(1,23)}
>>> D
{1: 'one', 2: 4, 3: [1, 2, 3], 5: (1, 23)}
>>> pro={"pro_name":'laptop',"price":55000,"discount":10}
>>> pro
{'pro_name': 'laptop', 'price': 55000, 'discount': 10}
>>> type(D)
<class 'dict'>
>>> status=True
>>> type(status)
<class 'bool'>
>>> s=false
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    s=false
NameError: name 'false' is not defined
>>> s=False
>>> type(s)
<class 'bool'>
>>> s=None
>>> type(s)
<class 'NoneType'>
>>> 