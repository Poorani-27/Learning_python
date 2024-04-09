def linear_time_complexity(n):
    print("\nLinear_time_complexity",end = " ")
    for i in range(n):
        print(i , end = " ") 

def linear_space_complexity(n):
    print("\n\nLiner_space_complexity ",end= " ")
    my_list =[i for i in range(n)]
    print(my_list, "\n")

n=int(input("\nEnter a Number : "))
linear_time_complexity(n)
linear_space_complexity(n)

