import random
import time
import pandas as pd
import matplotlib.pyplot as plt
def dynamicRodCutting(p, n):  # Bottom-Up
    
    # Cria uma lista de tamanho n+1 preenchida com zeros para armazenar os resultados ótimos
    r = [0] * (n+1)  
    for j in range(1, n+1):  # Loop para cada tamanho possível da tora
        
        q = float('-inf')  # Inicializa a variável q com um valor muito baixo para encontrar o máximo
        
        for i in range(1, j + 1):  # Loop para cada possível corte da tora
            
            q = max(q, p[i-1] + r[j - i])  # Calcula o valor máximo entre o valor do corte atual e a combinação de cortes anteriores
            
        r[j] = q  # Armazena o valor máximo para o tamanho atual da tora
        
    return r[-1]  # Retorna o valor máximo para a tora de tamanho n

def greedyRodCutting(p, n):
    
    valor_total = 0  # Inicializa o valor total como zero   
    
    #se n tiver na densidadeUsada, entrar nos ifs subsequentes
    while n > 0:  # Enquanto o tamanho da tora for maior que 1
        max_densidade = float('-inf')  # Inicializa a máxima densidade com um valor muito baixo
        
        for i in range(1, n + 1):  # Loop para cada possível corte da tora
            
            densidade_atual = p[i-1] / i  # Calcula a densidade atual para o corte atual
            if i <= n: #verifica o melhor tamanho baseado no restante da tora desejada
                if densidade_atual > max_densidade:  # Verifica se a densidade atual é maior que a máxima densidade e se o corte é válido
                    max_densidade = densidade_atual  # Atualiza a máxima densidade
                    corte = i  # Armazena o tamanho do corte com a maior densidade
        valor_total += p[corte-1]  # Adiciona o valor do corte selecionado ao valor total
        n -= corte  # Reduz o tamanho da tora pelo tamanho do corte selecionado
        
        
    return valor_total  # Retorna o valor total obtido

inc = int(input("Digite o valor de início (inc): "))
fim = int(input("Digite o valor final (fim): "))
stp = int(input("Digite o intervalo entre tamanhos (stp): "))
print("\nProcessando...\n")
print("n  vDP tDP   vGreedy tGreedy %")
print("----------------------------------------------------")

results = []

for inc in range(inc, fim + 1, stp):
    p = [random.randint(1, 10) for _ in range(inc)] #constroi vetor de preços
    start = time.time()
    vDP = dynamicRodCutting(p, inc)
    tDP = time.time() - start #Calcula tempo de execução 

    start = time.time()
    vGreedy = greedyRodCutting(p, inc)
    tGreedy = time.time() - start #Calcula tempo de execução

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
# print(p)
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