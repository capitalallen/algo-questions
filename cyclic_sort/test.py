def find_missing_number(nums):
    # TODO: Write your code here
    if len(nums)<2:
        return nums 
    nums = order_nums(nums)
    print(nums)
    for i in range(len(nums)):
        if nums[i]!=(i):
            return i 
    return n 
def order_nums(nums):
    i,l = 0,len(nums)
    while i < l:
        j = nums[i]
        if nums[i] < l and nums[i]!=nums[j]:
            nums[i],nums[j] = nums[j],nums[i]
        else:
            i+=1
    return nums 

def main():
  print(find_missing_number([4, 0, 3, 1]))
  print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()