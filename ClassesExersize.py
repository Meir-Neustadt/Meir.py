class MEN:
    __MinAge=0
    __MaxAge=120
    def __init__(self, name, family, age):
        self._Name=name
        self._Family=family
        if (age>=self.__MinAge and age<=self.__MaxAge):
            self._Age=age
        else: 
            self._Age=None    
    def __str__(self):
        return((self._Name)+' '+(self._Family)+' '+str(self._Age))   

class STUDENT(MEN):
    __Students=0
    def __init__(self, a, b, c, department, grade):
        super().__init__(a, b, c)
        self.__Department=department
        self.__Grade=grade
        STUDENT.__Students+=1
    @ staticmethod
    def StudentsNumber():
        return STUDENT.__Students   
    def __str__(self):
        return(super().__str__()+' '+self.__Department+' '+str(self.__Grade))    
    

a=STUDENT('Meir','Neustadt',67,'a',100)
b=STUDENT('Ohad','Benisty',128,'b',100)
c=STUDENT('Aharon','Ethrog',30,'a',100)
print(a)
print(b)
print(c)
print(STUDENT.StudentsNumber())



