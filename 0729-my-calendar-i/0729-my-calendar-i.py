class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        i = self._find_position(start, end)
        
        if i is not None:
            self.calendar.insert(i, (start, end))
            return True
        else:
            return False

    def _find_position(self, start, end):
        if not self.calendar:
            return 0

        low, high = 0, len(self.calendar) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if self.calendar[mid][1] <= start:
                low = mid + 1
            elif self.calendar[mid][0] >= end:
                high = mid - 1
            else:
                return None
        
        return low