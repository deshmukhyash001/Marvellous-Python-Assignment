def main():
    k = 0
    for i in range(1,100+1):
        if i%2 == 0 :
            k += i
    
    print(f"Sum of even numbers between 1 to 100 is: {k}")
if __name__ == '__main__':
    main()
