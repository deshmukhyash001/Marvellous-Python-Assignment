def main():
    print('Enter a number')
    num = int(input())
    
    sq = lambda no : no**2
    qb = lambda no : no**3
    
    print("square : ",sq(num))
    print("cube : ",qb(num))
    

if __name__ == '__main__':
    main()
