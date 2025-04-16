def nonoverlap(intervals):
    intervals=sorted(intervals, key=lambda x:x[1])
    end=intervals[0][1]
    count=0
    for i in range(1,len(intervals)):
        if intervals[i][0] < end:
            count+=1
        else:
            end=intervals[i][1]
    return count

intervals=[[1,2],[1,2],[1,2]]
res=nonoverlap(intervals)
print(res)