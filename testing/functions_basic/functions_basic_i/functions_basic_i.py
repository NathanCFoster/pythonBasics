#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# It should print 5... it does

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# Most likely undefineed, or maybe undefined 5... undefined

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#Prints 5

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#Prints 5

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# Prints 5... it also prints none? Most likely because when x is created it doesn't get a value, the function is just printing 5

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#Prints 3 and 5 and none... its actually an error because its trying to add two null values

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#Prints 7... its actually 25 because it returns the values as strings, so 3 + 5 would be 35... might be useful for a calculator

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#prints 100, 10

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#prints 7, 14 and 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#Prints 8

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#prints 500, 500, 300, 300... the last print is actually 500 so it seems like it temporarily sets the var b as 300 inside the function

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#prints 500 500 300 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#prints 500 500 300 300... this time it sets b outside of the function so it would not be a temp value

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#prints 1 3 2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#prints 1 3 5 10