nota1 = int(input("me diga uma nota: "))
nota2 = int(input("me diga uma nota: "))
nota3 = int(input("me diga uma nota: "))
nota4 = int(input("me diga uma nota: "))

media = (nota1 + nota2 + nota3 + nota4) /4
print(f"sua media é {media}")

if media >=7:
    print("aprovado")

else:
    print("reprovado")