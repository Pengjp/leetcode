class UndergroundSystem:

    def __init__(self):
        from collections import defaultdict
        self.startInfo = defaultdict()
        self.table = defaultdict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.startInfo[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkinName = self.startInfo[id][0]
        checkinTime = self.startInfo[id][1]
        info = (checkinName, stationName)
        if info not in self.table:
            self.table[info] = (t - checkinTime, 1)
        else:
            rec = self.table[info]
            self.table[info] = (rec[0] + t - checkinTime, rec[1] + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.table[(startStation, endStation)][0] / self.table[(startStation, endStation)][1]

