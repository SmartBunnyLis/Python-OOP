
arr = ['hello','world','my','name','is','Anna']
char = 'o'

def find(arr):
    newArr = []
    for element in arr:
        for letter in element:
            if letter == char:
                newArr.append(element)
    print newArr
find(arr)
