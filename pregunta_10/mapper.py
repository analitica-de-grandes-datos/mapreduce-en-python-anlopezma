#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

with open('data.csv', 'r') as archivocsv:
    for line in archivocsv:
        line = line.strip()
        columns = line.split("\t")

        if len(columns) >= 2:
            letters = columns[1].split(",")  
            number = columns[0]

            for letter in letters:
                print(f'{letter}\t{number}')
