def container(height):
    start, end=0,len(height)-1
    max_area=0
    while start < end:
        curr_height=min(height[start], height[end])
        width=end - start
        area=curr_height * width
        max_area=max(max_area, area)
        if height[start]<height[end]:
            start+=1
        else:
            end-=1
    return max_area

height=[1,8,6,2]
res=container(height)
print(res)