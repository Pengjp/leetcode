# MajorityElementII.py
# keep two candidates and two counters

import collections

def majorityElement(nums):
    ctr = collections.Counter()
    for n in nums:
        ctr[n] += 1
        if len(ctr) == 3:
            ctr -= collections.Counter(set(ctr))
    return [n for n in ctr if nums.count(n) > len(nums)/3] # second path to check

nums=[1,1,1,3,3,2,2,2]
print(majorityElement(nums))
