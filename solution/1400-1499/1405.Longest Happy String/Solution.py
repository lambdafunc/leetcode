class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = []
        if a > 0:
            heapq.heappush(h, [-a, 'a'])
        if b > 0:
            heapq.heappush(h, [-b, 'b'])
        if c > 0:
            heapq.heappush(h, [-c, 'c'])

        ans = []
        while len(h) > 0:
            cur = heapq.heappop(h)
            if len(ans) >= 2 and ans[-1] == cur[1] and ans[-2] == cur[1]:
                if len(h) == 0:
                    break
                nxt = heapq.heappop(h)
                ans.append(nxt[1])
                if -nxt[0] > 1:
                    nxt[0] += 1
                    heapq.heappush(h, nxt)
                heapq.heappush(h, cur)
            else:
                ans.append(cur[1])
                if -cur[0] > 1:
                    cur[0] += 1
                    heapq.heappush(h, cur)


        return ''.join(ans)
