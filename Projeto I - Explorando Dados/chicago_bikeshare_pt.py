#Primeiro vamos importar as bibliotecas
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# ToDo: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

for line in range(1,21):
    print(str(line))
    print(data_list[line])

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# ToDo: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

for i, line in enumerate(data_list[:20],start=1):
    print(f"Line : {i}\tGender: {line[-2]}")

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# ToDo: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem

def column_to_list(data, index):
    '''
        Função que adiciona as colunas(features) de uma lista em outra lista, na mesma ordem.
    Argumentos:
        data: Dataframe utilizado.
        index: O número da coluna que será utilizada.
    Retorna:
        Uma lista de valores referentes a coluna.
    '''
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for line in range(0, len(data)):
        linha = data_list[line]
        column_list.append(linha[index])
    return column_list

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])
print(len(column_to_list(data_list, -2)))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# ToDo: Conte cada gênero. Você não deveria usar uma função para isso.
lst = column_to_list(data_list, -2)
male = 0
female = 0
for item in lst:
    if item == 'Male':
        male += 1
    elif item == 'Female':
        female += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# ToDo: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)

def count_gender(lista):
    '''
     Função que faz a contagem de pessoas de cada gênero.
    Argumentos:
        lista: Arquivo lido.
    Retorna:
        Uma lista com o total de Masculinos e Femininos.
    '''
    male = 0
    female = 0
    for line in lista:
        if line[-2] == "Male":
            male += 1
        if line[-2] == "Female":
            female += 1
    return [male, female]

print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# ToDo: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.

def most_popular_gender(lista):
    '''
        Argumentos
            lista: Arquivo lido.
        Retorna:
            Qual o gênero com maior contagem de registros, ou se a contagem é o mesma.
    '''

    resposta = ""
    male, female = count_gender(lista)
    if male > female:
        resposta = "Male"
    elif female > male:
        resposta = "Female"
    else:
        resposta = "Equal"
    return resposta


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")


# TAREFA 7
# ToDo: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")
'''
    Argumentos:
        lista: arquivo lido
    Retorna:
        Uma lista de dois valores, sendo Customer ou Subscriber.
'''
def count_type(lista):
    customer = 0
    subscriber = 0
    for line in lista:
        if line[-3] == "Customer":
            customer += 1
        if line[-3] == "Subscriber":
            subscriber += 1
    return [customer, subscriber]

gender_list = column_to_list(data_list, -3)
types = ["Customer", "Subscriber"]
quantity = count_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de CLiente')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Cliente')
plt.show(block=True)


input("Aperte Enter para continuar...")
# TAREFA 8
# ToDo: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque existem linhas sem a coluna de gênero preenchida. Portanto não foram contabilizadas."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# ToDo: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)

max_trip = 0.
for item in trip_duration_list:
    if float(item) > max_trip:
        max_trip = float(item)

min_trip = 0.
temp = max_trip
for item in trip_duration_list:
    if float(item) < temp:
        min_trip = float(item)
        temp = float(item)

mean_trip = 0.
for item in trip_duration_list:
    mean_trip = mean_trip + float(item)
mean_trip = mean_trip / len(trip_duration_list)

print('O TIPO DA trip_duration_list É: ', type(trip_duration_list))
print('O TIPO Do elemento em trip_duration_list É: ', type(trip_duration_list[0]))


def median(valor_col):
    '''
   Argumentos
        valor_col: Lista com valores numéricos de uma das colunas do arquivo lido
    Retorna:
        A mediana dos valores em formato string
    '''

    n = len(valor_col)
    soma = 0
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(valor_col)[n//2]
    else:
        for calc in sorted(valor_col)[n//1:n//3]:
            soma += calc
        return soma/2
    
trip_duration_list = list(map(int, trip_duration_list))
median_trip = median(trip_duration_list)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# ToDo: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list, 3))


print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")

# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:

# def new_function(param1: int, param2: str) -> list:

'''
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.
'''

input("Aperte Enter para continuar...")

# TAREFA 12 - Desafio! (Opcional)
# ToDo: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    item_types = list(set(columns_list))
    count_items = [0 for _ in item_types]
    
    for elem in column_list:
        index = item_types.index(elem)
        count_items[index] +=1
        
    return item_types, count_items

if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -3)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
