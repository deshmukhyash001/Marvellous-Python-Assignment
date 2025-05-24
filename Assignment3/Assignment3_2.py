import Assignment5.basic as basic
def main():

    print("How many elements you want to store in array : ")
    list1 = basic.arrInp(int(input()))
    j = list1[0]
    for i in list1:
        if i > j:
            j = i
            
    print("maximum from array is: ",j)
                
if __name__ == "__main__":
    main()