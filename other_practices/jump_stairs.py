'''
You are at the bottom of a staircase with n stairs,
you can jump 1, 2, or 3 stairs at a time.
How many different ways can you jump up the stairs?
'''
n = 4

def stairs(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return stairs(n-3) + stairs(n-2) + stairs(n-1)

print(stairs(n))