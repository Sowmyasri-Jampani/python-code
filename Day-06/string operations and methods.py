Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s='python'
>>> s
'python'
>>> p=''
>>> p
''
>>> s
'python'
>>> t='programming'
>>> t
'programming'
>>> s+t
'pythonprogramming'
>>> t*3
'programmingprogrammingprogramming'
>>> 'e'*3
'eee'
>>> #repetation
>>> #indexing
>>> s ='python java flask mysql fastapi
SyntaxError: EOL while scanning string literal
>>> s ='python java flask mysql fastapi'
>>> s[0]
'p'
>>> s[f]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s[f]
NameError: name 'f' is not defined
>>> s[7]
'j'
>>> s[9]
'v'
>>> s[-4]
't'
>>> s[-2]
'p'
>>> 'p'
'p'
>>> #slicing
>>> s
'python java flask mysql fastapi'
>>> s[0:6:1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> s[0:6:1]
'python'
>>> s[7:11:1]
'java'
>>> s
'python java flask mysql fastapi'
>>> s[:6]
'python'
>>> s[7:11]
'java'
>>> s[12:17]
'flask'
>>> s[18:23]
'mysql'
>>> s[24:]
'fastapi'
>>> s[::-1]
'ipatsaf lqsym ksalf avaj nohtyp'
>>> s[-7:]
'fastapi'
>>> s[::2]
'pto aafakmslfsai'
>>> s[-15:-20:-1]
'ksalf'
>>> s[::-1]
'ipatsaf lqsym ksalf avaj nohtyp'
>>> #membership
>>> s
'python java flask mysql fastapi'
>>> 'java' in s
True
>>> 'mysql' in s
True
>>> 'c++' in s
False
>>> 'python'not in s
False
>>> #string methods
>>> s
'python java flask mysql fastapi'
>>> len(s)
31
>>> ord('a)
    
SyntaxError: EOL while scanning string literal
>>> ord('a')
97
>>> ord('c')
99
>>> ord('0')
48
>>> ord('*')
42
>>> ord('+')
43
>>> ord('-')
45
>>> ord('=')
61
>>> ord('')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    ord('')
TypeError: ord() expected a character, but string of length 0 found
>>> ord(' ')
32
>>> chr(20)
'\x14'
>>> chr(45)
'-'
>>> chr(90)
'Z'
>>> chr(98)
'b'
>>> max(s)
'y'
>>> min(s)
' '
>>> sorted(s)
[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'f', 'f', 'h', 'i', 'j', 'k', 'l', 'l', 'm', 'n', 'o', 'p', 'p', 'q', 's', 's', 's', 't', 't', 'v', 'y', 'y']
>>> #case sensitive
>>> s
'python java flask mysql fastapi'
>>> 'python java flask mysql fastapi'
'python java flask mysql fastapi'
>>> s.swapcase
<built-in method swapcase of str object at 0x0000029ECFDA08F0>
>>> s.swapcase()
'PYTHON JAVA FLASK MYSQL FASTAPI'
>>> s.upper()
'PYTHON JAVA FLASK MYSQL FASTAPI'
>>> s.lower()
'python java flask mysql fastapi'
>>> s.title()
'Python Java Flask Mysql Fastapi'
>>> s.capitliaze()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    s.capitliaze()
AttributeError: 'str' object has no attribute 'capitliaze'
>>> s.capitalize()
'Python java flask mysql fastapi'
>>> #formating
>>> s='python'
>>> s.center(40,'-')
'-----------------python-----------------'
>>> s.center(40,' ')
'                 python                 '
>>> s.center(40,'*')
'*****************python*****************'
>>> s.ljust(40,'*')
'python**********************************'
>>> s.rjust(40,'*')
'**********************************python'
>>> '1'.zfill(5)
'00001'
>>> '123'.zfill(5)
'00123'
>>> '123456'.zfill(5)
'123456'
>>> #finding methods
>>> s='Python java flask mysql fastapi'
>>> s
'Python java flask mysql fastapi'
>>> s.find('y')
1
>>> s.find('l')
13
>>> s.rfind('9')
-1
>>> s.rfind('k')
16
>>> s.index('j)
	
SyntaxError: EOL while scanning string literal
>>> s.index('j')
7
>>> s.rindex('l')
22
>>> s.rindex('z')
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    s.rindex('z')
ValueError: substring not found
>>> s.count('a')
5
>>> s.count('k')
1
>>> s.count('z')
0
>>> s='      code   gnan     '
>>> s.strip()
'code   gnan'
>>> s.lstrip()
'code   gnan     '
>>> s.rstrip()
'      code   gnan'
>>> #replace and translate
>>> s
'      code   gnan     '
>>> s='Python java flask mysql fastapi'
>>> s
'Python java flask mysql fastapi'
>>> s.replace('a','*')
'Python j*v* fl*sk mysql f*st*pi'
>>> s.replace('p','1')
'Python java flask mysql fasta1i'
>>> maketrans('apkqs','12345')
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    maketrans('apkqs','12345')
NameError: name 'maketrans' is not defined
>>> s.maketrans('apkqs','12345')
{97: 49, 112: 50, 107: 51, 113: 52, 115: 53}
>>> s.translate
<built-in method translate of str object at 0x0000029ECFDAB8F0>
>>> s.translate(s.maketrans('apkqs','12345'))
'Python j1v1 fl153 my54l f15t12i'
>>> s.translate(s.maketrans('apkqs','*****'))
'Python j*v* fl*** my**l f**t**i'
>>> 