# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio


print('Ingrese por consola la primera temperatura:')
numero_1 = int(input())

print('Ingrese por consola la segunda temperatura:')
numero_2 = int(input())

print('Ingrese por consola la tarecera temperatura:')
numero_3 = int(input())

if numero_1 > numero_2:
    if numero_1 > numero_3:
        print('La primera temperatura es la mayor.')
    else:
        print('La tercer temperatura es la mayor.')
elif numero_2 > numero_3:
    print('La segunda temperatura es la mayor.')
else:
    print('La tercer temperatura es la mayor.')

if numero_1 < numero_2:
    if numero_1 < numero_3:
        print('La primera temperatura es la menor.')
    else:
        print('La tercer temperatura es la menor.')
elif numero_2 < numero_3:
    print('La segunda temperatura es la menor.')
else:
    print('La tercer temperatura es la menor.')

promedio = (numero_1 + numero_2 + numero_3) / 3
print('el promedio de las temperaturas es:' , promedio)