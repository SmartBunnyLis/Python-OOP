arr=[1,3,5]
arr2=[4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw(arr):
    for element in arr:
        print element*"*"
draw(arr)


def draw2(arr2):
    for element in arr2:
        if isinstance(element,int):
            print element*"*"
        elif isinstance(element,str):
            newEl = len(element)
            print newEl*(element[0].lower())
draw2(arr2)

