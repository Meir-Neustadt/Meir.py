def S(a):
    h=[0]*27
    for i in range (len (a)):
        h[ord(a[i])-1488]+=1
    for i in range (len (h)):
        if b[i] < h[i]:
            b[i]=h[i]  

### MAIN ###             

a=['אריה','משה','אליעזר','פריידי','חני']
b=[0]*27
for i in range (len(a)):
    S(a[i])
for i in range (len(b)-1, -1, -1):
    for j in range (b[i]):
        print (chr(i+1488), end = ' ')
