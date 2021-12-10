# Author: CRS 12/09/21
def count_letter(lst):
    letter = 0
    looped = 0
    while looped < len(lst):
        if len(lst[looped]) % 3 == 0:
            letter += 1
        looped += 1
    return letter


print(count_letter(["cat", "bat", "apple"]) == 2)
print(count_letter(["apple", "hippo", "mouse"]) == 0)
print(count_letter(["hop", "pop", "bop"]) == 3)
