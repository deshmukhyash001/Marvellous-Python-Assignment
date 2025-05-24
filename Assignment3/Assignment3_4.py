import Assignment5.basic as basic

def main():
    
    print("How many elements you want to store in array : ")
    list1 = basic.arrInp(int(input()))
    print("Element to find : ")
    k = int(input())
    j = 0
    for i in list1:
        if i == k :
            j+=1
        
    print(f"Frequency of element {k} is: ",j)
    
    
if __name__ == "__main__":
    main()