def main():
    add = lambda no1,no2 : no1+no2
    sub = lambda no1,no2 : no1-no2    
    mul = lambda no1,no2 : no1*no2    
    div = lambda no1,no2 : no1/no2    
        
    print("Enter no1: ",end ="" )
    n1 = int(input())
    print("Enter no2: ",end ="" )
    n2 = int(input())
    
    print("Sum : ",add(n1,n2))
    print("Difference : ",sub(n1,n2))
    print("Product : ",mul(n1,n2))
    print("Division : ",div(n1,n2))

if __name__ == '__main__':
    main()
