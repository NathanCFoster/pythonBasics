
def couuntdown(num):
    nums = []
    for x in range(num, 0, -1):
        nums.append(x)
    return nums
print(couuntdown(3))

def printAndReturn(num1, num2):
    print(num1)
    return num2
print(printAndReturn(1,2))

def firstPlusLength(arr):
    return arr[0] + len(arr)
print(firstPlusLength([1,3,4]))

def valueGreaterThanSecond(arr):
    newArr = []
    for x in range(0, len(arr)):
        if(arr[x] > arr[1]):
            newArr.append(arr[x])
    return newArr
print(valueGreaterThanSecond([0,1,2,3,4]))

def lengthAndValue(length = 3, value = 4):
    arr = []
    for x in range(0,length):
        arr.append(value)
    return arr
print(lengthAndValue())
print(lengthAndValue(5,8))