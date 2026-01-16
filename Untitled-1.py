aluno = []
soma_notas = 0.0
quantidade_notas = 4

def menu():
    print("=" * 15 + " BOLETIM ESCOLAR " + "=" * 15)

menu()


notas_individuais = [] 

for i in range(quantidade_notas):
    while True:
        try:
            nota_str = input(f"Digite a {i + 1}ª nota: ")
            nota = float(nota_str)
            
            if 0 <= nota <= 10:
                notas_individuais.append(nota)
                soma_notas += nota
                break
            else:
                print("Nota inválida. Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número.")


if quantidade_notas > 0:
    media = soma_notas / quantidade_notas
    
    aluno.append((nome_aluno, media))
    
    print("\n--- Resultado Final ---")
    print(f"Aluno(a): {nome_aluno}")
    print(f"Soma das notas: {soma_notas:.2f}")
    print(f"Sua média é: {media:.2f}")
    print("=" * 45)
else:
    print("Não foi possível calcular a média. Nenhuma nota foi inserida.")