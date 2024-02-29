def IsSpecial(str):
    chrs=[0]*26
    if str[0]>='A'and str[0]<='Z':
        for chr in str:
            if chr>='A' and chr<='Z':
                chrs[ord(chr)-ord('A')]+=1
            else:
                return False
    if str[0]>='a'and str[0]<='z':
        for chr in str:
            if chr>='a' and chr<='z':
                chrs[ord(chr)-ord('a')]+=1
            else:
                return False 
    else:
        return False 
    for num in chrs:
        if num%2==1:
            return False
    print(chrs)
    return True

a="aaeettzz"
print(IsSpecial(a))  
