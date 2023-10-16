import random
import time
import pandas as pd
import matplotlib.pyplot as plt


def dinamicRodCutting(p, n):  # Bottom-Up
    # r armazena os valores máximos de venda para cada comprimento de tora
    r = [0] * (n + 1)

    # Loop para considerar cada possível comprimento da tora de 1 a n
    for j in range(1, n + 1):
        # Inicializa o valor máximo como '-infinito' para garantir que qualquer valor real substituirá isso
        q = float('-inf')

        # Loop interno para avaliar cada combinação de corte possível
        for i in range(1, j + 1):
            # Atualiza q para o valor máximo entre o valor atual e a nova combinação de corte
            q = max(q, p[i] + r[j - i])

        # Atualiza o valor máximo de venda para a tora de comprimento j
        r[j] = q

    # Retorna o valor máximo de venda para a tora de comprimento n
    return r[n]

def greedyRodCutting(p, n):
    # Inicializa o valor total de venda
    valor_total = 0

    # Continua enquanto houver tora para cortar
    while n > 0:
        # Inicializa a densidade máxima como '-infinito' para garantir que qualquer densidade real substituirá isso
        max_densidade = float('-inf')

        # Avalia cada possível comprimento de tora
        for i in range(1, n + 1):
            # Calcula a densidade para o comprimento i
            densidade_atual = p[i] / i

            # Atualiza a densidade máxima e o corte correspondente se a densidade atual for maior
            if densidade_atual > max_densidade :
                max_densidade = densidade_atual
                corte = i

        # Adiciona ao valor total o preço do pedaço de tora com a densidade máxima
        valor_total += p[corte]

        # Diminui a tora pelo comprimento do corte
        n -= corte

    # Retorna o valor total de venda
    return valor_total


inc = int(input("Digite o valor de início (inc): "))
fim = int(input("Digite o valor final (fim): "))
stp = int(input("Digite o intervalo entre tamanhos (stp): "))
print("\nProcessando...\n")
print("n  vDP tDP   vGreedy tGreedy %")
print("----------------------------------------------------")

results = []

for inc in range(inc, fim + 1, stp):
    p = [0] + [random.randint(1, inc) for _ in range(inc)]
    p.sort()
    start = time.time()
    vDP = dinamicRodCutting(p, inc)
    tDP = time.time() - start

    start = time.time()
    vGreedy = greedyRodCutting(p, inc)
    tGreedy = time.time() - start

    accuracy = (vGreedy / vDP) * 100
    print(f"{inc} {vDP} {tDP:.6f} {vGreedy} {tGreedy:.6f} {accuracy:.2f}")

    results.append({
        'n': inc,
        'vDP': vDP,
        'tDP': tDP,
        'vGreedy': vGreedy,
        'tGreedy': tGreedy,
        '%': accuracy
    })

# Salvar para CSV
df = pd.DataFrame(results)
df.to_csv('data.csv', index=False)

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('n')
ax1.set_ylabel('tDP', color=color)
ax1.plot(df['n'], df['tDP'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('tGreedy', color=color)
ax2.plot(df['n'], df['tGreedy'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()

fig2, ax3 = plt.subplots()

color = 'tab:red'
ax3.set_xlabel('n')
ax3.set_ylabel('vDP', color=color)
ax3.plot(df['n'], df['vDP'], color=color)
ax3.tick_params(axis='y', labelcolor=color)

ax4 = ax3.twinx()
color = 'tab:blue'
ax4.set_ylabel('vGreedy', color=color)
ax4.plot(df['n'], df['vGreedy'], color=color)
ax4.tick_params(axis='y', labelcolor=color)

fig2.tight_layout()
plt.show()