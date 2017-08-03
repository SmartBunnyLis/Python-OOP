class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *nums):
        for i in nums: 
            if type(i) is list or type(i) is tuple:
                for j in i:
                    self.result += j
            else:
                self.result += i 
        return self
     

    def subs(self, *nums):
        for i in nums: 
            if type(i) is list or type(i) is tuple:
                for j in i:
                    self.result -= j
            else:
                self.result -= i 
        return self
     
math1 = MathDojo()
print math1.add(2,(3,5)).subs(10).result
# print math1.add(2, [3,5]).subs(1, [2,3]).result
