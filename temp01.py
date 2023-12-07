number_n = int(input("Unesite broj n koji će biti posljednji broj liste: "))  # [1,2,3,4,5,6,7,8,9,10]
list_number = list(range(number_n))
list_number.append(number_n)
print(list_number)

index = 0
sum = 0
for i in list_number:
    sum = sum * int(list_number[index])
    index = index + 1
    
print("Sum:", sum)
print("Average: ",sum/number_n)
