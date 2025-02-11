from re import X


def loop_function(x):
    for i  in range(X):


        if i % 2 == 0:
         print(i, "is even!")    
    else:
     print(i, "is an odd number!")
print("Done!")
number_of_loops = 20
loop_function(number_of_loops)
