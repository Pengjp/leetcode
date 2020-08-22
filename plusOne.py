# plusOne.py
digits = [4,3,2,9]
def plusOne(digits):
	ans = str()
	for i in digits:
		ans += str(i)
	ans = int(ans) + 1
	return [int(i) for i in str(ans)]