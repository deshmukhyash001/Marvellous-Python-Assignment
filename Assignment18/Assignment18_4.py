import hashlib

def main():

    print("Enter 1st file name")
    fName = open(input(),"r")


    print("Enter 2nd file name")
    fName2 = open(input(),"r")

    Data = fName.read()
    Data2 =  fName2.read()

    a = hashlib.md5(b"")
    b = hashlib.md5(b"{Data}")

    print(list(a))
if __name__ == '__main__':
    main()
