#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
 for line in sys.stdin:
    credit_history = line.split(',')[2]
    sys.stdout.write("{}\t1\n".format(credit_history))
