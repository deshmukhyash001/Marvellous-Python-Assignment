import threading,time 

def evenFact(x):
    sum = 0
    for i in range(1,x):
        if x%i ==  0:
            sum += i
    print(sum)
            
def oddFact(x):
    sum = 0
    for i in range(1,x):
        if x%i !=  0:
            sum += i
    print(sum)
            
def main():
    print("Enter a number : ")
    n = int(input())        
    evenFacto = threading.Thread(target=evenFact,args=(n,))
    oddFacto = threading.Thread(target=oddFact,args=(n,))
    
    evenFacto.start()
    oddFacto.start()
    
if __name__ == '__main__':
    main()
