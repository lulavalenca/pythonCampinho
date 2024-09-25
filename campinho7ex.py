## Solicita ao usuário se deseja enviar um pacote
userReply = input("Do you need to ship a package? (Enter yes or no) ")

# Condicional para verificar a resposta do usuário
if userReply == "yes":
    print("we can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")    
    
    
"Exercício 2: Uso da declaração else"    
# Solicita ao usuário se deseja enviar um pacote
userReply = input("Do you need to ship a package? (Enter yes or no) ")

# Condicional para verificar a resposta do usuário e fornecer uma resposta alternativa
if userReply == "yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")


"Exercício 3: Uso da declaração elif"
# Solicita ao usuário qual serviço ele deseja utilizar
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")

# Condicional com múltiplas opções de serviço
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
