
"Exercício 1: Apresentação do tipo de dado lista"

# Definindo uma lista de frutas
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

# Acessando os itens da lista por posição
print(myFruitList[0]) 
print(myFruitList[1])
print(myFruitList[2])

#alterando um valor da lista
myFruitList[2] = "orange"
print(myFruitList)


"Exercício 2: Apresentação do tipo de dado tupla"
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

# Acessando os itens da tupla por posição
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

"Exercício 3: Apresentação do tipo de dado dicionário"

myFavoriteFruitDictionary = {
    "Akua": "apple",
    "Saanvi": "banana",
    "Paulo": "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])