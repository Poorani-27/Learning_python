import random

# Set a seed for reproducibility
seed_value = 42
random.seed(seed_value)

# random.choice
my_list = [1, 2, 3, 4, 5]
random_element = random.choice(my_list)

# random.randint
random_integer = random.randint(1, 10)

# random.uniform
random_float = random.uniform(0, 1)

# random.randrange with seed
start, stop, step = 0, 10, 2
random_range = random.randrange(start, stop, step)

# random.shuffle
shuffle_list = [1, 2, 3, 4, 5]
random.shuffle(shuffle_list)

# Print results
print("Random Choice:", random_element)
print("Random Integer:", random_integer)
print("Random Float:", random_float)
print("Random Range:", random_range)
print("Shuffled List:", shuffle_list)
