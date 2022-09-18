class Solution:
    def minimumSum(self, num: int) -> int:
        new1 = []
        new2 = []
        num_li = sorted(list(str(num)))
        for i in range(len(num_li)):
            if i % 2 == 0:
                new1.append(num_li[i])
            else:
                new2.append(num_li[i])
        new1 = int(''.join(new1))
        new2 = int(''.join(new2))
        return new1 + new2