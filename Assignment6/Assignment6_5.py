def main():
    print("Enter a number: ")
    k = int(input())
    
    for i in range(k,1,-1):
        if k%i == 0:
            prime = False
        else:
            prime = True
        
    if prime == True:
        print(k," is prime ")
    else :
        print(k," is not prime ")

        
if __name__ == '__main__':
    main()
