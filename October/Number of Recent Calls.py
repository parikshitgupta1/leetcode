class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < self.requests[-1] - 3000:
            self.requests.popleft()
        return len(self.requests)
