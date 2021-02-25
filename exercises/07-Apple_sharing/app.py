#Complete the function to return:
#1) How many apples each single student will get.
#2) How many apples wil remain in the basket.
#Hint: You can resolve this exercise either importing the math module or without it 
def apple_sharing(n,k):
  num1 = round(k / n)
  num2 = (num1 * n)
  num3 = (k - num2)
  desarrollo = (num1 , num3)
  return desarrollo
 
    

#Print the two answer per the example output.
print(apple_sharing(6,50))