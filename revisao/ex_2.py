# O problema do chocolate

"""
Um professor precisa sorter bombons para diversos alunos. 
Esses alunos serão sorteados  randômicamente.
O número deve corresponder ao número do diário.

"""
import random

while True:
    # padrão snake_case (PEP-8)
    sorteio_turma = random.randint(1,25)
    print(sorteio_turma)
    resposta = input("Deseja sortear outro número ? (s/n)").strip().lower()
    if resposta != "s":
        print("Encerrando o sorteio ")
        break


