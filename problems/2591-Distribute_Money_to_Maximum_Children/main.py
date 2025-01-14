# Solution to problem Distribute_Money_to_Maximum_Children
# Problem ID: 2591
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if children > money:
            return -1
        money = money - children
        count = money // 7
        
        if children < count:
            count = children
            remainder = (money - children*7) 
        else:
            remainder = (money - (money//7)*7)
        if children - count == 0:
            if remainder == 0:
                pass
            else:
                count = count - 1
        elif remainder == 3 and (children - count) == 1:
            count = count - 1
        elif remainder / (children - count) > 7:
            count = count - 1

        return count
