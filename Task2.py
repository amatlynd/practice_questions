# Question 2
# Write a function get_products_of_all_ints_except_at_index()
# that takes a list of integers and returns a list of the products.
# Do not use division

def get_products_of_all_ints_except_at_index(rawList):

    productList = []
    productValue = 1
    for i in range(len(rawList)): # Getting the index of the excluded product
        for j in range(len(rawList)): # Getting the product of the remaining values of the list
            if i != j:
                productValue = productValue*rawList[j]
        productList.insert(i,productValue)
        productValue = 1
    return productList

rawList = [1, 7, 3, 4]

print (get_products_of_all_ints_except_at_index(rawList))
