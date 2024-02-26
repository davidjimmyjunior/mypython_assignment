my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
my_list.insert(1, 15)
print(my_list)
my_list.extend([50, 60, 70])
print(my_list)
my_list.pop()
print(my_list)
my_list.sort()
print(my_list)
index_30 = my_list.index(30)
print(index_30)


def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d
    return inner_fun(a, b)

res = outer_fun(5, 10)
print(res)

def display(**kwargs):
    for i in kwargs:
        print(i)

display(emp="Kelly", salary=9000)

def add(a, b):
    return a+5, b+5

result = add(3, 2)
print(result)

for num in range(1, 5):
    print(num)
"""
    def some_thing(number1, number2):
    first_value = number1 + 8
    second_value = number2 - 5
    return first_value

print(some_thing(13, 10))
"""
x = 0
while x < 10:
    x = x + 1

 x = 0
for i in range(3):
    x = x + i   