def Prime(n):
    
    for i in range(1,n):
        if n%i == 0:
            return "number is not Prime"
    else:
        return "number is prime"

def main():
    print("Enter a number : ")
    num = int(input())
    print(Prime(num))
    
if __name__ == "__main__":
    main()