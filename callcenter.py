class Call(object):
    def __init__(self,idNum, callerName, phone, time, reason):
        self.idNum = idNum
        self.time = time
        self.reason = reason
        self.phone = phone
        self.callerName = callerName
    
    def display(self):
        print self.idNum,self.callerName,self.time,self.reason,self.phone

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = len(self.calls)

    def add(self,call):
        self.calls.append(call)
        return self

    def remove(self,call):
        self.calls.pop()
        return self


    def info(self):

        for i in caller2.calls:
            print i.callerName,i.phone

caller1 = Call(1,"Liz",111111111, "10pm", "'none of your biz'")
caller3 = Call(123456,"Lasdasasiz",11154454111111, "10pm", "'none ofasdasdsda your biz'")
caller2 = CallCenter()

caller2.add(caller3).add(caller1).remove(caller3)
caller2.info()
