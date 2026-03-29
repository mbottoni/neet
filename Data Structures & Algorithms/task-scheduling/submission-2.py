from collections import defaultdict
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        n_cycles = 0
        d_tasks  = defaultdict(int)
        d_cycles = defaultdict(int)
        for t in tasks:
            d_tasks[t] += 1
            d_cycles[t] = 0
        
        all_tasks = list(d_tasks.keys())
        while max(d_tasks.values()) > 0:
            # Pick the available task with the highest remaining count
            best_task = max(
                (task for task in all_tasks if d_cycles[task] == 0 and d_tasks[task] > 0),
                key=lambda task: d_tasks[task],
                default=None
            )
            if best_task:
                d_tasks[best_task] -= 1
                d_cycles[best_task] = n + 1  # Fix: should be n+1, not n

            for task in all_tasks:
                d_cycles[task] = max(0, d_cycles[task] - 1)
            
            n_cycles += 1

        return n_cycles