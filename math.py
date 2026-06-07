#math
#A Python program that finds the maximum of log 1000 and e^e

import math

value1 = math.log(1000)   # natural logarithm ln(1000)
value2 = math.e ** math.e

maximum = max(value1, value2)

print("log(1000) =", value1)
print("e^e =", value2)
print("Maximum =", maximum)