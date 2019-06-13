import pickle

fn = 'db.pickle'


def addSt():
    name = input('nombre del estudiante: ')
    name = name.upper()

    fichero = open(fn, 'rb')
    datos = pickle.load(fichero)
    fichero.close()

    for i in datos:
        if i == name:
            print('EL USUSRIO YA EXISTE:__________________________________')
            print('Nombre: {}, calificacion: {}'.format(i, datos[name]))
            return
    else:
        score = input('calificacion del estudiante: ')
        datos[name] = score

    fichero = open(fn, 'wb')
    pickle.dump(datos, fichero)
    fichero.close()


def read():
    fichero = open(fn, 'rb')
    datos = pickle.load(fichero)
    print('______________________________________________')
    for i in datos:
        print('.- Nombre: {}, calificacion: {}'.format(i, datos[i]))
    fichero.close()
    print('______________________________________________')


def search(name):
    fichero = open(fn, 'rb')
    datos = pickle.load(fichero)
    for i in datos:
        if i == name:
            print('______________________________________________')
            print('Nombre: {}, calificacion: {}'.format(i, datos[name]))
            return
    else:
        print('NO SE HA ENCONTRADO A {}'.format(name))
    print('______________________________________________')
    fichero.close()


def edit():
    name = input('Edita a: ')
    name = name.upper()
    score = input('Nevo promedio ')
    fichero = open(fn, 'rb')
    datos = pickle.load(fichero)
    fichero.close()
    for i in datos:
        if i == name:
            datos[name] = score
            fichero = open(fn, 'wb')
            pickle.dump(datos, fichero)
            fichero.close()
    else:
        print('NO SE HA ENCONTRADO A {}'.format(name))
    print('______________________________________________')





def delate():
    name = input('Eliminar a: ')
    name = name.upper()
    fichero = open(fn, 'rb')
    datos = pickle.load(fichero)
    del datos[name]
    print('Se ha elimiando a {}'.format(name))
    print('______________________________________________')
    fichero.close()

    fichero = open(fn, 'wb')
    pickle.dump(datos, fichero)
    fichero.close()

def menu():
    rss = int(input('1) add\n2) view All\n3) Search\n4) Editar calificacion\n5) Eliminar \n0) quit '))
    if rss == 1:
        addSt()
        menu()
    elif rss == 2:
        read()
        menu()
    elif rss == 3:
        name = input('Nombre: ')
        name = name.upper()
        search(name)
        menu()
    elif rss == 4:
        edit()
        menu()
    elif rss == 5:
        delate()
        menu()
    elif rss == 0:
        quit()
    else:
        menu()
menu()