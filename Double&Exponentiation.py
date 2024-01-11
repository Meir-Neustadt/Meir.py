
def D(num,mp):      
    global c
    n=num
    c+=6
    if mp>3:
        a=mp%2
        num=D(num,mp//2)
        RetNum=num+num
        RetNum+=a*n
        return RetNum
    if mp==3:
        return num+num+num
    if mp==2:
        return num+num
       
def F(num,R):
    global c
    global n
    if R>3:
        c+=5
        a=R%2
        num=F(num,R//2)
        if a==1:
            num=D(num,n)
        return D(num,num)
    if R==3:
        return D(num,D(num,num))
    return D(num,num)

c=0
n=567565658654757345698907890986897
print(F(n,6786675345786897985354241432536457)," ",c) 
c=0
print(D(6,42872648596175645852469808518239476579023),c)
c=0
print(DC(6,42872648596175645852469808518239476579023),c)
     
