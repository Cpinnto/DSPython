# Ejercicio 1: Loops y condiciones

for i in range(21):
    if i % 3 == 0 and i % 5 == 0: 
      print("FizzBuzz")
    elif i % 5 == 0:
      print("Buzz")
    elif i % 3 == 0:
      print("Fizzes")
    else:
      print(i) 