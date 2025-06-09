from functools import reduce
import basic


def isPrime(n):
    if n == 0 or n == 1:
        print("Number is prime")
        
    else:
        for i in range(2,n):
            if i%2 == 0:
                break;
            
def main():
    k = basic.arrInp(int(input("Enter array capacity  : ")))
    
    f = filter(isPrime,k)
    m = filter(lambda n : n*2,f)
    r = reduce(,m)

if __name__ == '__main__':
    main()

            
