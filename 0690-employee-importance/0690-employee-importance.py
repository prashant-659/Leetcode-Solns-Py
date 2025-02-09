"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp={e.id:e for e in employees}
        importance=0
        q=deque([id])

        while q:
            emp_id=q.popleft()
            employee=emp[emp_id]
            importance+=employee.importance
            q.extend(employee.subordinates)
        return importance