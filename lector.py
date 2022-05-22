



from distutils.log import error
from pickle import TRUE
import re


def leerExpresiones(expresiones):
    op = ['+', '-', '*', '/']
    par = ['(', ')']
    eq = '='
    point = '.'
    numbers = ['0','1','2','3','4','5','6','7','8','9','0']
    abc = ['a','b','c','d','f','g','h','i','j','k','l','n','m','p','q','r','s','t','u','v','w','x','y','z']
    dataBase = ['.','=','(', ')','+', '-', '*', '/','a','b','c','d','f','g','h','i','j','k','l','n','m','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','0']
    #print(par[0], par[1])
    print("lector de expresiones")
    for i in expresiones:
        conditional1 = False
        conditional2 = False
        description =[]
        parentesis = 0
        points = 0
        exponentes = 0
        variables = 0
        variables2 = []
        operacion = []
        operadores = []
        contOperadores = 0
        comentario = 0
        contadorEq = 0
        comment = []
        errorOp = False
     
        for elem in range (len(i)):
            
            operacion.append(i[elem])
# confirmar uso de comentarios
            if(i[elem]=='/'):
                if (i[elem+1]=='/'):
                    description.append("tienes un comentario")
                    comentario = comentario + 1
            if (comentario != 0):
                comment.append(i[elem])
            else:
    #confirmar el uso de variables
                for l in range (len(abc)):
                    if (i[elem].lower()==abc[l]):
                        variables = variables +1
                        variables2.append(i[elem])
    #confirmar exponente
                if (i[elem]=='e'):
                    exponentes = exponentes +1
    # confirmar uso de operadores
                for l in range (len(op)):
                    if(i[elem]==op[l]):
                        contOperadores = contOperadores + 1
                        operadores.append(i[elem])    
                        if(i[elem-1]==op[l]):
                            print("este")
                            errorOp = True 
                        if((i[elem]==op[l] and i[elem-1]== '=')):
                            errorOp = True
                        
                



    #confirmar uso de puntos
                if (i[elem]==point):
                    points = points + 1
                    #print ("points: ", points)

                #if points > 0:
                #   for l in range (11):
                #       if (i[elem-1] == numbers[l]):
                #           conditional1 = True
                #       if (i[elem+1] == numbers[l]):
                #           conditional2 = True
                #   if ((conditional2 == False) or (conditional1 == False)):
                #       description.append("error, bad use of the '.' ")
    # confirmar uso del operador igual
                if (i[elem] == eq):
                    contadorEq = contadorEq + 1
                    if (i[elem+1] == par[0]) or (i[elem+1]==par[1]):
                        for l in range (len(numbers)):
                            if (i[elem+2].lower() == numbers[l] ):
                                conditional1 = True 
                            if (i[elem+2].lower() == abc[l] ):
                                conditional2 = True 
                    else:
                        for l in range (len(numbers)):
                            if (i[elem+1].lower() == numbers[l] ):
                                conditional1 = True 
                            if (i[elem+1].lower() == abc[l] ):
                                conditional2 = True 
    #confirmar parentesis
                if (i[elem] == par[0]) or (i[elem]==par[1]):
                    parentesis = parentesis + 1
            

#confirmar errores

        if (contOperadores == 0):
            description.append("no usa operadores")
        if (errorOp == True):
            description.append("mal uso de operadores")    
        print(operacion)
        if (conditional1 == True):
            description.append("se iguala a un numero")
        if (conditional2 == True):
            description.append("se iguala a una variable")
        print("contidad de operadores = ", contOperadores)
        if(contOperadores > 0):
            print("operadores usados : ", operadores)
        print("comentarios = ",comentario)
        if (comentario > 0):
            print(comment)
        print("exponentes = ", exponentes)
        print("puntos = ",points)
        print("parentesis = ",parentesis)
        print("cantidad de variables = ",variables)
        if(variables > 0 ):
            print("variables usadas : ", variables2)
        if parentesis > 0:
            if (parentesis % 2 == 0):
                description.append("right use of parenthesis")
            else:
                description.append("error, missing parenthesis")

        if (points > 1):
            description.append("error, so many '.' ")
       
        if (exponentes > 1):
            description.append('error, mal uso de exponentes')

        print(description,"<---------------")

# funcion main
def main():
    file = input("| Alejandro Hidalgo Badillo |\n| Jorge Emiliano Turner Escalante |\n            ---------------\nfavor de introducir el nombre del archivo:")
    file = file + ".txt"
    f = open(file)
    expresiones = f.readlines()
    for i in range(len(expresiones)):
        expresiones[i] = expresiones[i].replace('\n', '')
        expresiones[i] = expresiones[i].replace(' ', '')

    print(expresiones)
    leerExpresiones(expresiones)
main()
