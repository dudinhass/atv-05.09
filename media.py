def media():
    quantidade_notas = int(input("quantas notas você deseja inserir? "))
    notas = []
    for i in range(quantidade_notas):
        nota = int(input(f"digite a nota {i + 1}: "))
        notas.append(nota)

    media = sum(notas) / quantidade_notas
    
    print(f"a media das notas é: {media:.2f}")

media()
