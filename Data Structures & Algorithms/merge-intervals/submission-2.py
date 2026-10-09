class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: sorted(x))
        prev = [0,0]
        current_interval = [intervals[0][0], intervals[0][1]]
        new_intervals = []
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= current_interval[1] and intervals[i][1] >= current_interval[1]:
                current_interval[1] = intervals[i][1]
            elif intervals[i][0] <= current_interval[1] and intervals[i][1] <= current_interval[1]:
                continue
            else:
                new_intervals.append(current_interval)
                current_interval = intervals[i]
        new_intervals.append(current_interval)
        
        return new_intervals
