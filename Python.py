idade = int(input("Digite sua idade"))
if(idade)<16:
    print("Não precisa votar")
elif(idade)==16 || idade > 65):
    print("Voto não obrigatório")
else:
    print("Voto obrigatório")
