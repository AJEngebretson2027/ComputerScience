import random
nums = [random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100)]
print(nums)
def bubble(number):
    steps = 0
    for j in range(0,len(nums)-1):
        for i in range(0, len(number) - 1):
            if number[i] > number[i+1]:
                number[i], number[i+1] = number[i+1], number[i]
                steps += 1
    print(number)
    print("completed in " + str(steps) + " steps.")
        
bubble(nums)