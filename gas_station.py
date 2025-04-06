def back(gas, cost):
    if sum(gas)<sum(cost):
        return -1
    tank=0
    start=0
    for i in range(len(gas)):
        tank+=gas[i]-cost[i]
        if tank<0:
            start=i+1
            tank=0
            
    return start
        




gas=[1,2,3,4,5]
cost=[3,4,5,1,2]
res=back(gas,cost)
print(res)