"Exercício 1: Apresentação do tipo de dado string "

# Cria uma string 

myString = "This is a string"
print(myString)

# Exibe o tipo de dado da string
print(type(myString))

# Concatena a string com seu tipo de dado

print(myString + " is of the data type " + str(type(myString)))


"Exercício 2: Uso da concatenação de strings"

# Cria duas strings e as concatena 
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString 
print(thirdString)

"Exercício 3: Uso de strings de entrada"

# Pede o nome do usuario
name = input("qual o seu nome? ")

# Exibe o nome inserido 
print(name)

"Exercício 4: Formatação de strings de saída"

# Pergunta a cor e o animal favoritos do usuario
color = input("what is your favorite color? ")
animal = input("what is your favorite animal? ")

## Exibe uma mensagem formatada com as informações coletadas
print("{}, you like a {} {}!".format(name, color, animal))