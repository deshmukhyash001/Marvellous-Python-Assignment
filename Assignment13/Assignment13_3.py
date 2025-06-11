class Numbers:
    
    def __init__(self,num):
        self.Num=num
        
    def ChkPrime(self):
        for i in range(self.Num-1,1,-1):
            if i % self.Num == 0:
                return False
                
        return True
    
    def ChkPerfect(self):
        
        if type(self.Num) == int:
            return f"{self.Num} is a Perfect Number"
        
        return f"{self.Num} is not a Perfect Number"
    
    def Factor(self,A=0):
        lis = list()
        if A != 0:
            for i in range(self.Num-1,1,-1):
                if i % self.Num == 0:
                    lis.append(i)
        
            return lis
        
        else:
            for i in range(self.Num-1,1,-1):
                if i % self.Num == 0:
                    lis.append(i)
            
            return lis
        
    def FactSum(self):
        factors = self.Factor(self.Num)
        sum = 0
        for i in factors:
            sum+=i
        
        return sum
    

def main():
    
    Obj1 = Numbers(12)
    Obj1 = Obj1.ChkPerfect()
    print(Obj1)
    
    Obj2 = Numbers(14)
    Obj2 = Obj2.ChkPrime()
    print(Obj2)
    
    
    Obj3 = Numbers(14)
    Obj3 = Obj3.Factor()
    print(Obj3)
    
    Obj4 = Numbers(15)
    Obj4 = Obj4.FactSum()
    print(Obj4)
    

if __name__ == '__main__':
    main()
