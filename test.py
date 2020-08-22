li = []
for i in range(1,100000):
	li.append(str(i))
n = 0
ans=[]
for i in li:
	if '11' in i:
		n+=1
		ans.append(i)
print(n)
# print(ans)