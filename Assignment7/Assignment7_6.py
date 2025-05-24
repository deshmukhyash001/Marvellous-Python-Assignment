def isPrime(no):
    k,l = False,1
    while k != True and l<no:
        k%l != 0
        l +=1
        
import basic
def main():
    li = basic.arrInp(int(input("enter array capacity : ")))
    
    k = list(filter(isPrime,li))        
    print(k)
    
if __name__ == '__main__':
    main()
