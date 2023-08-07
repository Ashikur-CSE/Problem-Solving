def solve(s):
  n = len(s)
  dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
  for i in range(n):
    for j in range(n):
      if i == 0 or j == 0:
        dp[i][j] = 0
      elif s[i - 1] == s[j - 1]:
        dp[i][j] = dp[i - 1][j - 1] + 1
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
  return dp[n - 1][n - 1]

def main():
  t = int(input())
  for _ in range(t):
    n = int(input())
    s = input()
    print(solve(s))

if __name__ == "__main__":
  main()