def main():
    print("Enter a num1 : ")
    k = int(input())
    
    print("Enter a num2 : ")
    k2 = int(input())
    
    m = lambda n1,n2 : n1*n2
    
    print(m(k,k2))

if __name__ == '__main__':
    main()
