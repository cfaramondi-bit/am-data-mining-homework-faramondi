# ===== Esercizio: Say “Hello World! With python” ===== 
if __name__ == '__main__':
    print("Hello, World!")


# ===== Esercizio: Python If-Else =====
#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    if n%2==1:
        print("Weird")
    elif n%2==0 and 2<=n<=5:
        print("Not Weird")
    elif n%2==0 and 6<=n<=20:
        print("Weird")
    elif n%2==0 and n>20:
        print("Not Weird")


# ===== Esercizio: Arithmetic Operators ====

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(f"{a+b}")
    print(f"{a-b}")
    print(f"{a*b}")
    
# ===== Esercizio: Python Division====
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(f"{a//b}")
    print(f"{a/b}")
    
# ===== Esercizio: Loops====

if __name__ == '__main__':
    n = int(input())
    if n>20 or n<1:
        print("Valore non valido")
    else:
        for i in range(n):
          print(f"{i**2}")

# ===== Esercizio: Write a function====
def is_leap(year):
    leap = False
    #if year<1900 or year>10**5:
      #  print("Invalid input")
    if year%4==0 and year%100!=0:
        return True
    elif year%4==0 and year%100==0 and year%400==0:
        return True
        
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))


# ===== Esercizio: Print function====
if __name__ == '__main__':
    n = int(input())
    #if n<1 or n>150:
     #   print("Invalid Input")
    for i in range(1,n+1):
        print(i,end="")



# ===== Esercizio: Find the Runner-Up score!====

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=sorted(set(arr))
    print(f"{arr[-2]}")



# ===== Esercizio: Finding the percentage====

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    average= sum(student_marks[query_name])/3
    print(f"{average:.2f}")

# ===== Esercizio: sWAP cASE====
def swap_case(s):
    result=""
    for lettera in s:
        if lettera.isupper():
            result += lettera.lower()
        else: 
            result += lettera.upper()    
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# ===== Esercizio: Tuples====
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    print(hash(t))


# ===== Esercizio: List Comprehensions====

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
lista=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n ]
print(f"{lista}")


# ===== Esercizio: String Split and Join====

