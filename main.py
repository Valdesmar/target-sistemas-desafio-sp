############ 1 #################
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)


############# 2 ################
def is_fibonacci(num):
    a, b = 0, 1
    while b <= num:
        if b == num:
            return f"{num} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"{num} não pertence à sequência de Fibonacci."

# Teste
numero = 21  # Pode ser substituído por qualquer outro número
print(is_fibonacci(numero))


############# 3 ##############
import json

def calcular_faturamento(dados):
    valores = [dia["valor"] for dia in dados if dia["valor"] > 0]
    
    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)
    dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)
    
    return menor_valor, maior_valor, dias_acima_da_media

# Supondo que o JSON está em um arquivo chamado 'faturamento.json'
with open('faturamento.json') as f:
    dados = json.load(f)

menor, maior, dias_acima_media = calcular_faturamento(dados)

print(f"Menor valor de faturamento: R${menor:.2f}")
print(f"Maior valor de faturamento: R${maior:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")


############### 4 ################
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento.values())

percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}

for estado, percentual in percentuais.items():
    print(f"{estado} representa {percentual:.2f}% do faturamento total.")

################### 5 ##############
def inverte_string(s):
    inverso = ""
    for char in s:
        inverso = char + inverso
    return inverso


string = "Target Sistemas"
print(f"String original: {string}")
print(f"String invertida: {inverte_string(string)}")
