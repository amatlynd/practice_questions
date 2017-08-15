# Question 3
# Given a list of integers, find the highest product
# you can get from three of the integers.
# The input list_of_ints will always have at least three integers

def highest_product(list_of_ints):

    totalProducts = []
    counter = 0
    
    for i in range(len(list_of_ints)):
        for j in range(len(list_of_ints)):
            if i != j:
                for k in range(len(list_of_ints)):
                    if i != k and j != k:
                        totalProducts.insert(counter, list_of_ints[i]*list_of_ints[j]*list_of_ints[k])
                        counter = counter + 1
    
    return max(totalProducts)


list_of_ints = [1,2,5,3,4]
list_of_ints2 = [5,1,2,4,3]
longer_list = [5,1,2,4,3,5,1,2,4,3,5,1,2,4,3]
print (highest_product(list_of_ints))
print (highest_product(list_of_ints2))
print (highest_product(longer_list))
