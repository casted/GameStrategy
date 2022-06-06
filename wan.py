from sko.GA import GA, GA_TSP

map3500 = [[-1, -1, -1, -1, -1, -1, -1],
           [-1, 0, 0, 0, 0, 0, -1],
           [-1, 0, 0, 0, 0, 0, -1],
           [-1, 0, 0, 0, 0, 0, -1],
           [-1, 0, 0, 0, 0, 0, -1],
           [-1, 0, 0, 0, 0, 0, -1],
           # [-1, 0, 0, 0, 0, 0, -1],
           [-1, -1, -1, -1, -1, -1, -1, ]]
index3500 = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5],
             [2, 1], [2, 2], [2, 3], [2, 4], [2, 5],
             [3, 1], [3, 2], [3, 3], [3, 4], [3, 5],
             [4, 1], [4, 2], [4, 3], [4, 4], [4, 5],
             [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]
             # [6, 1], [6, 2], [6, 3], [6, 4], [6, 5]]


def star(map, index, operands):
    thismap = [l[:] for l in map]
    score = 0
    for operand in operands:
        r = index[int(operand)][0]
        c = index[int(operand)][1]
        while (thismap[r][c] != -1):
            thismap[r][c] = (thismap[r][c] + 1) % 4
            score += 90
            if thismap[r][c] == 0:
                r -= 1
            if thismap[r][c] == 1:
                c += 1
            if thismap[r][c] == 2:
                r += 1
            if thismap[r][c] == 3:
                c -= 1
    return score



def fun(p):
    return 1 / star(map3500, index3500, p)


clickNum = 10
sizepop = 100
maxIter = 10000
PNum = 25
ga = GA(func=fun, n_dim=clickNum, size_pop=sizepop, max_iter=maxIter, lb=[0] * clickNum, ub=[PNum-1] * clickNum,
        precision=[1] * clickNum)
best_operat, best_func = ga.run()
print(best_operat)
print(star(map3500, index3500, best_operat))
# print(best_func)

# def greedNext(now): 		 # 当前是now，返回下一步的最优选择
#     gScore = 0
#     for next in range(PNum): # 遍历下一步的所有情况，t: try or temp
#         tOperat = now + [next]
#         tScore = star(map3500, index3500, tOperat)
#         # print("if click ", next, " then score: ", tScore)
#         if(tScore > gScore): # 得到得分最高的那步
#             gScore = tScore
#             best_next = next
#     # print("so click: ", best_next)
#     return [best_next]
#
# gOperat = []                      # 存贪心所得的解
# for i in range(clickNum):         # 添加clickNum个元素
#     gOperat += greedNext(gOperat) # 每次添加局部最优解
# print('贪心得到最优解: ', gOperat, ' score:  ', star(map3500, index3500, gOperat), '\n')

def greedNext4(now):          # 当前是now，返回当前后四步的最优选择
    t = 0
    gScore = 0
    for next1 in range(PNum): # 遍历后面第四步所有情况
        for next2 in range(PNum):
            for next3 in range(PNum):
                for next4 in range(PNum):
                    ams = now
                    # tOperat = now.extend([next1, next2, next3, next4])
                    ams.extend([next1, next2, next3, next4])
                    # tScore = star(map3500, index3500, tOperat)
                    tScore = star(map3500, index3500, ams)
                    # print("if click ", next1, ",", next2, ",", next3, ",", next4, " then score: ", tScore)
                    if(tScore > gScore): # 选出得分最高的组合
                        gScore = tScore
                        best_next = [next1, next2, next3, next4]
    # print("so click: ", best_next)
    return best_next

ans = list(best_operat[:-4])
ans.extend(greedNext4(ans))
print(ans)
print(star(map3500, index3500, ans))