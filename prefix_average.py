# prefix_average.py

# Quadratic time algorithm 
def prefix_average1(S):
	'''Return list such that, for all j, A[j] equals average of S[0]. ..., S[j]'''
	n = len(S)
	A = [0]*n # create new list of n zeros
	for j in range(n):
		A[j] = sum(S[0:j+1]) / (j+1)
	return A

# Linear - Time Algorithm
def prefix_aberage2(S):
	n = len(S)
	A = [0] * n
	total = 0
	for j in range(n):
		total += S[j] # update prefix sum too include S[j]
		A[j] = total / (j+1)
	return A
# we use dynamic programming to save time by mainting an extra variable 