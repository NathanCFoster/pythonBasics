for x in range(0, 151): 
    print(x)

for y in range(5, 10001, 5):
    print(y)

for c in range(1,100):
    if(c % 5 == 0):
        print("divisible by 5: " + str(c) + "Coding")
    elif(c % 10 == 0):
        print("divisible by 10: " + str(c) + "Coding Dojo")

sum = 0
for s in range(0, 500000):
    if(s % 2 == 1):
        sum += s
print(sum)

for f in range(2018, 0, -4):
    print(f)

lowNum = 2
highNum = 9
mult = 3
for n in range(lowNum, highNum+1):
    if(n % mult == 0):
        print(n)
