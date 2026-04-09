# detailed explanation of these concepts
# https://nedbatchelder.com/text/names1.html 

x = 2
y = x #pointing to same object in mem
x = 3 #y will keep pointing to 2, but x will now point to 3
print(x)

lst = [1,2,3]
new_lst = lst
new_lst[0] = 0
print(new_lst,lst) #[0, 2, 3] [0, 2, 3] (both changes)
new_lst = [1]
print(new_lst,lst) #[1] [0, 2, 3] (new_lst is assigned a new value hence, new ref is created for new_lst, but lst remains pointed to same address)


nums = [1,2,3]
for x in nums: #x is pointing to what nums[0] is pointing to
    x = x * 10 #but when x is assigned new object, its address gets changed to new address, keeping the num[0] address unchanged
print(nums) #no change
