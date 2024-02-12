def S1(a):
    Buyday=0
    SellDay=0
    Profit=0
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if (a[j]-a[i])>Bruto:
                BuyDay=i
                SellDay=j
                Profit=(a[j]-a[i])
    return(BuyDay,SellDay,Bruto) 

def S2(a):
    Buyday=0
    SellDay=0
    MostExpensive,ExpensiveDay=Expensive(a,0)
    Bruto=0
    for i in range(len(a)):
        if ExpensiveDay < i:
            MostExpensive,ExpensiveDay=Expensive(a,i+1)
        if (MostExpensive-a[i])>Bruto:
            Bruto=(MostExpensive-a[i])
            Buyday=i
            SellDay=ExpensiveDay   
    return(Buyday,SellDay,Bruto)

def Expensive(a,i):
    ME=a[i]
    Day=i
    for i in range(i+1,len(a)):
        if a[i]>=ME:
           ME=a[i]
           Day=i                       
    return (ME,Day)

a=[3,6,4,1,8,9,4,0,3]
print(S1(a),S2(a))
