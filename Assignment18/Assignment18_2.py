def main():
    print("Enter a file name")    
    fName = input()

    Fobj = open(fName,'r')
    print(Fobj.read())


if __name__ == '__main__':
    main()
