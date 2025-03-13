'''#tuples
academic_tuple = ('name','fathername','reg number','CNIC number')
print(academic_tuple)
'''

#with for
'''sum = ('a',)
for i in range(5):
    name = int(input('Enter a number: '))
    sum = i+name
    print(sum)
'''


'''#accessing tuple elements
fruits =('fruits','banana')
print(fruits[0])
print(fruits[-1])
'''

'''#CONCATENATION
tuple1 = ('hello')
tuple2 = ('Bye')
combined = tuple1 + tuple2
print(combined)
'''

'''
#repition
tuple3 = ('O-O','        _-')
repeat = tuple3*900
print(repeat)
'''

'''#slicing
numbers = (0,2,3,5)
print(numbers[2:4])
'''

'''#methods
tuple5 = ('apple', 'banana', 'cherry', 'sugar')
print(tuple5.count('a'))
print(tuple5.index('cherry'))
'''

'''#counting letters


my_tuple = ('hello', 'world', 'python','bello')
letter_to_count = input('Enter a letter to know the occurence: ')
element = my_tuple[0] #for one element
count_elemnt = element.count(letter_to_count)
print(f"Letter '{letter_to_count}' repititions in the element '{element}':{count_elemnt}'")

#for whole tuple
count_all = 0
for string in my_tuple:
    count_all +=string.count(letter_to_count)
print(f"Letter '{letter_to_count}' repititions in the tuple: {count_all}")
'''


#break, continue

for num in range(9,9000):
    if num == 900/4:
        break
    print(num)

for num in range(9,20):
    if num ==12:
        continue
    print(num)
