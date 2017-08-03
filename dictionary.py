
ali = {
    "name":"ali",
    "age":"33",
    "country of birth":"Iran",
    "language":"farsi"
}

# def prints(name):
#     print name
# prints(ali)
#prints all keys --> name,age,language....
for key,data in ali.iteritems():
    print key,"=",data
    