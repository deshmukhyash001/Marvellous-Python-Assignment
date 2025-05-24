def arrInp(no_of_element):
    arr = []
    for i in range(no_of_element):
        arr.append(int(input()))
        
    return arr

def maxx(arr):
    max = 0 
    for i in arr:
        if i > max:
            max = i
            
    return max