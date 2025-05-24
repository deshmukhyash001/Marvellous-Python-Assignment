import basic

def main():
    k = basic.arrInp(int(input("Enter size of array : ")))
    
    kk = list(map(lambda no:no*2,k))
    
    print(kk)

if __name__ == '__main__':
    main()
