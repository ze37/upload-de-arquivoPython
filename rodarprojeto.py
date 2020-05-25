import meuprojeto

pode_parar = False
lista_entrevistados = []

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


# Mostra a menor idade calculada
# Mostra a maior idade calculada
# Mostra a media de  idades dos adultos
# mostra a quantidade de nascimento por decadas
menor_idade = min([objeto.idade for objeto in lista_entrevistados])
maior_idade = max([objeto.idade for objeto in lista_entrevistados])

print(menor_idade)
print(maior_idade)
