class Circle:
    Pi = 3.14
    
    def __init__(self):
        self.Radius = 0.0
        self.Circumference = 0.0
        self.Area = 0.0
        
    def Accept(self):
        print("Enter a size of Radius")
        self.Radius = float(input())

    def CalculateArea(self):
        self.Area = Circle.Pi*(self.Radius**2)
        return self.Area
    
    def CalculateCircum(self):
        self.Circumference = 2*Circle.Pi*self.Radius
        return self.Circumference
    
    def Display(self):
        print("Area of circle is : ",self.CalculateArea())
        print("Circumference of circle is : ", self.CalculateCircum())
        
def main():
    Obj1 = Circle()
    Obj1.Accept()
    Obj1.Display()

if __name__ == '__main__':
    main()
