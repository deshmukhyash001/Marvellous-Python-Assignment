def divFive(num):
    if num%5 ==0:
        return True
    else:
        return False

def main():
    print("Enter a number :",end="")
    num = int(input())
    print(divFive(num))
    
if __name__ == "__main__":
    main()