class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_sp = []
        fleet = []
        for i in range(len(position)):
            pos_sp.append([position[i], speed[i]])
        
        pos_sp.sort(reverse=True)
        print(pos_sp)
        fleet.append(pos_sp[0])

        for i in range(1, len(position)):
            t1 = (target-fleet[-1][0]) / fleet[-1][1]
            t2 = (target-pos_sp[i][0]) / pos_sp[i][1]
            if t2 > t1:
                fleet.append(pos_sp[i])
        
        return len(fleet)