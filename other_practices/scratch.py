'''
A Man and his Umbrellas
只有rainy, thunderstorms需要用傘
'''

weather = ["rainy", "clear", "rainy", "cloudy"]

def umbrellas(weather):
    home = company = 0
    
    for i in range(len(weather)):
        if i % 2 == 0 and (weather[i] == 'rainy' or weather[i] == 'thunderstorms'):
            if home == 0 :
                company += 1
            else:
                home -= 1
                company += 1
        elif i % 2 != 0 and (weather[i] == 'rainy' or weather[i] == 'thunderstorms'):
            if company == 0:
                home += 1
            else:
                company -= 1
                home += 1
        else:
            continue
    
    return home + company


###########################################################################################

'''
Tribonacci Sequence

每個數字是前三個數字的和
n為正整數，n==0非回空集合
假設起始值為[0, 0, 1]
'''

t_list = [0, 0, 1]

def tribonacci(n):

    if n == 0:
        return []
    elif n == 1:
        return t_list[0]
    elif n == 2:
        return t_list[1]
    elif n == 3:
        return t_list[2]
    else:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

############################################################################################
'''
Check if two words are isomorphic to each other

同構關係
'''

from collections import Counter

A = 'RRCC'
B = 'TTWW'

def check_isomorphic(A, B):

    if len(A) != len(B):
        return False
    else:
        list_A = dict(Counter(A))
        list_B = dict(Counter(B))
        for i in range(len(A)):
            if list_A[A[i]] == list_B[B[i]]:
                continue
            else:
                return False
        return True

