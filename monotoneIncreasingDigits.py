# def func(N):
#     if N < 10: 
#         return N
#     A=list(str(N))

#     i, n = 0, len(A)

#     # identify the position when decrease occurs
#     while i < n - 1 and A[i] < A[i+1]: 
#         i += 1

#     # if i==n-1, that means no decrease
#     if i == n - 1: 
#         return N

#     # identify the position for equal situation
#     while i > 0 and A[i] == A[i - 1]: 
#         i -= 1
#     # subtract 1 for i and fill the remaining 9
#     A[i] = str(int(A[i]) - 1)
#     A[i+1:] = ['9'] * (n - i - 1)

#     for i in A:
#         print()
#     return int(''.join(A))

# print(func(997))
print("".join([for i in str(99)]))