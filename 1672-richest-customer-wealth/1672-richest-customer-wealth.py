class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        list = []

        for i in range(len(accounts)):
            list.append(sum(accounts[i]))
            
        return max(list)