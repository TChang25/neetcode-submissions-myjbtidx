class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            flag = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    flag = 1
                    res.append(j - i)
                    break
            if flag == 0:
                res.append(0)
        return res