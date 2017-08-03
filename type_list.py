l = ['magical unicorns','hello','world', 5,3]
# l = [2,3,1,7,4,12]

array = l
string = ''
total = 0
for i in array:
    
    if isinstance(i,str):
        print "String: ", " ".join(array)
        print "The list you entered is of string type"
        break
    elif isinstance(i,int):
        total += sum(array)
        print "The list you entered is of integer type"
        print "Sum: ", total
        break
    
# if isinstance(i,str):
#     if isinstance(i, int):
#         print "The list you entered is of mixed type"
#         print "String: ", " ".join(array)
#         print "Sum: " , sum(array)
        

        

