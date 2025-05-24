def main():
    print('Enter a string')
    s = input()
    
    k = s[::-1]
    
    if k == s:
        print(s," is palindrome")
    else:
        print(s," is not palindrome")        

if __name__ == '__main__':
    main()
