import sys 
def quadratic_time_complexity(n):
    total_operations =0
    for i in range(0,n):
        for j in range(0,n):
            print(j, end=" ")
            total_operations += 1  
    print("\nTotal operations:", total_operations)
    print("Time complexity O(n^2)")
def quadratic_space_complexity(n):
            my_list=[i*j for i in range(n) for j in range(n)]
            print(my_list)
            memory_used = sys.getsizeof(my_list)
            print("Length ",len(my_list))
            print(memory_used,  " used memory")
            print("space complexity O(n^2)")
n= int(input("\nn= "))
quadratic_time_complexity(n)
quadratic_space_complexity(n)
