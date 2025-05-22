lista = [7.5, 8.0, 6.5, 9.0, 10.0]

def calcular_media(numeros):
    
    nota = sum(numeros) / len(numeros)
    if nota < 4: "reprovado"
    if nota > 4 < 6: "recuperacao"
    if nota > 6: "aprovado"

media = calcular_media(lista)
print("A média das notas é: ", media)

#Crie um teste para a função média, se o aluno tirar menos que 4 está reprovado, se tirar entre 4 e 6 de recuperação e se tirar acima de 6 está aprovado
