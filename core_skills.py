import random
# rand_list = 
rand_list = [random.randint(1, 21) for _ in range(20)]

# list_comprehension_below_10 =
list_comprehension_below_10 = [x for x in rand_list if x < 10]
# list_comprehension_below_10 =
list_comprehension_below_10 = list(filter(lambda x: x < 10, rand_list))

if __name__ == "__main__":
    print("Random List:", rand_list)
    print("List Comprehension Below 10:", list_comprehension_below_10)
    print("Filter Function Below 10:", list_comprehension_below_10)
