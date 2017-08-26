class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class MergeInterval:
    def merge(self, intervals):
        n = len(intervals)
        sorted_intervals = self.sort_intervals(intervals)
        if n <= 1:
            return sorted_intervals

        merged = []
        first, second = sorted_intervals[0], sorted_intervals[1]
        if self.overlap(first, second):
            merged.append(self.merge_intervals(first, second))
        else:
            merged.append(first)
            merged.append(second)
        if n == 2:
            return merged

        last_merged = merged[-1]
        for i in range(2, n):
            curr_interval = sorted_intervals[i]
            if self.overlap(last_merged, curr_interval):
                merged[-1] = (self.merge_intervals(last_merged, curr_interval))
            else:
                merged.append(curr_interval)
            last_merged = merged[-1]
        return merged

    def sort_intervals(self, intervals):
        return (sorted(intervals, key=lambda interval: interval.start))

    def overlap(self, first, second):
        return first.end >= second.start

    def merge_intervals(self, first, second):
        return Interval(first.start, max(first.end, second.end))

test_merger = MergeInterval()
# Test sorting
unordered_intervals = [Interval(1, 3), Interval(15, 18), Interval(8, 10), Interval(2, 6)]
sorted_interval = test_merger.sort_intervals(unordered_intervals)
print("Expected: [1, 3], [2, 6], [8, 10], [15, 18]")
print("Actual: ", [[interval.start, interval.end] for interval in sorted_interval])

# Test Merging
solved = test_merger.merge(unordered_intervals)
print("Expected: [1, 6], [8, 10], [15, 18]")
print("Actual: ", [[interval.start, interval.end] for interval in solved])

solved = test_merger.merge([Interval(1,6), Interval(8,8), Interval(8, 15)])
print("Expected: [1, 6], [8, 15]")
print("Actual: ", [[interval.start, interval.end] for interval in solved])