# NAME:Sara Nauash
# GROUP:SE-2506

import math,csv,os
from abc import ABC,abstractmethod

# TASK 1: Function Arguments
def f1(n,a,c="Astana",**k):
    print(f"Name:{n}\nAge:{a}\nCity:{c}")
    for x,y in k.items():print(f"{x.capitalize()}:{y}")
    print("-" * 10)

f1("Alice",25)
f1("Bob",30,"Almaty")
n=input("Enter name:");a=input("Enter age:");h=input("Enter hobby:")
f1(n,a,hobby=h)

# TASK 2: Lambda, Map, and Filter
l=list(map(int,input("Enter numbers:").split()))
x=int(input("Enter threshold X:"))
s=list(map(lambda i:i**2,l))
e=list(filter(lambda i:i%2==0,l))
g=list(filter(lambda i:i>x,l))
print(f"Original:{l}\nSquared:{s}\nEven:{e}\nGreater than {x}:{g}")

# TASK 3: Basic Class and Object
class B:
    def __init__(self,t="",a="",p=0):
        self.t=t;self.a=a;self.p=p
    def d(self):
        print(f"The book '{self.t}' by {self.a} has {self.p} pages.")

b1=B("To Kill a Mockingbird","Harper Lee",281)
b2=B("The Great Gatsby","F. Scott Fitzgerald",180)
print("Enter a new book")
t=input("Title:");u=input("Author:");p=int(input("Pages:"))
b3=B(t,u,p)
b1.d();b2.d();b3.d()

# TASK 4: Class with __init__ and __str__
class R:
    def __init__(self,w,h):
        self.w=float(w);self.h=float(h)
    def a(self):return self.w*self.h
    def p(self):return 2*(self.w+self.h)
    def __str__(self):return f"Rectangle(width={self.w}, height={self.h})"

w=input("Enter width:");h=input("Enter height:")
r=R(w,h)
print(r);print(f"Area:{r.a()}");print(f"Perimeter:{r.p()}")

# TASK 5: Single Inheritance[cite: 1]
class V:
    def __init__(self,m,o,y):
        self.m=m;self.o=o;self.y=y
    def i(self):print(f"Vehicle:{self.m} {self.o} ({self.y})")

class C(V):
    def __init__(self,m,o,y,d):
        super().__init__(m,o,y);self.d=d
    def h(self):print("Beep beep!")

m=input("Make:");o=input("Model:");y=input("Year:");d=input("Doors:")
c=C(m,o,y,d)
c.i();print(f"Doors:{c.d}");c.h()

# TASK 6: Method Overriding and Polymorphism[cite: 1]
class S:
    def a(self):return 0
    def d(self):print("This is a shape.")

class Ci(S):
    def __init__(self,r):self.r=float(r)
    def a(self):return round(math.pi*(self.r**2),2)
    def d(self):print(f"This is a circle with radius {self.r}.")

class Sq(S):
    def __init__(self,s):self.s=float(s)
    def a(self):return self.s*self.s
    def d(self):print(f"This is a square with side {self.s}.")

r=input("Circle radius:");s=input("Square side:")
for i in [Ci(r),Sq(s)]:
    i.d();print(f"Area:{i.a()}")

# TASK 7: Association[cite: 1]
class Au:
    def __init__(self,n,t):self.n=n;self.t=t
class Bo:
    def __init__(self,t,y,a):self.t=t;self.y=y;self.a=a
    def i(self):
        print(f"Book: \"{self.t}\" ({self.y})\nAuthor: {self.a.n} ({self.a.t})")

n=input("Author Name:");t=input("Nationality:");b=input("Book Title:");y=input("Year:")
bo=Bo(b,y,Au(n,t))
bo.i()

# TASK 8: File I/O with Class Serialization[cite: 1]
class St:
    def __init__(self,n,i,g):self.n=n;self.i=i;self.g=[float(x) for x in g]
    def v(self):return sum(self.g)/len(self.g) if self.g else 0
    def s(self):return f"{self.n}|{self.i}|{','.join(map(str,self.g))}\n"

q=[St("Alice","001",[85,90]),St("Bob","002",[70,75])]
n=input("Student name:");i=input("ID:");g=input("3 grades:").split()
q.append(St(n,i,g))
with open("students.txt","w") as f:
    for s in q:f.write(s.s())
print("Data written.")
with open("students.txt","r") as f:
    for l in f:
        p=l.strip().split('|')
        o=St(p[0],p[1],p[2].split(','))
        print(f"{o.n} (ID: {o.i}) - Average: {o.v():.1f}")

# TASK 9: CSV Processing with Classes[cite: 1]
class E:
    def __init__(self,n,a,d,s):self.n=n;self.a=a;self.d=d;self.s=float(s)
    def r(self,p):self.s+=self.s*(p/100)
    def t(self):return {"name":self.n,"age":self.a,"dept":self.d,"sal":self.s}

z=[E("John",28,"HR",50000),E("Jane",32,"Sales",60000)]
n=input("New Emp Name:");a=input("Age:");d=input("Dept:");s=input("Salary:")
z.append(E(n,a,d,s))
h=["name","age","dept","sal"]
with open("employees.csv","w",newline='') as f:
    w=csv.DictWriter(f,fieldnames=h)
    w.writeheader()
    for e in z:w.writerow(e.t())
u=[]
with open("employees.csv","r") as f:
    r=csv.DictReader(f)
    for o in r:
        m=E(o["name"],o["age"],o["dept"],o["sal"])
        m.r(5);u.append(m)
with open("employees_updated.csv","w",newline='') as f:
    w=csv.DictWriter(f,fieldnames=h)
    w.writeheader()
    for e in u:w.writerow(e.t())
print("CSV tasks done.")

# TASK 10: Management System[cite: 1]
class Emp(ABC):
    def __init__(self,n,i):self.n=n;self.i=i
    @abstractmethod
    def p(self):pass
    @abstractmethod
    def c(self):pass

class HE(Emp):
    def __init__(self,n,i,r,h):super().__init__(n,i);self.r=float(r);self.h=float(h)
    def p(self):return self.r*self.h
    def c(self):return [self.n,self.i,'H',self.r,self.h]

class SE(Emp):
    def __init__(self,n,i,s):super().__init__(n,i);self.s=float(s)
    def p(self):return self.s/12
    def c(self):return [self.n,self.i,'S',self.s,0]

y=[]
while True:
    print("\n1.Add 2.Save 3.Load 4.Report 5.Exit")
    k=input("Choice:")
    if k=='1':
        t=input("1:Hourly 2:Salaried:");n=input("Name:");i=input("ID:")
        if t=='1':y.append(HE(n,i,input("Rate:"),input("Hours:")))
        else:y.append(SE(n,i,input("Salary:")))
    elif k=='2':
        with open("emps.csv","w",newline='') as f:
            w=csv.writer(f);[w.writerow(e.c()) for e in y]
    elif k=='3':
        y=[]
        with open("emps.csv","r") as f:
            r=csv.reader(f)
            for l in r:
                if l[2]=='H':y.append(HE(l[0],l[1],l[3],l[4]))
                else:y.append(SE(l[0],l[1],l[3]))
    elif k=='4':
        for e in y:print(f"{e.n} - Pay: ${e.p():.2f}")
    elif k=='5':break