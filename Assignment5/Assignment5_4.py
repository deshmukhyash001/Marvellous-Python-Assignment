def main():
    print("Enter 3 numbers : ")
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())

    if n1 > n2  and n1>n3:
        print(n1," is largest")

    elif n2 > n1 and n2 > n3:
        print(n2," is largest")

    elif n3 > n2  and n3>n1:
        print(n3," is largest")
        
if __name__ == '__main__':
    main()
