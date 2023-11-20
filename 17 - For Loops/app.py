# we can use the for loop to iterate a list of names, strings, and numbers
for item in ['Mosh', 'John', 'Sarah']: 
    print(item)

#iterating a list of numbers 
for item in [1, 2, 3, 4]:
    print(item)

# using the range function to print out a range of numbers so we dont have to type the numbers one by one,
print('range of numbers below using the range function')
for item in range(10): #10 will not be inculded 
    print(item)




#using the range function to give a specific rage of numbers
print("Printing range from 5-10")
for item in range(5, 10):
    print(item)

#using the step function to skip numbers
print(" printing a arange of numbers using the step function")
for item in range(5, 10, 2):
    print(item)

#printing the sum of a shopping cart using list and for loops
prices = [10, 20, 30]
total = 0

for item in prices:
    total += item
print(f"Total: {total}")
