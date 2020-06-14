'''
Give a string of angle brackets, angles, such as "<<><>><<<>", 
write a function that adds angle brackets to the beginning and end to make all angle brackets match and return it.
The angle brackets "match" if for every < there is a corresponding > appearing after it in the string,
and for every > there is a corresponding < appearing before it in the string.
'''
nums = "><>>>><><><><><>"

def function(nums):
    ans = nums
    right = 0
    for i in range(len(nums)):
        if nums[i] == '>':
            if right == 0:
                ans = '<' + ans
            else:
                right -= 1
        elif nums[i] == '<':
            right += 1
    ans += right * '>'       

    return ans

print(function(nums))