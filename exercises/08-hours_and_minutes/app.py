#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(secs):
  minutos = int(secs / 3600)
  horas = int(secs/60)
 



  return(minutos , horas)




#Invoke the funtion and pass any interger as its argument.
print(hours_minutes(3900))