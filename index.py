# Solicita ao usuário o número de alunos
num_alunos = int(input("Digite o número de alunos: "))

# Variável para armazenar a média geral da turma
media_geral = 0

# Loop para iterar sobre cada aluno
for i in range(num_alunos):
    # Solicita o nome do aluno
    nome_aluno = input(f"Digite o nome do aluno {i+1}: ")

    # Solicita as três notas do aluno
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    # Calcula a média do aluno
    media_aluno = (nota1 + nota2 + nota3) / 3

    # Verifica se o aluno foi aprovado ou reprovado
    if media_aluno >= 7.0:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    # Exibe os detalhes do aluno
    print(f"\nAluno: {nome_aluno}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média: {media_aluno:.2f}")
    print(f"Situação: {situacao}\n")

    # Adiciona a média do aluno à média geral da turma
    media_geral += media_aluno

# Calcula a média geral da turma
media_geral /= num_alunos

# Exibe a média geral da turma
print(f"Média geral da turma: {media_geral:.2f}")
