
from typing import List
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        srt_box = sorted(boxTypes, key=lambda x: x[1], reverse=True)

        t_unit = 0
        for box, unit in srt_box:

            if box <= truckSize:
                truckSize -= box
                t_unit += box * unit

            else:
                t_unit += truckSize * unit
                break

        return t_unit

obj = Solution()

boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
truckSize = 10
print(obj.maximumUnits(boxTypes, truckSize))
