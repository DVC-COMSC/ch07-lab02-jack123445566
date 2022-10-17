import random 
numbers=[]
for i in range(10): 
    n = random.randint(0,10)
    numbers.append(n)
    smallest = min(numbers)
print(f'Smallest element in the list is: {smallest}.')
