class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for x in nums:
            self.result += x
        return self
    def subtract(self, num , * nums):
        self.result -= num
        for x in nums:
            self.result -= x
        return self

md = MathDojo()
x = md.add(2).add(3,5,1).subtract(5,1).add(5,1,7,8).subtract(5,1,5,7).subtract(1).result
print(x)