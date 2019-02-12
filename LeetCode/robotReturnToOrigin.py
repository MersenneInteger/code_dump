#robot return to origin
class Solution:
    def judgeCircle(self, moves):
    
        moves_map = {'R':0, 'L':0, 'U':0, 'D':0}
        for move in moves:
            moves_map[move] += 1
        move_list = list(moves_map.values())
        if move_list[0] != move_list[1] or move_list[2] != move_list[3]:
            return False
        return True

s = Solution()
print(s.judgeCircle('UD'))
