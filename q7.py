# program to get sum of list divisible by 3 or 5

def three_sum(num_list):
    return sum([i for i in num_list if i % 3 or i % 5])


print(three_sum([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
