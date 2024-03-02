age = 25 
height = 1.75 
city = "Питер" 
country = "Florida in USA."

description = """
description - текстовое значение, 
которое занимает несколько строк
description
description
"""

print(age)
print(description)
print("Длинна текстовой строки", len(description))

upper_city = city.upper() # Метод upper, для преоброзование всех элементов.
print(upper_city)

substring = country[0:7]
print(substring)
