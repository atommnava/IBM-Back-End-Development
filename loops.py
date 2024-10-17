# The for loop enables you to execute a code block multiple times. For example, you would use this if you would like to print out every element in a list.
# Let's try to use a for loop to print all the years presented in the list dates

# For loop example

dates = [1982, 1980, 1973]
N = len(dates)

for i in range (N):
    print(dates[i])
    
# Use for loop to change the elements in list

squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i in range (0, 5):
    print("Before square ", i, 'is', squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is', squares[i])
    
    # Lopp through the list and iterate on both index and element value
    squares = ['red', 'yellow', 'green', 'purple', 'blue']
    
    for i, square in enumerate(squares):
        print(i, square)
        
# As you can see, the for loop is used for a controlled flow of repetition. 
# However, what if we don't know when we want to stop the loop? What if we want to keep executing a code block
# until a certain condition is met? The while loop exists as a tool for repeated execution based on a condition. The code block will keep being executed until the given logical condition returns a False boolean value.

count = 1
while count <= 5:
    print(count)
    count += 1
    
# While Loop Example

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    

print("It took ", i ,"repetitions to get out of loop.")
