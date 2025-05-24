
import basic

def main():
    li=basic.arrInp(int(input("Enter size of array : ")))
    k = list(filter(lambda n : n&1 ==0,li))
    
    print(k)
if __name__ == '__main__':
    main()
