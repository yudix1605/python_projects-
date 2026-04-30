def inserir_notas():
    num_notas = int(input("Quantas notas deseja inserir?"))
    notas = []

    for i in range(num_notas):
        nota = float(input(f"Informe a sua nota {i + 1}:"))
        notas.append (nota)

    return notas 
    


def calcular_media(notas):
    if not notas:
        return 0
    else:
        return sum(notas)/len(notas)
    


def exibir_resultados(notas, media):
    print("\n notas inseridas: ", notas)
    print(f"media das notas: {media:.2f}")


def main():
    
    print("descubra sua media")


    notas_alunos = inserir_notas()
    media_notas = calcular_media (notas_alunos)
    exibir_resultados(notas_alunos, media_notas)

if __name__ == "__main__":
    main()
