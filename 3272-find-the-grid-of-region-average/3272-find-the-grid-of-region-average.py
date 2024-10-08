from collections import defaultdict

class Solution:
    def resultGrid(self, v, k):
        r, c = len(v), len(v[0])
        m = defaultdict(lambda: [0, 0])

        for i in range(r - 2):
            for j in range(c - 2):
                s, f = 0, 0

                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        s += v[x][y]

                        if x + 1 < i + 3 and abs(v[x][y] - v[x + 1][y]) > k:
                            f = 1
                            break

                        if y + 1 < j + 3 and abs(v[x][y] - v[x][y + 1]) > k:
                            f = 1
                            break

                    if f == 1:
                        break

                if f == 1:
                    continue

                s = s // 9

                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        m[x, y][0] += s
                        m[x, y][1] += 1

        ans = [[0] * c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                if (i, j) in m:
                    s, count = m[i, j]
                    ans[i][j] = s // count
                else:
                    ans[i][j] = v[i][j]

        return ans