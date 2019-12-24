
'''m=int(input("enter the dimensions a"))
n=int(input("enter the dimensions b"))
p=int(input("enter the dimensions c"))
q=int(input("enter the dimensions d"))'''



m=15
p=2
count=0
print("m",m,"p",p)
first=p*p
coun1=1
print(first,">>>>",coun1)

if(m<p*2):
    while(m!=p):
        #print("m",m,"p",p)
        t=m
        m=p
        p=abs(t-p)
        print("m",m,"p",p)
        #count1=count1+1
        #print(count1)
        if (p==1 or  m==1 ):

            c=m*p
            print("inside if",coun1+c)
            break


        else:
            coun1=coun1+1
            print("inside else",coun1)


else:
    while(p!=0):
        h=m%p
        x=int(m/p)

        m=p
        p=h

        count=count+x
print("total blocks",count)







