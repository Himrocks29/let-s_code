#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#Case1
nums = [2,7,11,15]
target = 9

#Case2
'''nums = [3,2,4]
target = 6'''

#Case3
'''nums = [3,3]
target = 6'''

for i in range(len(nums)-1):
    #print("i="+str(i))

    for j in range(i+1, len(nums)):
        #print("j="+str(j))
        if(nums[i]+nums[j])==target:
            print(i,j)
            #return(i,j)