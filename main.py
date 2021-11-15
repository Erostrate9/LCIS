# 未优化：O(nm^2)搜索做法
def LCIS_1(S, T):
    n = len(S)
    m = len(T)
    dp = [[0 for x in range(m+1)]for y in range(n+1)]
    a=[-(1<<30)]+S
    b=[-(1<<30)]+T
    for i in range(1,n+1):
        for j in range (1,m+1):
            dp[i][j]=dp[i-1][j]
            if a[i]==b[j]:
                for k in range(0,j):
                    if(b[k]<b[j]):
                        dp[i][j]=max((dp[i-1][k]+1),dp[i][j])
    l=dp[0][0]
    for i in range(1,m+1):
            l=max(l,dp[n][i])
    return l,dp

# 优化：O(nm)搜索做法
def LCIS_2(S, T):
    n = len(S)
    m = len(T)
    dp = [[0 for x in range(m+1)]for y in range(n+1)]

    a=[-(1<<30)]+S
    b=[-(1<<30)]+T
    for i in range(1,n+1):
        # k循环其实可省去，只需在j循环中记录当前LCIS的长度
        # l: the length of LCIS
        l,p=0,0
        for j in range (1,m+1):
            dp[i][j]=dp[i-1][j]
            if a[i]==b[j]:
                if dp[i][j]<l+1:
                    dp[i][j]=l+1
            elif a[i] > b[j]:
                if dp[i][j]>l:
                    l=dp[i][j]
    l=0
    for i in range(1,m+1):
        if (dp[n][i]>l):
            l=dp[n][i]
    return l,dp


# 优化：O(nm)搜索做法
# 构造LCIS
def LCIS_3(S, T):
    n = len(S)
    m = len(T)
    dp = [[0 for x in range(m + 1)] for y in range(n + 1)]
    prev = [[0 for x in range(m + 1)] for y in range(n + 1)]
    # prev数组储存a_1~a_i，b1~b_j所构成的且
    # 以b[j]为结尾的LCIS的倒数第二位元素在b中的编号
    a = [-(1 << 30)] + S
    b = [-(1 << 30)] + T
    for i in range(1, n + 1):
        # l: the length of LCIS
        # p: the end of LCIS
        l, p = 0, 0
        for j in range(1, m + 1):
            dp[i][j] = dp[i - 1][j]
            if a[i] == b[j]:
                if dp[i][j] < l + 1:
                    dp[i][j] = l + 1
                    prev[i][j] = p
            else:
                prev[i][j] = prev[i - 1][j]
            if a[i] > b[j]:
                if dp[i][j] > l:
                    l = dp[i][j]
                    p = j

    l, end = 0, 0
    for i in range(1, m + 1):
        if (dp[n][i] > l):
            l = dp[n][i]
            p = i
    lcis = [b[p]]
    while (prev[n][p] != 0):
        p = prev[n][p]
        lcis.append(b[p])
    return l, lcis


# 优化：O(nm)搜索做法
# 构造LCIS
# 简化dp数组存储结构
def LCIS_4(S, T):
    n = len(S)
    m = len(T)
    dp = [0 for x in range(m + 1)]
    prev = [[0 for x in range(m + 1)] for y in range(n + 1)]
    # prev数组储存a_1~a_i，b1~b_j所构成的且
    # 以b[j]为结尾的LCIS的倒数第二位元素在b中的编号
    a = [-(1 << 30)] + S
    b = [-(1 << 30)] + T
    for i in range(1, n + 1):
        # l: the length of LCIS
        # p: the end of LCIS
        l, p = 0, 0
        for j in range(1, m + 1):
            if a[i] == b[j]:
                if dp[j] < l + 1:
                    dp[j] = l + 1
                    prev[i][j] = p
            else:
                prev[i][j] = prev[i - 1][j]
            if a[i] > b[j]:
                if dp[j] > l:
                    l = dp[j]
                    p = j

    l, end = 0, 0
    for i in range(1, m + 1):
        if (dp[i] > l):
            l = dp[i]
            p = i
    lcis = [b[p]]
    while (prev[n][p] != 0):
        p = prev[n][p]
        lcis.append(b[p])
    return l, lcis


# 优化：O(nm)搜索做法
# 构造LCIS
# 简化dp数组存储结构
# 简化prev数组存储结构
def LCIS_5(S, T):
    n = len(S)
    m = len(T)
    dp = [0 for x in range(m + 1)]
    prev = [0 for x in range(m + 1)]
    # prev数组储存a_1~a_i，b1~b_j所构成的且
    # 以b[j]为结尾的LCIS的倒数第二位元素在b中的编号
    a = [-(1 << 30)] + S
    b = [-(1 << 30)] + T
    for i in range(1, n + 1):
        # l: the length of LCIS
        # p: the end of LCIS
        l, p = 0, 0
        for j in range(1, m + 1):
            if a[i] == b[j]:
                if dp[j] < l + 1:
                    dp[j] = l + 1
                    prev[j] = p
            if a[i] > b[j]:
                if dp[j] > l:
                    l = dp[j]
                    p = j

    l, end = 0, 0
    for i in range(1, m + 1):
        if (dp[i] > l):
            l = dp[i]
            p = i
    lcis = [b[p]]
    while (prev[p] != 0):
        p = prev[p]
        lcis.append(b[p])
    return l, lcis


def __main__():
    S = [-5, 4, 1, 23, 41, 8, 6, 7, 5, 9]
    T = [-5, 3, 1, 2, 5, 6, 8, 5, 7, 9]
    #     l, lcis = LCIS(S, T)

    l, lcis = LCIS_5(S, T)
    print("Length of LCIS is", l)
    print("LCIS is:")
    lcis.reverse()
    for i in lcis:
        print(i, end=',')


if __name__ == '__main__':
    __main__()