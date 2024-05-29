height = input("Enter the height in m:")
weight = input("Enter the weight in kg:")
print(type(height))
print(type(weight))

weight_as_int = int(weight)
height_as_float = float(height)
#using the exponent operator
BMI = weight_as_int/height_as_float ** 2
#using multiplication and PEMDAS
BMI= (weight_as_int)/(height_as_float * height_as_float)
print(BMI)
BMI_as_INT = int(BMI)
print(BMI_as_INT)
print(round(BMI))