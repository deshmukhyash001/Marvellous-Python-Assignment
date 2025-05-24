def main():
    k = ('a','e','i','o','u')
    
    print("Enter a character : ")
    c = input()
    
    if c.lower() in k:
        print(c," is vovel")
    else:
        print(c," is consonent")
if __name__ == '__main__':
    main()
