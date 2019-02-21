# # 1. Define una función max () que toma como argumentos dos números y devuelve el mayor de ellos. 
# num1 = float(input('Enter first number: '))
# num2 = float(input('Enter second number: '))
# def max(a, b):
#     return a if a > b else b

# print('The max of {0} and {1} is {2}'.format(num1, num2, max(num1, num2)))

# # 2. Escribe una función que toma un carácter (es decir, una cadena de longitud 1) y devuelve True si es una vocal, False en caso contrario
# letter = input('Enter a letter: ')
# def vowel(a):
#     return a in 'AaEeIiOoUu'

# print('The letter {0} is vowel? -> {1}'.format(letter, vowel(letter)))

# # 3. Definir una función sum ()  que suma todos los números de una lista de números. Por ejemplo, suma ([1, 2, 3, 4]) debería devolver 10.

# a = [int(x) for x in input('Enter a sequence of numbers space separated: ').split()]

# print('The sum of {0} is-> {1}'.format(a, sum(a)))

# # 4. Definir una función reverse () que retorna la inversión de una cadena. Por ejemplo, reverse ("I am testing") debería devolver la cadena "gnitset ma I".

# string = input('Enter a string: ')

# print('The reversed string of {0} is-> {1}'.format(string, string[::-1]))

# # 5. Un pangrama es una frase que contiene todas las letras del alfabeto Inglés, al menos una vez, por ejemplo: "The quick brown fox jumps over the lazy dog".  Escribe una función para comprobar si una sentencia para ver si es un pangrama o no.
string = input('Enter a valid program: ')
isProgram = all(ord(char) < 123 and ord(char) > 65 for char in string)

print('The entered string {0} is program -> {1}'.format(string, isProgram))