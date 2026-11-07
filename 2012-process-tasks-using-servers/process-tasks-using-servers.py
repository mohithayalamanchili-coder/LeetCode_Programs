import heapq
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:

        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        ans = []
        time = 0

        for j, task in enumerate(tasks):
            time = max(time, j)

            # Release all servers that are free
            while busy and busy[0][0] <= time:
                end, w, i = heapq.heappop(busy)
                heapq.heappush(available, (w, i))

            # Wait if no server is available
            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    end, w, i = heapq.heappop(busy)
                    heapq.heappush(available, (w, i))

            w, i = heapq.heappop(available)
            ans.append(i)

            heapq.heappush(busy, (time + task, w, i))

        return ans