"""
Pergunta e calcula a estatisticas de idade das listas_entrevistados

Este codigo é dividido em 4 partes
1a. parte ler o arquivo json
2a. parte fazendo novas perguntas
3a. parte salvando tudono arquivo
4a. parte calculando e mostrando as estatisticas
"""
import meuprojeto
import statistics
import json
import sh


def carrega_dados():
    """
    Carrega as informaçoes do arquivo json.

    Popula a lista lista_entrevisados com instancia da classe.
    Entrevista com os valores que vem do arquivo json.
    """
    global lista_entrevistados

    def pega_dados(obj):
        """
        Cria uma instancia nova de Entrevista.

        Usa os dados vindo do json atraves do objeto 'obj'
        para nome, idade e ano_informado
        Retorna a instancia Entrevista()
        """

        instancia = meuprojeto.Entrevista(
            nome=obj["nome"],
            idade=obj["idade"],
            ano=obj["ano"]
        )
        return instancia

    try:
        arquivo_json = open("dados.json", "r")  # Abre o arquivo no disco
        # Converte em um diconario json ->python
        dados_json = json.load(arquivo_json)
        entrevistas = dados_json['Entrevistas']
        lista_entrevistados = [pega_dados(entrevista)
                               for entrevista in entrevistas]
    except Exception as erro:
        print("Ocorreu um erro ao carregar o arquivo.")
        print(f'O erro é: {erro}')


def novos_dados():
    """
    Pergunta novos nomes e anos de nascimentos.
    Enquanto o usuarioo digitar 'parar' ao perguntado o nome
    o programa pergunta o ano de nascimento e calcula a idade
    """

    pode_parar = False

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


def salvar_dados():
    """
    Salva as informaçoes geradas num arquivo json.
    Converte o dicionario Python para JSON e salva os dados da lista
    'lista_entrevistados
    Cria a lista no formato [{nome=obj.nome, ano=obj.ano_informado, idade=obj.idade}]
    Transforma a lista em um dicionario {"Entrevistas":lista}
    """

    lista_salvar = [
        dict(nome=obj.nome, ano=obj.ano_informado, idade=obj.idade)
        for obj in lista_entrevistados

    ]
    dict_salvar = {'Entrevistas': lista_salvar}
    dict_salvar = json.dumps(dict_salvar, indent=4, sort_keys=False)
    try:
        arquivo_json = open("dados.json", "w")  # Abre o arquivo e limpa
        arquivo_json.write(dict_salvar)  # Escreve os dados no arquivo
        arquivo_json.close()  # Fecha e salva o arquivo
    except Exception as erro:
        print("Ocorreu um erro ao carregar o arquivo.")
        print(f'O erro é: {erro}')


def calcular_dados():
    """
    Calcula as estatisticas de idades>:

    1. Mostra a menor idade calculada
    2. Mostra a maior idade calculada
    3. Mostra a media de  idades dos adultos
    4. Mostrar a quantidade de nascimentos por decadas

    O que temos: [1970, 1981, 1998, 2002, 1990, 1970 ]
    O que queremos:{1980: 10, 1990: 15, 2000: 5}

    1o passo: converter anos em decadas
    1985 / 10 = 198,5 int -> 198 * 10 = 1980
    2o passo: criar uma lista nova(set_decadas) com as decadas sem repetir
    3o passo: contar as decadas na lista original(lista_decadas) usando a lista nova
    Para cada decada dentro da lista nova(set_decadas)contar qtd vezes
    ela ela apareçe na lista original(lista_decadas)

    """

    menor_idade = min([objeto.idade for objeto in lista_entrevistados])
    maior_idade = max([objeto.idade for objeto in lista_entrevistados])

    media_adultos = statistics.median_high([
        objeto.idade for objeto in lista_entrevistados if objeto.idade >= 18])

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
    print('\n\n')
    resposta_ok = False
    while resposta_ok == False:
        try:
            resposta = input('Deseja mostrar os dados num arquivo ?(s/n')
            resposta = resposta[0].lower()
            if resposta == 's' or resposta == 'n':
                resposta_ok = True
        except:
            continue
    if resposta == 's':
        sh.gedit("dados.json")


carrega_dados()
novos_dados()
salvar_dados()
calcular_dados()
