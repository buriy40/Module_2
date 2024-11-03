my_list = [42, 69, 322, 13, 0, 9, -5, 7, 18, 6, -6, 5]
i = 0
while i<len(my_list):
    is_prime = True
    if my_list[i]>0:
        print(my_list[i])
        i=i+1
    elif my_list[i] == 0:
        i=i+1
    else:
        is_prime = False
        i = i + 1

