'''

*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  
*  *  *  *  *  *  *  *       L I S T A S        *  *  *  *  *  *  *  *  
*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  


m = [
	[1, 2, 3],
	[4, 5, 6]
	]

print(m[1][2])


strg = "Hello world!"
print(strg[5])


nums = [1,2,3]
print(nums + [4,5,6])
print(nums * 3)


words = ['spam', 'egg', 'spam', 'sausage']
print('spam' in words)
print('egg' in words)
print('tomato' in words)


nums = [1,2,3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)


words = ['hello', 'world', 'spam', 'eggs']
for word in words:
	print(word + '!')


strg = 'testing for loops'
count = 0

for x in strg:
	if(x == 't'):
		count += 1

print(count)


numbers = list(range(3,20,4))
	# primer argumento: inicio, segundo: final (excluído), tercero (step): intervalo
#numbers = range(10)  <<--da cualquiera
numbers2 = list(range(20,3,-2))
	# así se da vuelta el rango
print(numbers2)


for i in range(5):
	print('hello!')
	#print(list('hello!'))  <<--así da cualquiera de nuevo


squares = [0,1,4,9,16,25,36,49,64,81]
print('El largo de squares es: ' + str(len(squares)))
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])
print()
print(squares[:7])
print(squares[7:])
print()
print(squares[::2])
print(squares[2:8:])
print()
print(squares[1:-1])
print(squares[::-1])
print()


sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#      0  1  2  3  4   5   6   7   8   9
print(sqs[7:5:-1])


lista = [1,1,2,3,5,8,13]
print(lista[lista[4]])


for i in range(10):
	if not i % 2 == 0:
		print(i+1)


*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  
*  *  *  *  *  *  *  *    F U N C I O N E S     *  *  *  *  *  *  *  *  
*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  


nums = [1,3,5,2,4]
letters = 'hola muchedumbre'

print(len(nums))
print(len(letters))


nums = [1,2,3]
nums.append(4)
print(nums)


words = ['Python', 'fun']
index = 1
words.insert(index, 'is')
print(words)

words = 'Python fun'
words.insert(8, 'is')  <<--no funciona así
print(words)


letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('z'))


letters = ['p', 'q', 'r', 's', 'p', 'u']
print(max(letters))
print(min(letters))
print(letters.count('p'))
print(letters.remove('s'))
print(letters.reverse())


sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
sqs.remove(25)
print(sqs)
print()
sqs.reverse()
print(sqs)


nums = [4,5,6]
msg = 'Numbers: {0} {1} {2}'. format(nums[0], nums[1], nums[2])
print(msg)


msg = 'Numbers: {0} {1} {2}'. format(4,5,6)
print(msg)


msg = 'Numbers: {} {} {}'. format(4,5,6)
print(msg)


import platform as p
print(p.pyton_version(), p.python_build()[1])


# este bien clarito
print("{0}{1}{0}".format("abra", "cad"))


msg = "{x}, {y} ".format(x=5, y=12)
print(msg)


print('alto '.join(['spam', 'eggs', 'ham']))
#imprime 'spamalto eggsalto ham'

print('Hello ME'.replace('ME', 'world'))
#imprime 'Hello world'

print('This is a sentence.'.startswith('This'))
print('This is a sentence.'.endswith('This'))

print('This is a sentence.'.upper())
print('SON TODOS ALTOS'.lower())

print('spam., eggs., ham.'.split(', '))
#imprime ['spam.', 'eggs.', 'ham.']


def my_function():
	print('spam')
	print('spam')
	print('spam')

#my_function()

def my_function_2(n):
	print('spam\n' * n)

my_function_2(3)


def hello():
	print('Hello world!')

hello()
hello()
hello()


def print_with_exclamation(word):
	print(word + '!')

print_with_exclamation('spam')
print_with_exclamation('eggs')
print_with_exclamation('python')


def print_sum_twice(x, y):
	print(x + y)
	print(x + y)

print_sum_twice(5,8)


def maxi(x, y):
	if x >= y:
		return x
	else:
		return y

print(maxi(4, 7))
z = maxi(8, 5)
print(z)


def add_numbers(x, y):
	total = x + y
	return total
	print('This won\'t be printed')

print(add_numbers(4,5))



def shout(word):
'''
#Docstring explaining the function
#Print a word with an
#exclamation mark following it.
'''
	print(word + '!')

shout('spam')


def suma(x):
	res = 0
	for i in range(x+1):
		res += i
	return res

print(suma(100))
'''

print(list(range(4)))