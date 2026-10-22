class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        sorted_values = sorted(zip(position,speed), reverse = True)
        last_time = 0
        fleet = 0

        for p,s in sorted_values:
            time = (target-p)/s

            if time>last_time:
                fleet += 1
                last_time = time

        return fleet

