#  concept of Tuple 
# concept of hash: built-in hash function 
# #The hash() function returns an integer hash value for an object.
# only immutable objects like tuple can be hashed

# function 
def hashCalculation():
    my_tuple = tuple(my_list)
    hash_tuple = hash(my_tuple)
    print(hash_tuple)

# execution 
n = int(input())
my_list = list(map(int, input().split()))
hashCalculation(my_list)
