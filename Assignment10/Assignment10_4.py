import basic
from functools import reduce
def main():
    k = basic.arrInp(int(input("Enter a capacity of an array  : ")))

    f = list(filter(lambda n:n%2 == 0,k))
    
    m = list(map(lambda n : n**2,f))
    
    r = reduce(lambda n,n1:n+n1,m)
    
    print(f)
    print(m)
    print(r)
    

if __name__ == '__main__':
    main()
