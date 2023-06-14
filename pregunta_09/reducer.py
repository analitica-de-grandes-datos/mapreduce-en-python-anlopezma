#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

with open('data.csv', 'r') as archivocsv:
    for line in archivocsv:
        line = line.strip()
        columns = line.split("  ")

        if len(columns) >= 3:
            value = float(columns[2])
            print(f'{value}\t{line}')
