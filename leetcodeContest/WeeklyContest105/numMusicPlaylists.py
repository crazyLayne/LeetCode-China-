import math
class Solution:
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        # cur表示当前在选第几首歌，unvisited表示还有几首歌从未选过，wait表示在等待的歌
        def count(cur, unvisited, N, L, K, d):
            wait = min(K, cur)
            if cur>=L: 
                d[(cur, unvisited)] = 1
                return 1     #遍历完毕
            rem = L-cur     #剩余rem首歌
            if rem==unvisited: 
                d[(cur, unvisited)] = math.factorial(unvisited)
                return  d[(cur, unvisited)]     #剩余的歌刚好给unvisited
            visited = N-wait-unvisited          #可以选的听过的歌且不用等待的
            # 从visited里选一首，或者从unvisited里选
            r1 = count(cur+1, unvisited, N, L, K, d)*visited if (cur+1, unvisited) not in d else d[(cur+1, unvisited)]*visited
            r2 = count(cur+1, unvisited-1, N, L, K, d)*unvisited if (cur+1, unvisited-1) not in d else d[(cur+1, unvisited-1)]*unvisited
            d[(cur, unvisited)] = r1 + r2
            return d[(cur, unvisited)]
        d = {}
        return count(0, N, N, L, K, d)%(10**9+7)

# N = 2; L = 3; K = 1
# N = 2; L = 3; K = 0
# N = 3; L = 3; K = 1
N = 37; L = 50; K = 8
S = Solution()
print(S.numMusicPlaylists(N, L, K))