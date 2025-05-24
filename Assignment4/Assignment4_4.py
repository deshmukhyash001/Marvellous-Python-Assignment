import basic
from functools import reduce
def main():
    print("Enter number of elements you want to store in array: ")
    k = basic.arrInp(int(input()))

    F = list(filter(lambda no: no%2 == 0,k))
    print(F)
    
    M = list(map(lambda no:no**2,k))
    print(M)
    
    R = reduce(lambda a,b: a+b, k)
    print(R)
    
if __name__ == '__main__':
    main()
