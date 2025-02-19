#Superman is doing yet another good deed, using his power of flight to distribute meals for the Metropolis Food Bank. He wants to distribute meals in the least number of trips possible.
#Metropolis Food Bank currently stores meals in n packs where the ith pack contains meals[i] meals. There are also m empty boxes which can contain up to capacity[i] meals.
#Given an array meals of length n and capacity of size m, write a function minimum_boxes() that returns the minimum number of boxes needed to redistribute the n packs of meals into boxes.
#Note that meals from the same pack can be distributed into different boxes.

def minimum_boxes(meals, capacity):
    sumMeals = sum(meals)
    capacity = sorted(capacity, reverse=True)
    total = 0
    while sumMeals > 0:
        sumMeals -= capacity[total]
        total += 1
    print(total)
        


meals = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]

#1,2,3
#1,2,3,4,5

minimum_boxes(meals, capacity)

meals = [5, 5, 5]
capacity = [2, 4, 2, 7]

#5,5,5
#2,2,4,7

#7 - 5 = 2 - 1 pack
#2 + 2 + 2 = 1 - 2 packs
# 4 + 1 = 0 - 1 pack

minimum_boxes(meals, capacity)

'''
2
4

This problem may benefit from knowing how to sort a list. 
Python provides a couple options for sorting lists and other iterables, including sort() and sorted(). 
Use your independent research skills or the unit cheatsheet to research how these functions work!
'''