import animales

menu = {
    '1':'Cacatua',
    '2':'Delfin',
    '0':'Exit'
}

class Animal:
    cacatua=0
    delfin=0
    
    animales_lista = {
        1:animales.cacatua,
        2:animales.delfin
    }
    
    def __init__(self,cacatua,delfin):
        self.cacatua = cacatua
        self.delfin = delfin

    def mostrar_animal(self,op):
        print(self.animales_lista[op])

#Ejecución principal
if __name__ == '__main__':
    
    for k,i in menu.items():
        print(f'{k}:{i}')
    
    op = int(input('Elige qué animal quieres ver: ')) #building function
    
    while True:
        
        if op == 0:
            #El usuario quiere dejar de jugar
            print("Que el código te acompañe pythonian")
            break
        elif op == 1:
            #Imprimir animal
            print(animales.cacatua)
        elif op == 2:
            print(animales.delfin)
        else:
            #Opcion invalida
            print('Opción inválida, intentelo nuevamente')
            for k,i in menu.items():
                print(f'{k}:{i}')
            
        op = int(input('Elige qué animal quieres ver: '))