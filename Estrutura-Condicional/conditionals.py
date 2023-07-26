userReply = input("Você precisa enviar um pacote? (Digite sim ou não) ")
if userReply == "sim":
    print("Podemos ajudá-lo a enviar esse pacote!")
else:
    print("Por favor, volte quando precisar enviar um pacote. Obrigado.")
    
userReply = input("Você gostaria de comprar selos, comprar um envelope ou fazer uma cópia? (Insira selos, envelope ou copia) ")
if userReply == "selos":
    print("Temos muitos designs de selos para escolher.")
elif userReply == "envelope":
    print("Temos muitos tamanhos de envelopes para escolher.")
elif userReply == "copia":
    copies = input("Quantos exemplares você gostaria? (Digite um número) ")
    print("Aqui estão {} cópias.".format(copies))
else:
    print("Obrigado, por favor, volte.")
