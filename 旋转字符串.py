class Solution:
    # 参数s: 字符串列表
    # 参数offset:整数
    # 返回值：无
    def rotateString(self,s,offset):
        if len(s) > 0:
            offset = offset % len(s)
        temp = (s + s)[len(s) - offset : 2 * len(s) - offset]
        for i in range(len(temp)):
            s[i] = temp[i]

#主函数
if __name__ == '__main__':
    s = ['a','b','c','d','e','f','g']
    offset = 3
    print("输入：s = {}, offset = {}".format(s,offset))

    solution = Solution()
    solution.rotateString(s,offset)

    print("输出：s = {}".format(s))

