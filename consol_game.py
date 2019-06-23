dividendo = int(input('dividendo de 5 cifras:   '))
com = str(dividendo)
tam = len(com)

divdo = ''
for n in com:
    divdo += n

if tam < 5:
    print('error: {} cifras'.format(tam))
    del dividendo
    dividendo = int(input('dividendo de 5 cifras:   '))

divisor = int(input('divisor de 2 cifras:   '))
com = str(divisor)
tam = len(com)

if tam < 2:
    print('error: {} cifras'.format(tam))
    del divisor
    divisor = int(input('dividendo de 5 cifras:   '))

res = dividendo/divisor

key = str(res)
secKey = []
temp = []

for n in key:
    temp.append(n)

end = temp.index('.')

for i in range(end):
    r = temp[i]
    secKey.append(r)
tamSecKey = len(secKey)

holder = ''
for s in secKey:
    holder += '° '

#print(secKey)


print("""
INICIEMOS:

 Pista -> {}
          _______
       {} |{}
VEAMOS QUE TAN BUENO ERES ...

Recuarda como es la divicion tenemos 2 cifras como divisor {} y nuestro
dividendo cuenta con las 2 primeras cifras de {}, cunatas veces cabe el 
{} en {}?... Exacto y nos sobra 'X' ahora tenemos lo que nos sobra que es
'X' y bajamos el trecer numero quedando: X{}, ahora cuantas veces cabe 
{} en X{} ... y asi sucesivamente hasta que agotes las cifras de tu 
dividendo (hasta que te encuentres en tu ultima cifra {}) 

LA PISTA ES EL NUMERO QUE RESULTA DE TU DIVICION, VE COLOCANDO LOS 
NUMEROS UNO A UNO.
BUENA SUERTE !

""".format(holder, divisor, dividendo, divisor, divdo[:2], divisor, divdo[:2], divdo[3], divisor,divdo[3], divdo[-1]))

contador = 0

for i in range(tamSecKey):
    c = int(i) + 1
    nRes = input('numero {}?    '.format(c))
    if nRes in secKey[i]:
        print('ok')
        contador += 1
    else:
        print('SANTOS GUACAMOLES ESO NO ES !!!!')

status = 0
if contador == int(len(secKey)):
    status = 0
elif contador == int(len(secKey))-1:
    status = 1
elif contador == int(len(secKey))-2:
    status = 2
word = [
    'Genial eres un genio de las mates !',
    'Puedes mejorar :)',
    'Te fue algo mal pero puedes mejorar :] !'
]
print("""
HEMOS CONCLUIDO TUS RESPUESTAS {} DE {}:
{}

""".format(contador, len(secKey), word[status]))

