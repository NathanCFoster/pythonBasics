import random
class product:
    def __init__(self, name, price, category, num):
        self.name = name
        self.price = price
        self.category = category
        self.numOfSelf = num
        self.ids = []
        self.usedIds = []
        for x in range(0, 30):
            self.usedIds.append(x)
        for x in range(0,num):
            ran = random.randint(0, len(self.usedIds)-1)
            self.ids.append(ran)
            self.usedIds.pop(ran)
        
    def printInfo(self):
        print("There are %d %ss for $%d in the %s aisle\nIds:\n%s" %(self.numOfSelf, self.name, self.price, self.category, self.ids))
    def updatePrice(self, change, isIncreased):
        if(isIncreased == True):
            self.price *= change
        else:
            self.price /= change
    def sell(self, id):
        self.numOfSelf -= 1
        for x in range(0,len(self.ids)-1):
            if(self.ids[x] == id):
                self.ids.pop(x)
                return self
    def randSell(self):
        self.numOfSelf -=1
        ran = random.randint(0, len(self.usedIds))
        self.ids.pop(ran-1)
            
