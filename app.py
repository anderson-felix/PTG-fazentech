import sqlite3
import os
import time

from binarySearch import BinarySearch as bs


# def binarySearch(lista, value):
#   minimo = 0
#   maximo = len(lista) - 1
#   while minimo <= maximo:
#     meio = (minimo + maximo) // 2
#     if value < lista[meio]:
#       maximo = meio - 1
#     elif value > lista[meio]:
#       minimo = meio + 1
#     else:
#       return True
#   return False

def Search(query):
  idList = []
  for i in query:
    idList.append(i)
  return idList

# MAIN
program = -1

while program != 0:
  conn = sqlite3.connect("./fazenda.db")# confira se o seu diretório está correto
  cursor = conn.cursor()
  os.system('clear')
  print('\t____________FazenTech____________')
  print('\t___________COW CONTROL___________')



  program = int(input("""
  Digite o número correspondente a ação desejada.
  (0) - SAIR
  (1) - LISTAR VACAS ATUAIS
  (2) - CRIAR UM NOVO REGISTRO
  (3) - ATUALIZAR UM REGISTRO
  (4) - DELETAR UM REGISTRO
  (5) - BUSCA ESPECÍFICA

  -->  """))

  if program == 0:
    print('\nSaindo...')
    time.sleep(1)
    os.system('clear')

  elif program == 1:
    os.system('clear')
    print('\n\n\t____________REGISTROS____________ \n')
    for id, ordenha, ult_ordenha in cursor.execute('SELECT id, ordenhada, ult_ordenha FROM Vaca'):
      print(id, ordenha, ult_ordenha)
    os.system('pause')

  elif program == 2:
    os.system('clear')

    ordenha = str(input('A vaca já realizou o processo de ordenha? (S/N) -> ')).strip().upper()

    if ordenha == 'S':
      ult_ordenha = str(input('\nInforme a data da última ordenha -> ')).strip()
      cursor.execute(f'INSERT INTO Vaca (ordenhada, ult_ordenha) VALUES ("S","{ult_ordenha}")')

    elif ordenha == 'N':
      cursor.execute(f'INSERT INTO Vaca (ordenhada, ult_ordenha) VALUES ("N",null)')

    else:
      print('\nComando incorreto!\n')
      os.system('pause')

    print('\nRegistro criado!\n')
    os.system('pause')

  elif program == 3:
    os.system('clear')
    up = int(input('Qual o ID da vaca que deseja atualizar? -> '))
    ordenha = str(input('A vaca já realizou o processo de ordenha? (S/N) -> ')).strip().upper()

    if ordenha == 'S':
      ult_ordenha = str(input('Informe a data da última ordenha -> '))
      cursor.execute(f'UPDATE Vaca SET ordenhada="S", ult_ordenha="{ult_ordenha}" WHERE id={up}')

    elif ordenha == 'N':
      cursor.execute(f'UPDATE Vaca SET ordenhada="N", ult_ordenha=null WHERE id={up}')

    else:
      print('\nComando incorreto!\n')
      os.system('pause')

    print(f'\nRegistro {up} atualizado!\n')
    os.system('pause')

  elif program == 4:
    os.system('clear')
    up = int(input('Qual o ID da vaca que deseja deletar? -> '))
    cursor.execute(f'DELETE FROM Vaca WHERE id={up}')
    print(f'\nRegistro {up} Deletado!\n')
    os.system('pause')

  elif program == 5:
    os.system('clear')
    sql = cursor.execute('SELECT id FROM Vaca') # comando sql para executar a busca binaria.

    search = Search(sql) # a função Search vai pegar os dados do comando sql e transformar em uma lista.

    strConvert = str(search).replace("(","").replace(")","").replace(",","").replace("[","").replace("]","").split()# transformando a lista em string para fazer o tratamento, usando o replace para remover caracteres indesejados

    listConvert = list(strConvert) # adicionando os dados tratados a uma lista.

    query = []
    for i in listConvert:
      query.append(int(i))

    value = int(input('Informe um ID para verificar se ele está nos registros -> '))
    result = binarySearch(query,value)

    if result == True:
      print(f'\nO registro {value} se encontra nos registros\n ')

    else:
      print(f'\nO registro {value} não se encontra nos registros\n ')

    os.system('pause')

  else:
    os.system('clear')
    print('\nComando incorreto!\n')
    os.system('pause')

  conn.commit()
  cursor.close()
  conn.close()

