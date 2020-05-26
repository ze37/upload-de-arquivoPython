import meuprojeto
import statistics
import json

pode_parar = False
lista_entrevistados = []

# Ler o arquivo  json


def pega_dados(obj):
    instancia = meuprojeto.Entrevista(
        nome=obj["nome"],
        idade=obj["idade"],
        ano=obj["ano"]
    )
    return instancia


try:
    arquivo_json = open("dados.json", "r")
    dados_json = json.load(arquivo_json)
    entrevistas = dados_json['Entrevistas']
    lista_entrevistados = [pega_dados(entrevista)for entrevista in entrevistas]
except Exception as erro:
    print("Ocorreu um erro ao carregar o arquivo.")
    print(f'O erro é: {erro}')


while pode_parar == False:
    entrevistado = meuprojeto.Entrevista()
    if entrevistado.pergunta_nome().lower() == 'parar':
        pode_parar = True
    else:
        try:
            entrevistado.pergunta_idade()
            # x = 1000 / 0
        except ZeroDivisionError:
            print("Ocorreu um erro mas a lista foi salva")
            lista_entrevistados.append(entrevistado)
        except Exception as erro:
            print("Ocorreu um erro mas a lista NAO foi salva")
            print(f'O tipo de erro foi {(type(erro))}')
            print(f'A menssagen foi {erro}')
        else:
            lista_entrevistados.append(entrevistado)
lista_salvar = [
    dict(nome=obj.nome, ano=obj.ano_informado, idade=obj.idade)
    for obj in lista_entrevistados

]
dict_salvar = {'Entrevistas': lista_salvar}
dict_salvar = json.dumps(dict_salvar, indent=4, sort_keys=False)
try:
    arquivo_json = open("dados.json", "w")
    arquivo_json.write(dict_salvar)
    arquivo_json.close()
except Exception as erro:
    print("Ocorreu um erro ao carregar o arquivo.")
    print(f'O erro é: {erro}')

    # Gravar o arquivo JSON

    # Mostra a menor idade calculada
    # Mostra a maior idade calculada
    # Mostra a media de  idades dos adultos
    # mostra a quantidade de nascimento por decadas
menor_idade = min([objeto.idade for objeto in lista_entrevistados])
maior_idade = max([objeto.idade for objeto in lista_entrevistados])

media_adultos = statistics.median_high([
    objeto.idade for objeto in lista_entrevistados if objeto.idade >= 18])

# Mostrar a quantidade de nascimentos por decadas
# O que temos: [1970, 1981, 1998, 2002, 1990, 1970 ]
# 1o passo: converter anos em decadas
# 2o passo: criar uma lista nova com as decadas sem repetir
# 3o passo: contar as decadas na lista original usando a lista nova
# O que queremos:{1980: 10, 1990: 15, 2000: 5}

# 1985 / 10 = 198,5 int -> 198 * 10 = 1980

lista_decadas = [int(objeto.ano_informado / 10) *
                 10 for objeto in lista_entrevistados]
set_decadas = set(lista_decadas)
qtd_nascimento = {decada: lista_decadas.count(
    decada) for decada in set_decadas}

print("\nResultados:")
print('-------------------------------')
print(f'Quantidade de Entrevistas: {len(lista_entrevistados )}')
print(f'Menor idade informada: {(menor_idade)}')
print(f'Maior idade informada: {(maior_idade)}')
print(f'Media de idade dos adultos informados: {(media_adultos)}')
print('\nNascimento por decadas')
print('-------------------------------')
for decada, quantidade in qtd_nascimento.items():
    print(f'{decada}: {quantidade} nascimentos')
print('\n')
