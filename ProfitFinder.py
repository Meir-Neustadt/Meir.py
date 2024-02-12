def S(a):
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

a=[3,5,1,7,4,9,6,4]
print(S(a))
