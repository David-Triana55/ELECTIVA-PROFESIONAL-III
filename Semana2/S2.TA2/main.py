with open("./Archivos/Eliminatorias.txt", "r", encoding="utf-8") as f:
  lineas = f.readlines()
  diccionarioEquipos = {}

  lista = [4,35,53,2,4,5]

  for linea in lineas[1:]:

    position = linea.split('\t')
    print(linea.split('\t'))

    diccionarioEquipos[position[1]] = int(position[0].strip('.'))


  for key, value in diccionarioEquipos.items():
    print(f"{key} {value}")


    for idx, j in enumerate(lista, start= 2):
      print(f"{idx} {j}")

  print(diccionarioEquipos)