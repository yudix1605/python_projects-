def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calc_digito(base):
        soma = sum(int(cpf[i]) * (base + 1 - i) for i in range(base))
        digito = (soma * 10) % 11
        return 0 if digito == 10 else digito

    return calc_digito(9) == int(cpf[9]) and calc_digito(10) == int(cpf[10])


# Loop até CPF válido
while True:
    cpf = input("Digite um CPF: ")
 
    if validar_cpf(cpf):
        print("CPF válido!")
        break
    else:
        print(" CPF inválido, tente novamente.\n")