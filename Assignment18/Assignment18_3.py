def main():
    print("Enter a file name")
    fObj = open(input(),'r')

    Data = fObj.read()
    fObj.close()

    fObj = open("Demo.txt","w")
    fObj.write(Data) 

if __name__ == '__main__':
    main()
