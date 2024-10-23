numbers_list=[12,34,11,9,6,24]
target =36
first_index = numbers_list[0]
#input_number = input("enter your number list : ")
#for i in numbers_list:
for i in range(0,len(numbers_list)):
    for j in range(i+1,len(numbers_list)):
        if numbers_list[j] + numbers_list[i]==target:
            print(i,j)
            break