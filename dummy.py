'''a=int(input("a"))
b=int(input("b"))
count=0
x=range(a,b)

for i in range(a,b+1):
    count=0
    for j in range (1,i+1):

            c=i%j
            if(c==0):
                count=count+1
    if(count>=3):
        print("not prime",i)

    elif(count==2):
        print("prime",i)'''


