import Assignment5.basic as basic
from MarvellousNum import ChkPrime as ListPrime
def main():
    print("How many elements you want to store in array : ")
    list1 = basic.arrInp(int(input()))
    print(ListPrime(list1))
    
if __name__ == "__main__":
    main()