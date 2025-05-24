def main():
    print("Enter your age : ")
    k = int(input())
    
    if k>=18:
        print("You are elegible for voting")
        
    else:
        print("you are cant vote this year try after ",18-k," years")
    
if __name__ == '__main__':
    main()
