#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    columns = line.split().split(",")

   if len(columns) >=2:

        key= columns[1]
        value = line.strip()

        print(f"{key}\t{value}")

