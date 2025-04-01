intervals=[[1,3],[6,9]]
newinterval=[2,5]
def merge_intervals(intervals, newinterval):
    start, end=newinterval
    res=[]
    is_inserted=False
    for interval in intervals:
        if interval[1]<start:
            res.append(interval)
        elif interval[0]>end:
            if not is_inserted:
                res.append([start,end])
                is_inserted=True
            res.append(interval)    
        else:
            start=min(interval[0],start)
            end=max(interval[1],end)
    if not is_inserted:
        res.append(start, end)
    return res
res=merge_intervals(intervals, newinterval)
print(res)
