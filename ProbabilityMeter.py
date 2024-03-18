probability=0

def prob(n,p,c):
    global probability
    if n!=0:
        prob(n-1,p*5/6,c)
        prob(n-1,p*1/6,c+1) 
    elif c>=2:
        probability+=p

prob(5,1,0)
print(probability)
