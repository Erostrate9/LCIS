def LCIS(S, T):
    m = len(S)
    n = len(T)
    dp = [0 for x in range(max(m,n))]
    prev = [[-1 for x in range(n)] for y in range(m)]
    lcis = ['' for x in range(min(m, n))]
    for i in range(m):
        # l stands for the length of LCIS
        # p stands for the end of LCIS
        # p must < s[i]
        l, p = 0, -1
        for j in range(n):
            if S[i] == T[j]:
                if dp[j] < l + 1:
                    dp[j] = l + 1
                    prev[i][j] = p

            if T[j] < S[i]:
                if dp[j] > l:
                    l = dp[j]
                    p = j
    l=0
    p=-1
    for i in range(n):
        if (dp[i] > l):
            l = dp[i]
            p = i
    j, k = p, l
    for i in range(m - 1, -m-n, -1):
        if (i<0 or prev[i][j] != -1):
            k -= 1
            lcis[k] = T[j]
            j = prev[i][j]
        if k <= 0:
            break
    return l, lcis


def __main__():
    S = [1, 2, 4, 3, 4,5,8,7,1,2,4,8]
    T = [4, 2, 1, 4, 2, 3, 1,12,3,5,6,7,8,1,2,4]
    l, lcis = LCIS(S, T)
    print("Length of LCIS is", l)
    print("LCIS is:")
    for i in range(l):
        if lcis[i] != '':
            print(lcis[i], end=',')


if __name__ == '__main__':
    __main__()
