
N = int(input())

serie = list(range(N+1))

print(sum(serie))

''' another solution:

t = 0
ix = 0

for i in serie:
	t += serie[ix]
	ix += 1

print(t)
'''

'''yet another one'''

def suma(N):
	res = 0
	for i in range(N+1):
		res += i
	return res

print(suma(100))