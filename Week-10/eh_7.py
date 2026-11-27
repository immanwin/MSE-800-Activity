try:
    nums = [1, 2, 3]
    print(nums[5])
except (IndexError, KeyError) as e:
    print(type(e).__name__)
else:
    print("no error")
