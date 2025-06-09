class Demo:
    Value = None

    def __init__(self,x,y):
        self.no1 = x
        self.no2 = y
    
    def Fun(self):
        print(self.no1)
        print(self.no2)
        
    def Gun(self):
        print(self.no1)
        print(self.no2)    

def main():
    Obj1 = Demo(10,11)
    Obj2 = Demo(20,21)

    Obj1.Fun()
    Obj2.Fun()
    
    Obj1.Gun()
    Obj2.Gun()

if __name__ == '__main__':
    main()
