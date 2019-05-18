def calc_area(a):
    stack = []
    maxArea = a[0]
    stack.append(0)
    for ele in range(1,len(a)): 
        if(not stack):
            stack.append(ele)
        elif(a[stack[-1]] <= a[ele]):
            stack.append(ele)
        else:
            while(stack and a[stack[-1]] > a[ele]):
                poppedEle = stack.pop()
                if(stack):
                    currArea = a[poppedEle] * (ele - stack[-1] -1)
                else:
                    currArea = a[poppedEle] * ele
                
                if(currArea > maxArea):
                        maxArea = currArea
            stack.append(ele)
    while(stack):
        poppedEle = stack.pop()
        if(stack):
            currArea = a[poppedEle] * (ele - stack[-1])
            
        else:
            currArea = a[poppedEle] * ele
        
        if(currArea > maxArea):
                maxArea = currArea
        
    return maxArea
    
if __name__ == '__main__':
    a = [24,16,32,26,47,25,11,28,39,10] 
    print(calc_area(a))