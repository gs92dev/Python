"""userReply = input("Do you need to ship a package? (Enter yes or no) ")

if userReply == "yes":
    print("We can help you ship that package!")
    
elif userReply == "no":
    print("oi")
else :
    print("try again")"""

usuario = input("Qual serviço voce deseja?   Digite carta, envelope ou enviar")

if usuario == "carta":
    print("quantas cartas?")
elif usuario == "envelope":
    print("Qual cor do envelope")
else :
    print("Você precisa enviar")
    