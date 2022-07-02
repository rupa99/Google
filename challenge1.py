#list = []
def solution(area):
    # print("here")
    count = area 
    sum = 0
    list = []

    for i in range(area):
        #print(count)
        if(sum + (count * count) <= area):
            list.append(count * count)
            sum = sum + (count * count)
            #print(sum)
            if(count == 1 and sum + (count * count) <= area):
                #we just add the remaining as 1 squared 
                no_ones = area - sum
                for x in range(no_ones):
                    list.append(1)
                break # we don't want to go to the point where we have zero

            
            count = count - 1
        else:
            count = count - 1

    #val = (*list, sep = ", ")
    #return val
    print (list)
    return(list)

        
solution(12)
#solution(15324)