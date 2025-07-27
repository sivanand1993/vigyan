import my_functions as func
import random
#1.1. Import functions: (5 points)
fahren=59
print(str(fahren)+" Fahrenheit is "+str(func.fahrenheitCelsiusCOnverter(fahren))+" Celsius.")
celsius=15
print(str(celsius)+" Celsius is "+str(func.celsiusFahrenheitCOnverter(celsius))+" Fahrenheit.")

#1.2. NullToBooleanConverter: (5 points)
val1=None
print(func.NullToBooleanConverter(val1))
val1=123
print(func.NullToBooleanConverter(val1))

#1.3. Magic 8-Ball: (5 points)
val2=random.randint(1,10)
print(func.getAnswer(val2))
