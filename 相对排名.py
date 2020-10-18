# num = [5,4,3,2,1]
# score = {}
# for i in range(len(num)):
#     score[num[i]] = i
#     print("score = ",score)
# sortedScore = sorted(num,reverse=True)
# print("sortedScore = ",sortedScore)
# answer = [0] * len(num)
# print("answer = ",answer)


class Solution:
    # 参数nums:整数列表
    # 返回列表
    def findRelativeRanks(self,nums):
        score = {}
        for i in range(len(nums)):
            score[nums[i]] = i
            print("score=",score)
        sorteScore = sorted(nums,reverse=True)
        answer = [0] * len(nums)
        for i in range(len(sorteScore)):
            res = str(i + 1)
            if i == 0:
                res = 'Gold Medal'
            if i == 1:
                res = 'Silver Medal'
            if i == 2:
                res = 'Bronze Medal'
            answer[score[sorteScore[i]]] = res
        return answer




#主函数
if __name__ == '__main__':
    num = [5,6,7,3,2,1]
    s = Solution()
    print("输入：",num)
    print("输出：",s.findRelativeRanks(num))