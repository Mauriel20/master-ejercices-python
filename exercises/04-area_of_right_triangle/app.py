#Complete the function to return the area of the triangle.
b = int(input("Size of B"))
h = int(input("Size of H"))

def area_of_triangle(arg1, arg2):
    #your code here, please remove the "None" 
    desarrollo= ((1/2) * arg1 * arg2)
    return desarrollo
# Testing your function
print(area_of_triangle(b, h))