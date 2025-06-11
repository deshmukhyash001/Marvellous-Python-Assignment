class BookStore:
    NoOfBooks = 0
    def __init__(self,A,N):
        self.Name  =  A
        self.Author = N
        BookStore.NoOfBooks+=1
        
    def Display(self):
        print(self.Name,"By",self.Author,". No of books :",BookStore.NoOfBooks)
    
    

def main():
        
    Obj1 = BookStore("Linux System Programming","Robert Love")
    Obj1.Display()
    
    Obj2 = BookStore("C Programming ","Dennis Ritchie")
    Obj2.Display()

if __name__ == '__main__':
    main()
