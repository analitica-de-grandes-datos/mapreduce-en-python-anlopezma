#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

lines = sys.stdin.readlines()

sorted_lines= sorted(lines, key=lambda x: x.split(",")[1])

for line in sorted_lines:
  print(line.strip())
