'''
Calculate Sum of List:
Write a Python function to calculate the sum of all elements in a given list of integers.

Input: [1, 2, 3, 4, 5]
Expected Output: 15

'''
a=[1,2,3,4,5]
print(sum(a))

'''
Find Maximum Value:
Implement a function to find the maximum value in a list of numbers without using the built-in max() function.

Input: [3, 7, 2, 9, 5]
Expected Output: 9

'''
a=[3,7,2,9,5]
a=sorted(a)
print("The array is sorted in ascending order so the maximum element could be the last element : ",a[-1])

'''
Remove Duplicates:
Write a Python program to remove duplicate elements from a list and preserve the original order of elements.

Input: [1, 2, 3, 2, 4, 3, 5]
Expected Output: [1, 2, 3, 4, 5]

'''
a=[1,2,3,2,4,3,5]
a=sorted(a)
a=[a[i] for i in range(len(a)) if i==0 or a[i] !=a[i-1]]
print(a)

'''
Merge Sorted Lists:
Implement a function to merge two sorted lists into a single sorted list.

Input: [1, 3, 5], [2, 4, 6]
Expected Output: [1, 2, 3, 4, 5, 6]
'''
a=[1,3,5]
b=[2,4,6]
c=sorted(a+b)
print(c)

'''
Check Palindrome:
Write a Python function to check if a given list is palindrome (i.e., reads the same forwards and backwards).

Input: [1, 2, 3, 2, 1]
Expected Output: True

'''
a=[1,2,3,2,1]
print(a == list(reversed(a)))
# print(a==a[::-1])

'''
Implement a function to rotate the elements of a list to the left by a given number of positions.

Input: [1, 2, 3, 4, 5], 2
Expected Output: [3, 4, 5, 1, 2]
'''