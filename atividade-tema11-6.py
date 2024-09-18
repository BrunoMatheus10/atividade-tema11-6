# Recebe o salário bruto do usuário
salario_bruto = float(input("Digite o salário bruto (em reais): "))

# Calcula a contribuição ao INSS com base nas faixas de salário
if salario_bruto <= 1693.72:
    inss_contribuicao = salario_bruto * 0.08
elif salario_bruto <= 2822.90:
    inss_contribuicao = salario_bruto * 0.09
else:
    inss_contribuicao = salario_bruto * 0.11

# Calcula o salário líquido (descontando a contribuição ao INSS)
salario_liquido = salario_bruto - inss_contribuicao

# Exibe os resultados
print("Contribuição ao INSS: R$",inss_contribuicao)
print("Salário líquido restante: R$",salario_liquido)
