# python算法：动态规划dynamic programming
# DP:寻找多封装下最优解的过程
# 原理：先解决相对简单的子问题，再逐步解决大问题

# 实现：
# 1、状态list的构建，list[i][j]的含义以及i和j与待分析内容的关系
# 2、在for循环中递归关系是如何



# 问题： 背包问题
# 每样东西都有相应的价值，可呆呆的他在收拾背包时发现，
# 他的背包最大容量只有6斤，装不下所有的东西，只能从这堆东西中挑选 组合价值 最高的物品

# ==========================================================================

# constraint: 只能拿一次相同物品

# def dynamic_p() -> list:
#     items = [                                       # 物品属性
#         {"name": "水", "weight": 3, "value": 10},
#         {"name": "书", "weight": 1, "value": 3},
#         {"name": "食物", "weight": 2, "value": 9},
#         {"name": "小刀", "weight": 3, "value": 4},
#         {"name": "衣物", "weight": 2, "value": 5},
#         {"name": "手机", "weight": 1, "value": 10}
#     ]
#     max_capacity = 6             # constrain: 最大背包重量
#     # 构造一个list：维度：(item_size+1) * (max_capacity+1)
#     dp = [[0]*(max_capacity + 1) for _ in range(len(items) + 1)]
#
#     for row in range(1, len(items) + 1):                # +1处理是因为range是左闭右开形式
#         for col in range(1, max_capacity + 1):
#             weight = items[row-1]["weight"]
#             value = items[row-1]["value"]
#
#             if weight > col:
#                 dp[row][col] = dp[row-1][col]
#             else:
#                 dp[row][col] = max(value + dp[row-1][col-weight], dp[row-1][col])
#     return dp
#
#
# dp = dynamic_p()        # 得到最优解的函数
#
# for i in dp:
#     print(i)
#
# print(dp[-1][-1])       # 打印最优解


# ============================================================================
# constraint: 可重复拿相同物品

# def dynamic_p() -> list:
#     items = [                                       # 物品属性
#         {"name": "水", "weight": 3, "value": 10},
#         {"name": "书", "weight": 1, "value": 3},
#         {"name": "食物", "weight": 2, "value": 9},
#         {"name": "小刀", "weight": 3, "value": 4},
#         {"name": "衣物", "weight": 2, "value": 5},
#         {"name": "手机", "weight": 1, "value": 10}
#     ]
#     max_capacity = 6             # constrain: 最大背包重量
#     # 构造一个list：维度：(item_size+1) * (max_capacity+1)
#     dp = [[0]*(max_capacity + 1) for _ in range(len(items) + 1)]
#
#     for row in range(1, len(items) + 1):                # +1处理是因为range是左闭右开形式
#         for col in range(1, max_capacity + 1):
#             weight = items[row-1]["weight"]
#             value = items[row-1]["value"]
#
#             if weight > col:
#                 dp[row][col] = dp[row-1][col]
#             else:
#                 dp[row][col] = max(value + dp[row][col-weight], dp[row-1][col])    # 重复与否在这行code
#     return dp
#
#
# dp = dynamic_p()        # 得到最优解的函数
#
# for i in dp:
#     print(i)
#
# print(dp[-1][-1])       # 打印最优解

# 最长递增子序列

# def length_lis(nums: list) -> int:
#     length = len(nums)
#     dp = [1] * length
#
#     for i in range(len(nums)):
#         if nums[i] > nums[i-1]:
#             dp[i] = dp[i-1] + 1
#     print(dp)
#     return max(dp)
#
#
# nums = [6, 10, 9, 2, 3, 6, 10, 111, 66]
# print(length_lis(nums))

# ===========================================================
# 最长公共子串

# def dynamic_p(s1, s2) -> list:
#     r = len(s1)     #4,5
#     c = len(s2)
#     dp = [[0] * (c+1) for _ in range(r+1)]
#
#     for row in range(1, r+1):
#         for col in range(1, c+1):
#             if s1[row-1] == s2[col-1]:
#                 dp[row][col] = dp[row-1][col-1] + 1     #去拿行的上一个字符和列上一个字符的比较结果
#             else:
#                 dp[row][col] = 0
#     return dp
#
#
# dp = dynamic_p("beare", "beeear")
#
# max_str = 0
# for i in dp:
#     max_str = max(max_str, max(i))
#
# print(max_str)



# 求最长回文子串
# 算法：动态规划：dp[right][left]表示s[left:right]
def longestPalindrome(self, s: str) -> str:
    n = len(s)

    dp = [[0] * n for _ in range(n)]
    start, max_len = 0, 1

    for right in range(n):                      # dp[right][left]表示s[left:right]
        for left in range(right + 1):
            span = right - left + 1
            if span == 1:
                dp[right][left] = 1
            elif span == 2:
                dp[right][left] = s[right] == s[left]
            else:
                dp[right][left] = (s[right] == s[left]) and (dp[right - 1][left + 1])

            if dp[right][left]:
                if span > max_len:
                    max_len = span
                    start = left
    return s[start:start + max_len]