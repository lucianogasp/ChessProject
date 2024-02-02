import re
from random import choice

regex = re.compile(r'^(?:[A-Z][a-h]?[1-8]?x?[a-h][1-8]|[a-h]x[a-h][1-8]?(?:=[A-Z])?|[a-h][1-8](?:=[A-Z])?)(?:\+|\+\+|#)?$')

# Primeiro         r'^(?:[A-Z][a-h]?[1-8]? | [a-h])x?[a-h][1-8]$'
# Vencedor         r'^(?:[A-Z][a-h]?[1-8]?x?[a-h][1-8] | [a-h]x[a-h][1-8]? | [a-h][1-8])$'
# Venc resumido    r'^([A-Z][a-h]?[1-8]?x?([a-h][1-8]) | [a-h]x\1 | \1)$'
# ChatGPT:         r'^(?:[A-Z]?[a-h][1-8](?:x[a-h][1-8]?)?|[a-h][1-8])$'

strings = ['Ta5', 'Bc5', 'Cc3', 'De1', 'Rh1', 'e4', 'Txh5', 'Bfx3', 'Bg2x', 'Cxxg2', 'xDe5', 'xh2', 'cxd4', 'exd', 'fx6', 'fxx6', 'xf6', 'f6x', 'fe4x', 'fgx', 'fg4', 'dd6', 'ddxe6', 'fx5g', 'fdx5g','Cc3 e4']


letras = ' abcdefghTCBDRxxxxxxxxx++++++++++###########==============='
num = '12345678'
chrt = ' '
el = ''
lista = list()

for _ in range(5000000):
    tag = choice([0, 1, 2])
    if tag == 1:
        el += choice(letras)
    elif tag == 2:
        el += choice(num)
    else:
        lista.append(el)
        el = ''

accept = list()
reject = list()
for s in lista:
    x = regex.findall(s)
    if x:
        accept += x
    else:
        reject.append(s)

c_esp = list()
for find in accept:
#    if find.count('+') or find.count('++') or find.count('#') or find.count('='):
    if find.count('='):
        c_esp.append(find)

print(f'rejected: {reject}')
print('\n')
print(f'accepted: {accept}')
print('\n')
print(f'chrt especials: {c_esp}')
print('\n')
print(f'taxa de acerto: {len(accept)/len(lista):.5f}')
print(f'{len(accept)} / {len(lista)}')
print()
