def combinationSum(candidates, target):
    candidates = sorted(candidates)
    re = []
    def dfs(candidates, target, select=[], last=0):
        if target in candidates and target >= last:
            re.append(select + [target])
        [dfs(candidates, target - i, select + [i], i) for i in candidates if target - i > 0 and i >= last]
    dfs(candidates, target)

    if re:
        return len(sorted(re, key=lambda x: len(x))[0])
    else:
        return -1

assert (combinationSum([3,5],5)) == 1
assert (combinationSum([3,5],6)) == 2
assert (combinationSum([3,5],7)) == -1