from heapq import heappush, heappop

class Solution(object):
    def getSkyline(self, buildings):
        # add start-building events
        events = [(L, -H, R) for L, R, H in buildings]
        # also add end-building events(acts as buildings with 0 height)
        events += list({(R, 0, 0) for _, R, _ in buildings})
        # and sort the events in left -> right order
        events.sort()

        # res: result, [x, height]
        res = [[0, 0]]
        # live: heap, [-height, ending position]
        live = [(0, float("inf"))]
        for pos, negH, R in events:
            # 1, pop buildings that are already ended
            while live[0][1] <= pos: heappop(live)
            # 2, if it's the start-building event, make the building alive
            if negH: heappush(live, (negH, R))
            # 3, if previous keypoint height != current highest height, edit the result
            if res[-1][1] != -live[0][0]:
                res.append([pos, -live[0][0]])
        return res[1:]
