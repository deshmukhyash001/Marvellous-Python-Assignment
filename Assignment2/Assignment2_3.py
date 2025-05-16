def facto(n): 
    fact = 1 
    res = 1
    
    while fact<=n and fact>=1:
        res *= fact
        fact += 1
    return res

def main():
    
    print("Enter a number : ")
    num = int(input())        
    print(facto(num))    
    
if __name__ == "__main__":
    main()