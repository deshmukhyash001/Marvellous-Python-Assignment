from functools import reduce
import basic
def main():
    k=basic.arrInp(int(input("Enter capacity of array : ")))

    f = list(filter(lambda n : n>70 and n<90,k))

    m = list(map(lambda n : n+10,f))
    
    r = reduce(lambda n,m: n*m,f)
    
    print(f)
    print(m)
    print(r)
if __name__ == '__main__':
    main()
