class Solution(object):
    def reconstructQueue(self, people):
    	if not people:
    		return []

    	peopledct, height, res = {}, [], []
    	# Record height queue info
    	for i in range(len(people)):
    		p = people[i]
    		 # if the person with same height appeared before, then add height and its pos to the list
    		if p[0] in peopledct:
    			peopledct[p[0]] += [(p[1], i)]
    		# if this height is new to the record, we record the height and add to the book
    		else:
    			peopledct[p[0]] = [(p[1], i)]
    			height += [p[0]]

    	height.sort()
    	# we loop from tallest to smalles
    	for h in height[::-1]:
    		# perform in-group sort for each group of people with same height
    		peopledct[h].sort()
    		for p in peopledct[h]:
    			# we insert it to the exisitng queue, note that k is the relative position
    			res.insert(p[0], people[p[1]])
    	return res

people =  [[7,1], [4,4], [7,0], [5,0], [6,1], [5,2]]
s = Solution()
print(s.reconstructQueue(people) == [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]])

# Solution 2

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # we first sort the list by height then sort it by positiion
        people = sorted(people, key = lambda x: (-x[0], x[1])) # it means that we first sort list by height(negative gives an descending order), then sort it by k
        # new people [[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]
        res = []
        for p in people:
            res.insert(p[1], p)
        return res

s = Solution()
print(s.reconstructQueue(people) == [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]])