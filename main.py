def odd_list(lst):
    for i in lst:
        if i % 2 != 0:
            print(i , end=" ")

my_list = [1,2,3,4,5,6,7,8,9]
odd_list(my_list)
