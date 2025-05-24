import basic
from functools import reduce

def main():
    k = basic.arrInp(int(input("Enter no of array element : ")))
    print(type(k))

    k1 = list(filter(lambda no: no>=70,list(k)))
    print(k1)

    k2 = list(map(lambda no : no+10,k1))
    print(k2)

    k3=reduce(lambda a,b: a+b,k2)
    print(k3)
    
if __name__ == '__main__':
    main()