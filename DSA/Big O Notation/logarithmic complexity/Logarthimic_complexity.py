def binary_search(arr, target):
    print("quadratic_time_complexity")
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def fib(num):
   
    if num<= 1:
        return n 
    else :
        return fib(num-1)+fib(num-2)



arr = list(map(int, input("Enter elements separated by space : ").split()))

arr.sort()


n = int(input("\nEnter the target element : "))

num=int(input("num ="))

index = binary_search(arr, n)

if index != -1 :
    print(f"Element found at index {index}.")
else:
    print("Element not found.")

result = fib(num)
print(result)


