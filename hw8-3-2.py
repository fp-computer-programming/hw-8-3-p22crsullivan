# Author: CRS 12/09/21
def count_odds(lst):
    odd = 0
    looped = 0
    while looped < len(lst):
        if lst[looped] % 2 != 0:
            odd += lst[looped]
        looped += 1
    return odd


print(count_odds([1, 2, 3, 4, 5, 6]) == 9)
print(count_odds([1, 3, 5, 7, 9]) == 25)
print(count_odds([2, 4, 6, 8, 10]) == 0)