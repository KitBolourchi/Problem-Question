def palindrome(x):
    orig = x
    back_w = 0

    while x > 0:
        back_w = (back_w * 10) + (x % 10)
        x = x // 10
    
    return orig == back_w

print(palindrome(1223321))
