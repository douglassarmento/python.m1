a = int (input ('Digite o valor do cateto oposto:'))
b = int (input ('Digite o valor do cateto adjacente:'))
print ('O valor da hipotenusa é {}.'.format ((a ** 2 + b ** 2)**0.5))

from math import hypot

co = float (input ('Digite o valor do cateto oposto:'))
ca = float (input ('Digite o valor do cateto adjacente:'))
print ('O valor da hipotenusa é {}.'.format (hypot (co,ca)))