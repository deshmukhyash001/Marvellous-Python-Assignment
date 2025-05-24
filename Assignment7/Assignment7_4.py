import basic
from functools import reduce
def main():
    li = basic.arrInp(int(input("Enter capacity of array : ")))        
    prod = reduce(lambda n,m:n*m,li) 
    print("product is : ",prod)

if __name__ == '__main__':
    main()

