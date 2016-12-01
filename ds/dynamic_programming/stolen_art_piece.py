# http://interactivepython.org/runestone/static/pythonds/Recursion/pythondsProgrammingExercises.html
# Question 14

# Suppose you are a computer scientist/art thief who has broken into a major art gallery.
# All you have with you to haul out your stolen art is your knapsack which only holds WW pounds of art,
# but for every piece of art you know its value and its weight. 
# Write a dynamic programming function to help you maximize your profit. 
# Here is a sample problem for you to use to get started: Suppose your knapsack can hold a total weight of 20. 
# You have 5 items as follows:

# item     weight      value
#   1        2           3
#   2        3           4
#   3        4           8
#   4        5           8
#   5        9          10

def solve(weightValueList, backsack, maxProfitList):
    for item in range(backsack+1):
        itemCount = item
        newItem = 1
        for j in [x for x in weightValueList x[0]]