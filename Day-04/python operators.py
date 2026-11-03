Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> "ARTHEMATIC OPERATORS"
'ARTHEMATIC OPERATORS'
>>> a=10
>>> b=20
>>> a+b
30
>>> a-b
-10
>>> a*b
200
>>> a/b
0.5
>>> a//b
0
>>> a%b
10
>>> a**b
100000000000000000000
>>> #add,sub,multiply,divison,floar div, mod,power value
>>> "COMPARISION OPERATORS"
'COMPARISION OPERATORS'
>>> a=20
>>> b=20
>>> a<b
False
>>> a<=b
True
>>> a>b
False
>>> a=20
>>> b=10
>>> a<b
False
>>> a<=b
False
>>> a>b
True
>>> a>=b
True
>>> a==b
False
>>> a!=b
True
>>> "ASSIGNMENT OPERATORS"
'ASSIGNMENT OPERATORS'
>>> C=30
>>> C=C+10
>>> C
40
>>> C-=10
>>> C
30
>>> C*=2
>>> C
60
>>> C/=5
>>> C
12.0
>>> C//=5
>>> C
2.0
>>> C/=5
>>> C
0.4
>>> C%=3
>>> C
0.4
>>> C**=9
>>> C
0.0002621440000000001
>>> "LOGICAL OPERATORS"
'LOGICAL OPERATORS'
>>> #and or not
>>> a=20
>>> a%2==0 and a>10
True
>>> b
10
>>> b%2==0 and b>10
False
>>> b%2==0 or b>10
True
>>> b%2==0
True
>>> not b%2==0
False
>>> #and means all values true
>>> # or means any one is true
>>> #not means negative
>>> "MEMBERSHIP OPERATORS"
'MEMBERSHIP OPERATORS'
>>> #STR list tuple set dict
>>> s='python'
>>> 'p' in  s
True
>>> 'e' in s
False
>>> 'd' not in s
True
>>> 'n' not in s
False
>>> l=["java","c","css","python","flask"}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> l=["java","c","css","python","flask"]
>>> "java" in l
True
>>> "c++" in l
False
>>> "mern" not in l
True
>>> "flask
SyntaxError: EOL while scanning string literal
>>> "flask" not in l
False
>>> t=(1,2,3)
>>> 1 in t
True
>>> 7 in t
False
>>> 1 not in t
False
>>> 9 not in t
True
>>> s={1,2,3,4}
>>> 1 in s
True
>>> 7 in s
False
>>> 2 not in s
False
>>> 7 not in s
True
>>> d={1:2,3:4,5:6}
>>> 1 in d
True
>>> 2 in d
False
>>> 3 not in d
False
>>> 4 not in d
True
>>> "IDENTITY OPERATORS"
'IDENTITY OPERATORS'
>>> l=[1,2,3]
>>> m=[1,2,3]
>>> id(l)
2243382243200
>>> id(m)
2243385519552
>>> 1==m
False
>>> l==m
True
>>> l is m
False
>>> n=m
>>> n
[1, 2, 3]
>>> id(n)
2243385519552
>>> n==m
True
>>> n is m
True
>>> n is not m
False
>>> n is not l
True
>>> 