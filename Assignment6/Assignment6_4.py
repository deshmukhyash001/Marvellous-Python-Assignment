def main():
    print("Enter a number : ",end="")
    
    k = int(input())
    facto = 1
    for i in range(k,0,-1):
        facto = facto*i
        
    print(facto)
if __name__ == '__main__':
    main()
