import os
def main():
    print("Enter a file name : ")    
    fName = input()

    print("Yes available ") if os.path.exists(fName) else print("not available")

if __name__ == '__main__':
    main()
