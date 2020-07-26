def combinationSum(candidates, target):
    def dfs(remain, combo, index):
        if remain == 0:
            result.append(combo)
            return
        for i in range(index, len(candy)):
            if candy[i] > remain:
                break #
            
            dfs(remain - candy[i], combo + [candy[i]], i)
            
    candy = sorted(candidates)
    result = []
    dfs(target, [], 0)

    if not result:
        return -1
    return result

def getUmbrellas(requirement, sizes):
    def helper(rest, combo, index):
        if rest == 0:
            results.append(combo)
            return
        for i in range(index, len(candy)):
            if candy[i] > rest:
                # exceeded the sum with candidate[i]
                break #the for loop
            
            helper(rest - candy[i], combo + [candy[i]], i)
            
    candy = sorted(sizes)
    results = []
    helper(requirement, [], 0)
    if not results:
        return -1
    else:
        return(len(sorted(results, key=lambda x:len(x))[0]))

print(getUmbrellas(755,[3,5]))
# li = [[4,5,6],[1],[1,3]]

def func(string):
    if not string:
        return ""

    queue = list(string)
    cur = queue.pop(0)
    cur_cnt = 1
    ret = []
    while queue:
        temp = queue.pop(0)
        if temp == cur:
            cur_cnt += 1
        else:
            if cur_cnt == 1:
                ret.append(cur)
            else:
                ret.append("%s%s" % (cur, cur_cnt))
            cur = temp
            cur_cnt = 1
    
    if cur_cnt == 1:
        ret.append(cur)
    else:
        ret.append("%s%s" % (cur, cur_cnt))

    return "".join(ret)

print(func('abaabbbc'))
import numpy as np

total = []
for i in range(10000):
    a,b=0,0
    count = 0
    while a < 5 or b < 5:
        if np.random.uniform() < 0.5:
            a += 1
        else:
            b += 1
        if a == b:
            count +=1
    total.append(count)

print(np.mean(total))
