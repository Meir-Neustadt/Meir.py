import random
a=(5,5,6)
z,x,c=a
print(z)
s,d,h=a
print(s)


a={"1345":3, "0712":5, "0219":4}
max,keyy=0,None
for r in a:
    if a[r]>max:
        max=a[r]
        keyy=r
d=keyy[0]+keyy[1]
print(d)
num=0 
for i in range (len(d)):
    num=num*10+ord(d[i])-48 
print(num)    


bin={'8':'1000','9':'1001','a':'1010','b':'1011','c':'1100','d':'1101','e':'1110','f':'1111'}
a='9da8f'
for i in a:
    print(bin[i], end=' ')
print('h' in a)    


a={"rr":555, "yy":355, "ii":575, "pp":855 }
max=0
namee=""
for p in a:
    if(a[p]>max):
        max=a[p]
        namee=p
print(namee)
w=88

hexToBin={'0':"0000", '1':"0001", '2':"0010", '3':"0011", '4':"0100", '5':"0101", '6':"0110", '7':"0111",
            '8':"1000", '9':"1001", 'a':"1010", 'b':"1011", 'c':"1100", 'd':"1101", 'e':"1110",  'f':"1111"}
w={0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7',
            8:'8', 9:'9', 10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
for i in range(16):
    print(i, '\t',w[i], '\t',hexToBin[w[i]])
m=16*[None]
for i in range(len(m)):
    m[i]=chr(random.randint(40,120))
print(m)
H={} 
j=0  
for i in w:
    H[w[i]]=m[j]
    j+=1
for i in range(16):
    print(i, '\t', w[i], '\t', H[w[i]])
