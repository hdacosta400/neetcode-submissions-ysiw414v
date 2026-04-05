from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        

        queue = deque([("0000", 0)])
        visited = set()
        deadends_set = set(deadends)

        min_dist = -1
        while queue:
            lock_state, dist = queue.popleft()

            visited.add(lock_state)

            if lock_state == target:
                return dist
            if lock_state in deadends:
                return -1 


            for idx in range(len(lock_state)):
                up_str = lock_state[:idx] + self.move_wheel_up(lock_state[idx]) + lock_state[idx+1:]
                down_str = lock_state[:idx] + self.move_wheel_down(lock_state[idx])  + lock_state[idx+1:]

                if up_str == target or down_str == target:
                    return dist + 1

                if (up_str not in deadends_set and up_str not in visited) :
                    queue.append((up_str, dist + 1))
                    visited.add(up_str)

                if down_str not in deadends_set and down_str not in visited:
                    queue.append((down_str, dist + 1))
                    visited.add(down_str)
        
        return min_dist


    def move_wheel_up(self, slot):
        slot = int(slot)
        return str((slot + 1) % 10)

    def move_wheel_down(self, slot):
        slot = int(slot)
        return str((slot - 1) % 10)
           





        