# linear recursion
def good_fibonacci(n):
	if n<= 1:
		return(n, 0)
	else:
		(a, b) = good_fibonacci(n - 1)
		return (a+b, a)

print(good_fibonacci(5)[0])

def linear_sum(S, n):
	'''Return the sum of the first n numbers'''
	if n == 0:
		return 0
	else:
		return linear_sum(S, n-1) + S[n-1]

def reverse(S, start, stop):
	if start < stop - 1: # base case
		S[start], S[stop-1] = S[stop-1], S[start]
		reverse(S, start+1, stop-1)
def reverse_iterative(S):
	start, stop = 0, len(S)
	while start < stop-1:
		S[start], S[stop-1] = S[stop-1], S[start]
		start, stop = start+1, stop-1

def power(x, n):
	if n == 0:
		return 1
	else:
		return x * power(x, n-1)

def power(x, n):
	if n == 0:
		return 1
	else:
		partial = power(x, n//2)
		result = partial * partial
		if n % 2 == 1:
			result *= x
		return result