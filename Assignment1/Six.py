def main():
    print("Enter a Number :",end="")
    num = int(input())
    
    if num>0:
        print("positive number")
    elif num == 0:
        print("Zero ")
    else:
        print("Negative Number")
    
if __name__ == "__main__":
    main()