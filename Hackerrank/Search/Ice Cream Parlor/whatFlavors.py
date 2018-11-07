def whatFlavors(cost, money):
    mapp = {}
    choice1 = 0
    choice2 = 0
    for i in range(len(cost)):
        if cost[i] in mapp:
            mapp[cost[i]].append(i)
        else:
            mapp[cost[i]] = [i]
        if cost[i] < money:
            if money - cost[i] in mapp:
                if cost[i] != money - cost[i]:
                    choice1 = i + 1
                    choice2 = mapp[money - cost[i]][0] + 1
                else:
                    if len(mapp[cost[i]]) > 1:
                        choice1 = i + 1
                        choice2 = mapp[money - cost[i]][0] + 1
    choice1, choice2 = min(choice1, choice2), max(choice1, choice2)
    print(choice1, choice2)