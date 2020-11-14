class BinarySearch:
  def binarySearch(lista, value):
  minimo = 0
  maximo = len(lista) - 1
  while minimo <= maximo:
    meio = (minimo + maximo) // 2
    if value < lista[meio]:
      maximo = meio - 1
    elif value > lista[meio]:
      minimo = meio + 1
    else:
      return True
  return False