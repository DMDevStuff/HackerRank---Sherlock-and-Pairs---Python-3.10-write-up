##    https://www.hackerrank.com/challenges/sherlock-and-pairs/problem
##
##    Sherlock is given an array of N integers by Watson. Now Watson asks
##    Sherlock how many different pairs of indices i and j exist such that i is not
##    equal j to but array[i] is equal to array[j].

##### ##### ##### #####

#   O(n)
#   n is the number of elements in a

#   Idea:
#       Since we are looking for pairs of matching elements, a good place
#       to start is to create a dictionary that stores an element as a key
#       and a list containing all the indices that element appears at,
#       as the associated value.  From here, the problem is reduced to
#       solving for n choose 2, where n is the length of an index list, for
#       each index list.

#   Note:
#       n choose 2 is a special case of n choose k
#       Instead of the normal formula which contains a lot of factorial functions
#       n choose 2 can be simplified to n * (n - 1) to save computational overhead

#   Algo:
#       1. Initiate empty dictionary for storing element:index_list pairs => O(1)
#       2. Initiate variable to count the total number of pairs found => O(1)
#       3. Iterate through the given array and store each element as a key and
#           the index it appears at in a list as the associated value => O(n)
#       4. Iterate through the created dictionary, if the length of the list
#           associated with a key is greater than one, calculate n choose 2 where
#           n is the length of the list and add it to the
#           total number of pairs found => O(n)
#       5. Return total number of pairs found => O(1)

def solve(a):
    
    index_table = dict()
    total_number_of_pairs = 0
    
    for index in range(len(a)):
        
        try:
            index_table[a[index]].append(index)
            
        except:
            index_table[a[index]] = list()
            index_table[a[index]].append(index)
            
    for key in index_table:
        
        n = len(index_table[key])
        
        if n > 1:
            
            total_number_of_pairs += (n * (n - 1))
            
    return total_number_of_pairs
