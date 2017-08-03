words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
newWords = words.replace('day', 'month')
print newWords
# =========================================
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

# ===========================
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0],x[len(x)-1]

# ++++++++++++++++++++++++++++++++++++

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print "sorted s:", x
y= x[:len(x)/2]
z = x[len(x)/2:]
print y
print z
z.insert(0,y)
print z
# ==========================================
