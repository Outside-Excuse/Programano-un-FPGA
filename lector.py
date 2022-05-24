#Jorge Emiliano Turner Escalante 
#Alejandro Hidalgo Badillo A01423412 
from ast import expr
from distutils.log import error
from pickle import TRUE
import re
from tkinter import Variable

def leerExpresiones(expresiones):
     database = ['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','_']
     numData = ['1','2','3','4','5','6','7','8','9','0']
     operaciones = ['+','*','%','-']
     punto = ['.']
     parentesis = ['(',')']
     exponente = ['e']
     equal = ['=']
     #print(expresiones)
     for i in range(len(expresiones)):
         description =[]
         comentario = 0
         contador = 0
         type = []
         numeros = []
         operadores = []
         puntos = []
         puntoo = 0
         parentesis2 = []
         NUM =0
         num_par = 0
         Exponentes = []
         contador_Exp = 0
         igual = []
         contador_igual = 0
         for a in range(len(expresiones[i])):

            if expresiones[i][contador] == "/":
                if expresiones[i][contador+1] == "/":
                    comentario = comentario+1
            if (comentario != 0):
                description.append(expresiones[i][contador])



            #print(expresiones[i][contador])


            #marcar variables 
#variables---------------------->
            contador2 = 0
            typecount = []
            contador3 = 0
            numcount = []
            contador4 = 0
            operadorCount = []
            contador5 = 0
            puntoCount = []
            contador6 = 0
            parenCount = []
            contador7 = 0
            expCount = []
            contador8 = 0
            igualCount = []
            if expresiones[i][contador].lower() != " " and comentario==0: 
                for b in range(len(database)):
                    #print(database[contador2]
                    if database[contador2] == expresiones[i][contador].lower():

                       
                        typecount.append(expresiones[i][contador])
                        contador2 = contador2+ 1
                       



                    else:
                        contador2 = contador2+ 1

                cad = ''.join(typecount)
                type.append(cad)
#Numeros--------------------->
                for l in range(len(numData)):
                    if numData[contador3] == expresiones[i][contador].lower():
                        numcount.append(expresiones[i][contador])
                        contador3 = contador3+1
                        NUM = NUM +1
                    else:
                        contador3 = contador3 +1
                cod = ''.join(numcount)
                numeros.append(cod)
#Operaciones------------------->
                for j in range(len(operaciones)):
                    if operaciones[contador4] == expresiones[i][contador].lower():
                        operadorCount.append(expresiones[i][contador])
                        contador4 = contador4+1
                    else:
                        contador4 = contador4 +1
                ced = ''.join(operadorCount)
                operadores.append(ced)

                
#pontus--------------------->
                for k in range(len(punto)):
                    if punto[contador5] == expresiones[i][contador].lower():
                        puntoCount.append(expresiones[i][contador])
                        contador5 = contador5+1
                        
                        puntoo = puntoo +1
                    else:
                        contador5 = contador5+1
                cid = ''.join(puntoCount)
                puntos.append(cid)
#parentesis-------------------->
                for m in range (len(parentesis)):
                    if parentesis[contador6] == expresiones[i][contador]:
                        parenCount.append(expresiones[i][contador])
                        contador6 = contador6+1
                        num_par = num_par+1
                    else:
                        contador6 = contador6 + 1
                cud =''.join(parenCount)
                parentesis2.append(cud)
#Exponentes------------------------>
                for n in range (len(exponente)):
                    if exponente[contador7] == expresiones[i][contador].lower():
                        expCount.append(expresiones[i][contador])
                        contador7 = contador7 +1
                        contador_Exp = contador_Exp + 1
                    else:
                        contador7 = contador7+1
                doom = ''.join(expCount)
                Exponentes.append(doom)    
#Asignacion------------------------------->  
                for x in range (len(equal)):
                    if equal[contador8] == expresiones[i][contador]:
                        igualCount.append(expresiones[i][contador])    
                        contador8 = contador8 + 1
                        contador_igual = contador_igual +1
                    else:
                        contador8 = contador8 +1
                kitten = ''.join(igualCount)
                igual.append(kitten)      



                









            contador = contador +1
         

#impresiones---------------------->
         print("variables -----> ",type)
         if contador_igual > 0:
            print("Asignacion ----->",igual)
         print("Operadores -----> ",operadores)
         if NUM > 0:
            print("numeros -----> ", numeros)
        
         if num_par > 0:
             print("Parentesis -----> ", parentesis2)
         if comentario > 0:
            print("comentario -------> ", description)
         if puntoo > 0:
             print("puntos -----> ",puntos)
         if contador_Exp > 0:
             print("Exponente ----->", Exponentes)
         print("--------------------fin de operacion--------------------")
     



                    



           
     

# funcion main
def main():
    file = input("| Alejandro Hidalgo Badillo |\n| Jorge Emiliano Turner Escalante |\n            ---------------\nfavor de introducir el nombre del archivo:")
    file = file + ".txt"
    f = open(file)
    expresiones = f.readlines()
    for i in range(len(expresiones)):
        expresiones[i] = expresiones[i].replace('\n', '')
        

   
    leerExpresiones(expresiones)
main()
