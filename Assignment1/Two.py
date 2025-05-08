def ChkNum(num):
    if num%2 == 0:
        print("Even Number")
    else :
        print("Odd  Number")

def main():
    print("Enter a Number :",end=" ")
    num = int(input())
    
    ChkNum(num)
    
if __name__ == "__main__":
    main()