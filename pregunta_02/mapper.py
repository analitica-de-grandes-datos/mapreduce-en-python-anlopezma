#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
import csv

for row in sys.stdin:
    elementos = row.split(',')

    amount= elementos[4]
    purpose= elementos[3]
    
    linea= purpose + ";"+ amount
    sys.stdout.write(linea+"\n")
