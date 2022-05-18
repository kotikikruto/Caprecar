# Капрекар для десятичной сс (вход и выход - в десятичной!)
def Caprecar_10(n, l):
    nums = []
    for i in range(l):
        nums.append(n % 10)
        n //= 10
    nums = sorted(nums)
    k = 0
    for i in range(l):
        k += (nums[l - i - 1] - nums[i]) * 10 ** (l - i - 1)
    return k
