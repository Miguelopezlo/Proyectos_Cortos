
ops=[5,2,"C","D","+"]
nums=[]
for i in range(len(ops)):
    if isinstance(ops[i],int):
        nums.append(ops[i])
    elif ops[i]=="+":
        nums.append(nums[-2]+nums[-1])
    elif ops[i]=="D":
        nums.append(2*nums[-1])
    elif ops[i]=="C":
            nums.pop(-1)
    print(nums)
print(sum(nums))


