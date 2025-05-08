def Add(num1,num2):
    return num1+num2

def main():
    print("Enter First Number :",end=" ")
    num1 = int(input())
    
    print("Enter Second Number :",end=" ")
    num2 = int(input())
    
    print(Add(num1,num2))
    
if __name__ == "__main__":
    main()