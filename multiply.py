a=[1,2,3]
arr = a
newArr=[]

def multiply():
  # multiply by 5 function
    for number in arr:
        total=number*5        
        newArr.append(total)
    print newArr
multiply()