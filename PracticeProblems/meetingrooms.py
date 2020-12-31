class Solution():
    def meetingrooms(self,ranges):
        rooms = 0
        emptyranges = {}
        for x in ranges:
            print(emptyranges)
            if not self.isInEmptyranges(emptyranges,x):
                rooms += 1
                emptyranges[rooms] = [(float("-inf"),x[0]),(x[1],float("inf"))]
        print(emptyranges)
        return rooms
    def isInEmptyranges(self,emptyranges,myrange):
        for x in emptyranges:
            for emptyrange in emptyranges[x]:
                if emptyrange[0]<= myrange[0] and  emptyrange[1]>= myrange[1]:
                    emptyranges[x].append((emptyrange[0],myrange[0]))
                    emptyranges[x].append((myrange[1],emptyrange[1]))
                    emptyranges[x].remove(emptyrange)
                    return True
        return False
#print(Solution().meetingrooms([(0,10),(10,20)]))
#print(Solution().meetingrooms([(0,50),(8,15),(10,21),(20,30)]))

import heapq

def meeting_rooms(meetings):
  meetings.sort(key=lambda x: x[0])
  meeting_ends = []
  max_rooms = 0

  for meeting in meetings:
    print(meeting_ends)
    while meeting_ends and meeting_ends[0] <= meeting[0]:
      print(meeting_ends)
      heapq.heappop(meeting_ends)
    heapq.heappush(meeting_ends, meeting[1])
    max_rooms = max(max_rooms, len(meeting_ends))
  
  print(meeting_ends)
  return max_rooms

print(meeting_rooms([[0, 10], [10, 20]]))
# 1

print(meeting_rooms([[20, 30],[9,14], [8,15],[10, 21], [0, 50]]))
# 3


