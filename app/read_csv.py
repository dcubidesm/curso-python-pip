#Permite leer un archvio csv

import csv


def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []  #guardar una lista de diccionarios
    print(header)
    for row in reader:
      iterable = zip(header, row)  ##union de dos listas array de tuplas
      #pasarlo como un diccionario compenhesion
      country_dic = {key: value for key, value in iterable}
      data.append(country_dic)
    return data


if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])

#ejercicio: import csv
"""
def read_csv(path):
   total = 0
   with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      for row in reader:
         total += int(row[1])
   return total

response = read_csv('./data.csv')
print(response)

"""
