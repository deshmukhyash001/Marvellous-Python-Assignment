def main():
    print("enter a number: ")
    k = int(input())
    
    for i in range(1,k+1):
        for j in range(i):
            print("*",end=" ")
        print()

if __name__ == '__main__':
    main()
