from functools import reduce

my_list = [1,2,3,4]

# Coke classic
ssv = (sum([val for val in my_list])) / len(my_list)

# Coke, map_reduce flavor
squared_map = list(map(lambda x: x ** 2, my_list))

# Func for reduce
def mean(x1, x2):
    return sum(x1 + x2) / 2

squared_reduce = reduce(mean, squared_map)

print(ssv)
print(squared_map)
print(squared_reduce)
