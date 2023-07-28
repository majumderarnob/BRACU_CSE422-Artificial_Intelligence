import random
import math

id = input("Enter your student id:")
depth = int(id[0]) * 2
branch = int(id[2])
hp = int(id[-1] + id[-2])
min_hp = int(input('Minimum value for the range of negative HP '))
max_hp = int(input('Maximum value for the range of negative HP '))
leaf = [random.randint(min_hp, max_hp) for i in range (branch**depth)]
alpha = -math.inf
beta = math.inf
count = 0


def alpa_betaPrunning(leaf, d, alpha, beta, maximizingPlayer, idx, count):
    if d == 0:
        return (leaf[idx],count + 1)
    if maximizingPlayer == True:
        best = -math.inf
        for i in range(branch):
            best1, count = alpa_betaPrunning(leaf, d-1, alpha, beta, False, idx * branch + i, count)
            best = max(best, best1)
            alpha = max(best, alpha)
            if alpha >= beta:
                break
        return best, count
    else:
        best = math.inf
        for i in range(branch):
            best1,count = alpa_betaPrunning(leaf, d - 1, alpha, beta, True, idx * branch + i, count)
            best = min(best, best1)
            beta = min(best, beta)
            if alpha >= beta:
                break
        return best, count
   
    
ans = alpa_betaPrunning(leaf, depth, -math.inf, math.inf, True, 0, count)
print("Depth and Branches ratio is",depth,":",branch)
print("Terminal States(Leaf Nodes) are",leaf)
print("Left life(HP) of the defender after maximum damage caused by the attacker is", hp - ans[0])
print("After Alpha-Beta Pruning Leaf Node Comparisons",ans[1])
 