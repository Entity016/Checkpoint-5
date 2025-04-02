# Ejercicio 1
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# Ejercicio 2
def sum_numbers(a, b, c):
    return(a + b + c)

print(sum_numbers(12, 4, 3))

# Ejercicio 3
sum_num_lambda = lambda a, b, c: a + b + c
print(sum_num_lambda(12, 4, 3))

# Ejercicio 4

nombre = 'Enrique'

lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

if nombre.lower() in [n.lower() for n in lista_nombre]:
    print('El nombre está en la lista')
else:   
    print('El nombre no está en la lista')
