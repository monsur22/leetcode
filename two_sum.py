ls = [1,2,3,4]
for i in range(len(ls)):
    for j in range(i+1,len(ls)):
        if ls[i]+ls[j] == 6:
            print(ls[i],ls[j])
            # print(i,j)
    # return ls[i]
    # print(ls)