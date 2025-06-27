def main():
    print("Enter a Number ")
    f_Name = open(input(),"r")
    Data = f_Name.read()
    
    word = input()
    count = 0
    
    Data.split(" ")
    for i in Data:
        if i == word:
            count += 1


if __name__ == '__main__':
    main()
