def find_largest(numbers)->list:
    largest=numbers[0]
    for i in numbers:
       if i > largest:
           largest=i
    return (largest,":is a largest number")

numbers=[4,12,7,19,3]
nega_numbers=[-1,-2,-3,-4]
print(find_largest(numbers))
            
