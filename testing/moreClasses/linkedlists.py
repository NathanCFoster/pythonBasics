class SList:
    def __init__(self):
        self.head = None
    def addToFront(self,val):
        newNode = SLNode(val)
        currentHead = self.head
        newNode.next = currentHead
        self.head = newNode
        return self
    def printValues(self):
        print("\nCurrent Values:")
        runner = self.head
        while(runner != None):
            print(runner.val)
            runner = runner.next
        return self
    def addToBack(self, val):
        newNode = SLNode(val)
        runner = self.head
        if(runner != None):
            while(runner.next != None):
                runner = runner.next
            runner.next=newNode
        else:
            self.head = newNode
        return self
    def removeFromFront(self):
        #pretty sure it meant to print not return its value
        print(self.head.val)
        self.head = self.head.next
        return self
    def removeFromBack(self):
        runner = self.head
        while(runner.next.next != None):
            runner = runner.next
        print(runner.next.val)
        runner.next = None
        return self
    def removeVal(self, val):
        runner = self.head
        while(runner.next != None):
            if(val == runner.next.val):
                print(runner.next.val)
                runner.next = None
            else:
                runner = runner.next
        return self
    def insertAt(self, val, n):
        runner = self.head
        newNode = SLNode(val)
        if(n == 0):
            newNode.next = self.head
            self.head = newNode
        else:
            for x in range(0, n):
                if(x == n-1):
                    newNode.next = runner.next
                    runner.next = newNode
                elif(runner.next != None):
                    runner = runner.next
        return self
    def debugNext(self):
        runner = self.head
        while(runner.next != None):
            print("runner %s" %(runner.val))
            runner = runner.next
        return self

class SLNode:
    def __init__(self, val):
        self.val = val
        self.next = None

myList = SList()
myList.addToBack("STUPID!").addToFront("is").addToFront("THIS").printValues()#this line is why its stupid
myList.addToBack("this").removeFromFront().addToFront("brain").removeFromBack().removeVal("STUPID!").insertAt("smart", 4).debugNext().printValues()
#Not sure what edge cases are...