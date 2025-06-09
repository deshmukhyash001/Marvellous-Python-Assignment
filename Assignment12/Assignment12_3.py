class Arithematic():
    def __init__(self):
        self.No1 = 0.0
        self.No2 = 0.0  
        
    def Accept(self):
        
        print("Enter no1 : ")  
        self.No1 = float(input())
        
        print("Enter no2 : ")  
        self.No2 = float(input())

    def Sum(self):
        
        return self.No1 + self.No2
        
    def Sub(self):
        return self.No1 - self.No2
    
    def Prod(self):
        return self.No1 * self.No2
    
    def Div(self):
        return self.No1 / self.No2
    
    def Display(self):
        print("Addition of", self.No1 , "And",self.No2, "is", self.Sum())
        print("Subraction of", self.No1 , "And",self.No2, "is", self.Sub())
        print("Product of", self.No1 , "And",self.No2, "is", self.Prod())
        print("Division of", self.No1 , "And",self.No2, "is", self.Div())
        
        
def main():
    Obj1 = Arithematic()
    Obj1.Accept()
    Obj1.Display()        

if __name__ == '__main__':
    main()
