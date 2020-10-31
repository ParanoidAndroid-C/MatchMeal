
Money = 13
calories = [3, 4, 3]
cost = [2, 3, 4]

def ukp(w, weights, values):
    answ = [0]*(w+1)
    rame = [[] for i in range(0, w+1)]
    
    for i in range(0, w+1):
        for j in range(0, len(weights)):
            if weights[j] <= i:
                if answ[i-weights[j]] + values[j] > answ[i]:
                    rame[i].clear()
                    rame[i].append(i-weights[j])
                    rame[i].append(j)
                answ[i] = max(answ[i], answ[i-weights[j]] + values[j])
    items(rame, values, answ[w], w)
    return answ[w]
    
def items(myList, values, max_val, max_w):
    used_items = []
    summ = 0
    k = max_w
    while summ < max_val:
        summ += values[myList[k][1]]
        used_items.append(values[myList[k][1]])
        k = myList[k][0]

    print(used_items)
        

print(ukp(Money, cost, calories))