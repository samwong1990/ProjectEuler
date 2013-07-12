import platform
import itertools

def fib(n):
	a = 0
	b = 1
	for _ in range(n):
		yield b
		a,b = b, a+b

def fibsUpTo(n):
	return itertools.takewhile(lambda x: x<n, fib(n))

def evenFibsUpTo(n):
	return filter(lambda x: x % 2 == 0, fibsUpTo(n))

if __name__ == '__main__':
	print(sum(evenFibsUpTo(4*10**6)))