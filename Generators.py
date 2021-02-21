def square_numbers(nums):
    for i in nums:
        yield (i*i)

my_nums = square_numbers([1,2,3,4,5])

# my_nums = [x*x for x in [1,2,3,4,5]]
#
# for num in my_nums:
#     print(num)

print(list(my_nums))  # Takes a lot of memory if generators converted to list

# Generators take extremely less memory as it loads values one by one..