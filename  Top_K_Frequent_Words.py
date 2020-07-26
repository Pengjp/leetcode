import collections
def topKFrequent(nums, k):
	c = collections.Counter((nums))
	li = c.most_common(k)
	return [i[0] for i in li]  


print(topKFrequent(nums = [1,1,1,2,2,3], k = 2) == [1,2])