def split_and_join(line):
    # write your code here
    line=line.split(" ")
    return "-".join(line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# ===== Esercizio: What’s Your Name?====
def print_full_name(first, last):
    # Write your code here
    print(f"Hello {first} {last}! You just delved into python.")
    return
    
    
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# ===== Esercizio: Mutations====

def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    string= ''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# ===== Esercizio: Text Wrap====

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# ===== Esercizio: Introduction to Sets====

def average(array):
    dist_heights=set(array)
    av=sum(dist_heights)/len(dist_heights)
    return av
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# ===== Esercizio: No Idea!====

if __name__ == '__main__':
    n,m =map(int, input().split()) 
    arr = list(map(int, input().split()))
    A=set(map(int, input().split()))
    B=set(map(int, input().split()))
    h=0
    for i in range(0,n):
        if arr[i] in A: h+=1
        if arr[i] in B: h-=1
    print(f"{h}")


# ===== Esercizio: Symmetric Difference====

if __name__=='__main__':
    M=int(input())
    A=set(map(int,input().split()))
    N=int(input())
    B=set(map(int,input().split()))
    diff=(A.difference(B)).union(B.difference(A))
    diff_new=list(diff)
    diff_new.sort()
    for i in range (0,len(diff_new)):
        print(f"{diff_new[i]}")

# ===== Esercizio: Set.add()====

if __name__=='__main__':
    N=int(input())
    stamps=set()
    for _ in range (N):
        stamps.add(input())
    print(f"{len(stamps)}")


# ===== Esercizio: Set.union() Operation====

n=int(input())
en=list(map(int,input().split()))
b=int(input())
fr=list(map(int,input().split()))

en_new=set(en)
fr_new=set(fr)

print(f"{len(en_new.union(fr_new))}")


# ===== Esercizio: Set.intersection() Operation====

n=int(input())
en=list(map(int,input().split()))
b=int(input())
fr=list(map(int,input().split()))

en_new=set(en)
fr_new=set(fr)

print(f"{len(en_new.intersection(fr_new))}")


# ===== Esercizio: Set.difference() Operation====

n=int(input())
en=list(map(int,input().split()))
b=int(input())
fr=list(map(int,input().split()))

en_new=set(en)
fr_new=set(fr)

print(f"{len(en_new.difference(fr_new))}")


# ===== Esercizio: Set.symmetric_difference() Operation====

n=int(input())
en=list(map(int,input().split()))
b=int(input())
fr=list(map(int,input().split()))

en_new=set(en)
fr_new=set(fr)
print(f"{len((en_new.difference(fr_new)).union(fr_new.difference(en_new)))}")


# ===== Esercizio: Check Subset====

T=int(input())
for _ in range(T):
    n_A=int(input())
    A=set(map(int,input().split()))
    n_B=int(input())
    B=set(map(int,input().split()))
    print(f"{A.issubset(B)}")


# ===== Esercizio: Check Strict Superset====
A=set(map(int,input().split()))
n=int(input())
booleans=[]
for _ in range(n):
    subsets=set(map(int,input().split()))
    booleans.append(A>subsets)
print(all(booleans))

# ===== Esercizio: Lists====
if __name__ == '__main__':
    N = int(input())
    lista=[]
    for _ in range(N):
        command=input().split()
        if command[0]== "insert":
            lista.insert((int(command[1])),int(command[2]))
        elif command[0]=="print":
            print(lista)
        elif command[0]=="remove":
            lista.remove(int(command[1]))
        elif command[0]=="append":
            lista.append(int(command[1]))
        elif command[0]=="sort":
            lista.sort()
        elif command[0]=="pop":
            lista.pop()
        elif command[0]=="reverse":
            lista.reverse()
            
        
  
# ===== Esercizio: Set.discard(),.remove(),.pop()====

n = int(input())
s = set(map(int, input().split()))
N=int(input())
for _ in range(N):
    command= input().split()
    if command[0]=="pop":
        s.pop()
    elif command[0]=="remove":
        s.remove(int(command[1]))
    elif command[0]=="discard":
        s.discard(int(command[1]))
print(sum(s))


# ===== Esercizio: String Validators====

if __name__ == '__main__':
    s = input()
    alnum=[]
    alpha=[]
    digits=[]
    lower=[]
    upper=[]
    for i in range (len(s)):
        alnum.append(s[i].isalnum())
        alpha.append(s[i].isalpha())
        digits.append(s[i].isdigit())
        lower.append(s[i].islower())
        upper.append(s[i].isupper()) 
    print(any(alnum))
    print(any(alpha))
    print(any(digits))
    print(any(lower))
    print(any(upper))
    


# ===== Esercizio: Text Alignment====
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))




# ===== Esercizio: Find a String ====

def count_substring(string, sub_string):
    n=len(string)
    k=len(sub_string)
    c=0
    for i in range (len(string)):
        if string[i:i+len(sub_string)]==sub_string: c+=1
    return c
            
   
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# ===== Esercizio: collections.Counter()====

from collections import Counter
if __name__=="__main__":
    X=int(input())
    all_sizes=list(map(int, input().split()))
    N=int(input())
    availability=Counter(all_sizes)
    money=0
    for _ in range(N):
        size,xi=list(map(int, input().split()))
        if availability[size]>0:
            money+=xi
            availability[size]-=1
    print(money)


# ===== Esercizio: Calendar Module====

import calendar

