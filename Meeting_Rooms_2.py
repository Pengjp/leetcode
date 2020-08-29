# Meeting_Rooms_2.py

def minMeetingRooms(intervals: List[List[int]]) -> int:
    ''' in this implementation, we first sort the like by starting time and 
    use a priority queue to store the end time. Then loop through the remaining meeting,
    if new meeting start is smaller that latest end time, we need a new room
    '''
    from heapq import heappush, heappop
    
    if not intervals:
        return 0
    rooms = []
    # sort by start timee
    intervals.sort(key = lambda x:x[0])
    # push first meeting end time
    heappush(rooms, intervals[0][1])
    
    for meeting in intervals[1:]:
        # if current meeting start time is greater or equal than 
        # previous meeting end time, we won't need a new room
        if meeting[1] >= rooms[0]:
            heappop(rooms)
        
        heappush(rooms, meeting[1])
    
    return len(rooms)


def minMeetingRooms(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0
    StartTime = [i[0] for i in intervals]
    EndTime = [i[1] for i in intervals]
    StartTime.sort()
    EndTime.sort()

    rooms = 0
    EndIndex = 0
    StartIndex = 0
    
    while StartIndex < len(StartTime):
        if StartTime[StartIndex] < EndTime[EndIndex]:
            rooms += 1
        else:
            EndIndex += 1
        StartIndex += 1
    return rooms