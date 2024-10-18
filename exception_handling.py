# Exceptions

# 1/0
# y = a + 5

# potential code before try catch

#try:
    # code to try to execute
#except:
    # code to execute if there is an exception
    
# code that will still execute if there is an exception

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a = ",a)
except:
    print("There was an error.")
    
c = 1

try:
    d = int(input("Please enter a number to divide c"))
    c = c/d
    print("Success c=",c)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
    
 # potential code before try catch

#try:
    # code to try to execute
#except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
#except NameError:
    # code to execute if there is a NameError
#except:
    # code to execute if ther is any exception
#else:
    # code to execute if there is no exception
#finally:
    # code to execute at the end of the try except no matter what
    
# code that will execute if there is no exception or a one that we are handling
