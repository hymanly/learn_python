class Solution:
    # 参数number:一个3位整数
    # 返回值：反转后的数字
    def reverseInteger(self,number):
        h = int(number / 100)
        t = int(number % 100 / 10)
        z = int(number % 10)
        return(100 * z + 10 * t + h)

# 主函数
if __name__ == '__main__':
    solution = Solution()
    num = int(input('输入一个3位整数：'))
    ans = solution.reverseInteger(num)
    print("输入：",num)
    print("输出：",ans)