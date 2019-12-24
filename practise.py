'''thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
thislist.pop()
print(thislist)
print(mylist)
thislist.reverse()
print(thislist)
thislist.sort()
print(thislist)
print(thislist.index("banana"))
newstr = list(mystr)
print(newstr)
newstr.reverse()
print(newstr)

if newstr == mystr:
    print("palindrome")'''


'''str1=input("enter a line")
mystr=str1.split()
print(mystr.sort())
print(mystr)'''


#punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''#
#mystr = input("enter a string with punctuations")#

newstring=""

#for x in mystr:#
   # if x in punctuations:#
  #    newstring=newstring+x#

#print(newstring)#

''''tr=['1','2','2','1']

newstr=reversed(mystr)
print(list(newstr))
print(mystr)
if list(newstr)==list(mystr):
    print("pal")'''

'''X = [[12,7],
    [4 ,5],
    [7 ,8]]

Y = [[5,8,1],
    [6,7,3],
    [0,0,0]]



result=[[X[j][i] for j in range(3)] for i in range(2)]


for r in result:
   print(r)'''

'''x= int(input("enter a number"))

for i in range(1,11):
    result=x*i
    print(result,end="   ")


result=[x*i for i in range(1,11)]
print(result)'''

'''while True:
    no=int(input("enter the  no"))
    if no>0:
        print("positive")
    elif no<0:
        print("negative")
    else:
        print("no is 0")
    choice=input("do you want to check with different no: Y/N")
    if choice=='N':
        exit()'''


'''def rec(n):
    if n<=1:
       result= 1
    else:
        result= n + rec(n-1)


print(rec(6))'''
10
'''def recur_sum(n):
   """Function to return the sum
   of natural numbers using recursion"""
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

print("The sum is",recur_sum(9))'''

'''c=[20,30,20]
if c[0]>c[1] and c[0]>c[2]:
    print(c[0],"is g0retaer")
elif c[1]>c[0] and c[1]>c[2]:
    print(c[1],"is g0retaer")
else:
    print(c[2],"is gretaer")'''



'''count=0
num=int(input("enter a number"))

for i in range(2,num):
    if (num%i==0):
        print("not prime")
        break
else:
    print("prime")'''
'''for i in range(2, 10):
  #  if i > 1:
       for j in range(2,i):
           if (i % j) == 0:
               break
       else:
            print(i)'''



#func=map(lambda x:2**x,range(11))
#for i in func:
  #  print(i)

'''a,b=0,1
sum=0
terms=10
for i in range(1,11):
    print(a,end="   ")
    sum=a+b
    a=b
    b=sum'''

'''from datetime import datetime
now = datetime.now() # current date and time
year = now.strftime("%Y")
print("year:", year)
month = now.strftime("%m")
print("month:", month)
day = now.strftime("%d")
print("day:", day)
time = now.strftime("%H:%M:%S")
print("time:", time)
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)'''

'''squares = {1:1, 2:4, 3:9, 4:16, 5:25}
print(squares.pop(4))
print(squares)'''

'''mystr = "banana"
myit = iter(mystr)
print(next(myit))'''


# define Python user-defined exceptions
'''class Error(Exception):
   """Base class for other exceptions"""
   pass
class ValueTooSmallError(Exception):
   """Raised when the input value is too small"""
   pass
class ValueTooLargeError(Exception):
   """Raised when the input value is too large"""
   pass
# our main program
# user guesses a number until he/she gets it right
# you need to guess this number
number = 10
while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise ValueTooSmallError
       elif i_num > number:
           raise ValueTooLargeError

       break
   except ValueTooSmallError:
       print("This value is too small, try again!")
       print()
   except ValueTooLargeError:
       print("This value is too large, try again!")
       print()

else:
           print("Congratulations! You guessed it correctly.")'''


'''class p:
    a=777

    def __init__(self):
        self.b=9

class c(p):


    def m1(self):

        print(super().a)

        print(self.b)
s=c()
s.m1()'''



'''class p:
    a=10
    def __init__(self):
        print("constructor")
    def m1(self):
        print("instnace")

    @classmethod
    def m2(cls):
        print("class")
    @staticmethod
    def m3():
        print("static")


class c(p):
    @staticmethod
    def m1():
        print(super().a)
        print(super().m2())
        print(super().m3())

c=c()
c.m1()'''


'''class test:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return "name is {} and age is {}".format(self.name, self.age)


t=test()
print(t)'''


'''class test:
    a=10
    def __init__(self):
        self.b=20


t1=test()
t2=test()


test.a=888
t2.b=999


t1.a=777
t1.b=999
print(test.a)
print(t1.a)
print(t1.b)
print(t2.a)
print(t2.b)'''


'''s={1:1,2:2,3:3,4:4}
t={2:3,4:6,3:5}

for i,j in s.items():

    for i,k in t.items():

print(j*k)'''

#print(9/4)

'''a=int(input())
b=int(input())
count=0
for i in range(a,b):
        for j in range(2,i):
            c=i%j
            if(c==0):
                count=count+1


if(count>2):
    print("not prime",i)'''

'''with open("emp.txt", "r") as work_data:
    previous_content=work_data.readlines()


previous_content.append()
#print(previous_content)

with open("emp.txt", "w") as work_data:
    new= "".join(previous_content)
    work_data.write(new)


with open("emp.txt", "r") as work_data:
    for line in work_data:
        print(line)'''


'''a=[5,2,3,9,4]
temp=[]
print(len(a))
for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j+1]:
            a[j+1], a[j] = a[j], a[j+1]

print (a)'''
count=0
a=3
k = 2*a - 2
for i in range(1,a+1):

    for j in range(1,a+1):
        if (count==0):
            print ( j ,end ="  ")
        if (count>0):
            print ("\t", j ,"\t",end ="  ")

    a=a-1
    print("\n")
    print("\t\t\t")
    count=+1