if __name__=="__main__":
    MM, DD, YYYY = map(int, input().split())
    weekdays=["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    print(weekdays[calendar.weekday(YYYY,MM,DD)])


# ===== Esercizio: Zipped!====

N,X=map(int,input().split())
K=[]
for _ in range(X):
    marks=list(map(float,input().split()))
    K.append(marks)
for t in zip(*K):
    average=sum(t)/len(t)
    print(f"{average:.1f}")


# ===== Esercizio: Collections.OrderedDict()====

from collections import OrderedDict

N=int(input())
d=OrderedDict()
for _ in range(N):
    *name,price= input().split()
    name=" ".join(name)
    d[name]=d.get(name,0)+int(price)
for name,tot in d.items():
    print(name,tot)

# ===== Esercizio: Arrays====

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr.reverse()
    return numpy.array(arr,float)
    
    
    

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# ===== Esercizio: Shape and Reshape====

import numpy

integers=numpy.array(input().split(),int)
print (numpy.reshape(integers,(3,3)))


# ===== Esercizio: Transpose and Flatten====

import numpy

N,M=list(map(int,input().split()))
columns=[]
for _ in range(N):
    columns.append(numpy.array(input().split(),int))
matrix=numpy.reshape(columns,(N,M))
print (numpy.transpose(matrix))
print(matrix.flatten())


# ===== Esercizio: Concatenate====

import numpy

N,M,P=list(map(int,input().split()))
columns1=[]
for _ in range(N):
    columns1.append(numpy.array(input().split(),int))
columns2=[]
for _ in range(M):
    columns2.append(numpy.array(input().split(),int))
matrix1=numpy.reshape(columns1, (N,P))
matrix2=numpy.reshape(columns2, (M,P))
print (numpy.concatenate((matrix1,matrix2),axis=0))



# ===== Esercizio: Zeros and Ones====

import numpy

dim=numpy.array(input().split(),int)
print(numpy.zeros((dim),dtype=int))
print(numpy.ones((dim),dtype=int))


# ===== Esercizio: Eye and Identity====

import numpy
numpy.set_printoptions(legacy='1.13')

N,M=list(map(int,input().split()))
print (numpy.eye(N,M,k=0))


# ===== Esercizio: Array Mathematics====

import numpy


N,M=list(map(int,input().split()))
A=[]
for _ in range(N):
    A.append(numpy.array(input().split(),int))
B=[]
for _ in range(N):
    B.append(numpy.array(input().split(),int))
A=numpy.array(A)
B=numpy.array(B)
print (numpy.add(A, B))
print (numpy.subtract(A, B))
print (numpy.multiply(A, B))
print (numpy.floor_divide(A, B))
print (numpy.mod(A, B))
print (numpy.power(A, B))


# ===== Esercizio: Floor, Ceil and Rint====

import numpy
numpy.set_printoptions(legacy='1.13')

A=numpy.array(input().split(),float)
print (numpy.floor(A))
print (numpy.ceil(A))
print (numpy.rint(A))



# ===== Esercizio: Sum and Prod====
import numpy


N,M=list(map(int,input().split()))
integers=[]
for _ in range (N):
    integers.append(numpy.array(input().split(),int))
integers=numpy.array(integers)
somma=numpy.sum(integers,axis=0)
print(numpy.prod(somma))


# ===== Esercizio: Min and Max====

import numpy


N,M=list(map(int,input().split()))
integers=[]
for _ in range (N):
    integers.append(numpy.array(input().split(),int))
integers=numpy.array(integers)
minimum=numpy.min(integers,axis=1)
print(numpy.max(minimum))


# ===== Esercizio: Mean, Var, Std====

import numpy

N,M=list(map(int,input().split()))
integers=[]
for _ in range (N):
    integers.append(numpy.array(input().split(),int))
integers=numpy.array(integers)
print (numpy.mean(integers,axis=1))
print (numpy.var(integers,axis=0))
print(round(numpy.std(integers, axis=None), 11))


# ===== Esercizio: Dot and Cross====

import numpy

N=int(input())
A=numpy.array([input().split() for _ in range (N)],int)
B=numpy.array([input().split() for _ in range (N)],int)

print (numpy.dot (A,B))


# ===== Esercizio: Inner and Outer====

import numpy

A=numpy.array(input().split(),int)
B=numpy.array(input().split(),int)
print(numpy.inner(A,B))
print(numpy.outer(A,B))


# ===== Esercizio: Polynomials====

import numpy

P=numpy.array(input().split(),float)
x=float(input())
print (numpy.polyval(P,x))


# ===== Esercizio: Linear Algebra====

import numpy

N=int(input())
A=numpy.array([input().split() for _ in range (N)],float)

print(numpy.round(numpy.linalg.det(A),2))


# ===== Esercizio: Nested Lists====

if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    second_lowest=sorted(set(score for _, score in students))[1]
    result=sorted(name for name, score in students if score==second_lowest)
    for i in range(len(result)):
        print(result[i])


# ===== Esercizio: Designer Door Mat====

n,m=map(int,input().split())
for i in range(1,n,2):
    print((".|."*i).center(m,'-'))
print("WELCOME".center(m,'-'))
for i in range(n-2,0,-2):
    print((".|."*i).center(m,'-'))


# ===== Esercizio: String Formatting====

def print_formatted(number):
    width=len(bin(number))-2
    for i in range(1,number+1):
        print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# ===== Esercizio: Alphabet Rangoli====

def print_rangoli(size):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    width=4*size-3         
    lines=[]
    for i in range(size):
        left=alphabet[size-1:size-1-i:-1] if i>0 else ""
        row=left+alphabet[size-1-i]+left[::-1]
        lines.append("-".join(row).center(width,'-'))
    print("\n".join(lines+lines[-2::-1]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# ===== Esercizio: Capitalize!====

def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# ===== Esercizio: The Minion Game====
def minion_game(string):
    vowels="AEIOU"
    n=len(string)
    stuart=0
    kevin=0
    for i,ch in enumerate(string):
        if ch in vowels:
            kevin+=n-i
        else:
            stuart+=n-i
    if stuart>kevin:
        print("Stuart",stuart)
    elif kevin>stuart:
        print("Kevin",kevin)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

# ===== Esercizio: Merge the Tools!====

def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        part=string[i:i+k]
        print(''.join(dict.fromkeys(part)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# ===== Esercizio: The Captain’s Room====
K=int(input())
room_number=list(map(int, input().split()))

unique=set(room_number)
captain=(K*sum(unique)-sum(room_number))//(K-1)
print(captain)

# ===== Esercizio: Set Mutations====

_=input()
A=set(map(int, input().split()))
for _ in range(int(input())):
    op,_=input().split()
    B=set(map(int, input().split()))
    getattr(A,op)(B)
print(sum(A))


# ===== Esercizio: DefaultDic Tutorial====

from collections import defaultdict

n,m=map(int,input().split())
d = defaultdict(list)
for i in range(1,n+1):
    elem_A=input()
    d[elem_A].append(i)
for _ in range(m):
    elem_B=input()
    if d[elem_B]:  
        print(' '.join(map(str, d[elem_B])))
    else:
        print(-1)


# ===== Esercizio: Collections.namedtuple()====

from collections import namedtuple

N=int(input())
columns=input().split()
Student=namedtuple('Student',columns)
total=0
for _ in range(N):
    data=input().split()
    student=Student(*data)
    total+=int(student.MARKS)
print(f"{total/N:.2f}")


# ===== Esercizio: Time Delta====

from datetime import datetime
import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):
    fmt="%a %d %b %Y %H:%M:%S %z"
    d1=datetime.strptime(t1,fmt)
    d2=datetime.strptime(t2,fmt)
    return str(int(abs((d1-d2).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()


# ===== Esercizio: Word Order====

from collections import OrderedDict

n=int(input())
counts=OrderedDict()
for _ in range(n):
    word=input()
    counts[word]=counts.get(word,0)+1
print(len(counts))
print(*counts.values())


# ===== Esercizio: Collections.deque()====

from collections import deque

d=deque()
for _ in range(int(input())):
    command,*args=input().split()
    getattr(d,command)(*args)
print(*d)


# ===== Esercizio: Company Logo====

#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    s = input()
    counts=Counter(s)
    top3=sorted(counts.items(),key=lambda x:(-x[1],x[0]))[:3]
    for char,count in top3:
        print(char, count)


# ===== Esercizio: Piling Up!====

from collections import deque

T=int(input())
for _ in range(T):
    n=int(input())
    cubes=deque(map(int, input().split()))
    prev=float('inf')
    possible=True
    while cubes:
        if cubes[0]>=cubes[-1]:
            cur=cubes.popleft()
        else:
            cur=cubes.pop()
        if cur>prev:
            possible=False
            break
        prev=cur
    print("Yes" if possible else "No")


# ===== Esercizio: Athlete Sort====

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    arr.sort(key=lambda row:row[k])
    for row in arr:
        print(*row)


# ===== Esercizio: ginortS====

S=input()

def key(c):
    if c.islower():
        return (0,c)
    if c.isupper():
        return (1,c)
    if int(c)%2==1:
        return (2,c)
    return (3,c)
print("".join(sorted(S,key=key)))


# ===== Esercizio: Map and Lambda Function====
cube = lambda x: x**3

def fibonacci(n):
    fib=[]
    a,b=0,1
    for _ in range(n):
        fib.append(a)
        a,b=b,a+b
    return fib
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

# ===== Esercizio: XML1- Find Score====

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
     return len(node.attrib)+sum(get_attr_number(child) for child in node)

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

# ===== Esercizio: XML2- Find the Maximun Depth====

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem,livello):
    global maxdepth
    livello+=1
    if livello>maxdepth:
        maxdepth=livello
    for child in elem:
        depth(child,livello)
        
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)

# ===== Esercizio: Detect Floating Point Number====

import re
T=int(input())
for _ in range(T):
    print(bool(re.match(r'^[+-]?\d*\.\d+$',input())))


# ===== Esercizio: Re.split()====

regex_pattern = r"[,.]" # Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

# ===== Esercizio: Group(),Groups(),Groupdict()====

import re

S=input()
m = re.search(r'([A-Za-z0-9])\1',S)
print(m.group(1) if m else -1)


# ===== Esercizio: Re.findall() and Re.finditer()====

import re 

S=input()
vocali='aeiouAEIOU'
consonanti='qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
matches=re.findall(r'(?<=[' +consonanti+ r'])([' +vocali+ r']{2,})(?=[' +consonanti+ r'])',S)

print('\n'.join(matches) if matches else -1)


# ===== Esercizio: Re.Start() and Re.end()====

import re 
S=input()
k=input()
pattern=re.compile(k)
m=pattern.search(S)
if not m:
    print((-1,-1))
while m:
    print((m.start(),m.end()-1))
    m=pattern.search(S,m.start()+1)


# ===== Esercizio: Hex Color Code====
import re

N=int(input())
css = "\n".join(input() for _ in range(N))

for block in re.findall(r'\{([^}]*)\}', css):
    for c in re.findall(r'#(?:[0-9a-fA-F]{3}){1,2}(?![0-9a-zA-Z])', block):
        print(c)


# ===== Esercizio: HTML Parser Part 1====

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print('Start :',tag)
        for name, value in attrs:
            print('->',name,'>',value)

    def handle_endtag(self,tag):
        print('End   :',tag)

    def handle_startendtag(self,tag,attrs):
        print('Empty :',tag)
        for name, value in attrs:
            print('->',name,'>',value)

parser = MyHTMLParser()
N=int(input())
parser.feed("\n".join(input() for _ in range(N)))


# ===== Esercizio: Validating Phone Numbers====

import re
N=int(input())
for _ in range(N):
    s=input()
    print('YES' if re.fullmatch(r'[789]\d{9}',s) else 'NO')


# ===== Esercizio: Validating Roman Numerals====

regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    # Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

# ===== Esercizio: Validating and Parsing Email Adresses====

import re
import email.utils

n=int(input())
pattern=re.compile(r"[A-Za-z][\w.-]*@[A-Za-z]+\.[A-Za-z]{1,3}")
for _ in range(n):
    line=input()
    name,address=email.utils.parseaddr(line)
    if pattern.fullmatch(address):
        print(email.utils.formataddr((name,address)))


# ===== Esercizio: Validating UID====

import re 

T=int(input())
pattern=re.compile(
    r"^(?!.*(.).*\1)(?=(?:.*[A-Z]){2})(?=(?:.*\d){3})[A-Za-z0-9]{10}$")
for _ in range(T):
    print("Valid" if pattern.match(input()) else "Invalid")


# ===== Esercizio: Standardize Mobile Number Using Decorators====

def wrapper(f):
    def fun(l):
        f(["+91 "+n[-10:-5]+" "+n[-5:] for n in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

# ===== Esercizio: Decorators 2====

import operator

def person_lister(f):
    def inner(people):
        return [f(p) for p in sorted(people,key=lambda p: int(p[2]))]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

# ===== Esercizio: Birthday Cake Candles====

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    return candles.count(max(candles))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


# ===== Esercizio: Recursive Digit Sum====

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    p=sum(int(c) for c in n)*k
    if p<10: return p 
    else: return superDigit(str(p),1)
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

