# LCIS
Longest Common Increasing Subsequence，最长公共增长子序列

$dp[i,j]表示a_{1}～a_i和b_1～b_j所能构成的以b_j结尾的LCIS的长度$

当$a_i\neq b_j$时，有$dp[i,j]==dp[i-1,j]$

当$a_i= b_j$时，有$$dp[i,j]=\max \limits_{0\leq k<j,b_k<b_j}\{dp[i-1,k]\}+1=\max \limits_{0\leq k<j,b_k<a_i}\{dp[i-1,k]\}+1$$

