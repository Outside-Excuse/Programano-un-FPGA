import string

def verificarToken(token):
    if token[1] in string.ascii_letters:
        token_type = 'variable'

    return token_type

def identificarCaso(res):
    caso = ''
    p_states = []
    state = []

    return caso
    
def leerExpresiones(exp):
    token_list = []
    op = ['+', '-', '*', '/']
    par = ['(', ')']
    eq = '='

    token = ''

    a_state = False
    par_count = 0
    msg = 'Expresion invalida'
    caso = False

    for elem in exp:
        for i in range(len(elem)):

            if elem[i] not in op and elem[i] not in par and elem[i] != eq and elem[i] != ' ':
                token += elem[i]

            elif elem[i] in op:
                if token != '':
                    #res = verificarToken(token)
                    #caso = identificarCaso(res)
                    if caso:
                        token_list.append((token, msg))
                        pass
                    else:
                        token_list.append((token))
                token = ''
                token_list.append((elem[i], "operador"))

            elif elem[i] in par:
                if token != '':
                    #res = verificarToken(token)
                    #caso = identificarCaso(res)
                    if caso:
                        token_list.append((token, msg))
                        pass
                    else:
                        token_list.append((token))
                token = ''
                if elem[i] == par[0]:
                    token_list.append((elem[i], "Par izquierdo"))
                else:
                    token_list.append((elem[i], "Par derecho")) 

                if elem[i] == par[0]:
                    par_count += 1
                else:
                    par_count -= 1

            elif elem[i] == eq:
                if token != '':
                    #res = verificarToken(token)
                    #caso = identificarCaso(res)
                    if caso:
                        token_list.append((token, msg))
                        pass
                    else:
                        token_list.append((token))
                token = ''
                token_list.append((elem[i], "Asignacion"))

            try:
                elem[i+1]
            except:
                if token != '':
                    #res = verificarToken((token, res))
                    #caso = identificarCaso(res)
                    if caso:
                        token_list.append((token, msg))
                        pass
                    else:
                        token_list.append((token, 'Par count ' + str(par_count)))
                token = ''

    print(token_list)





def lexerAritmetico (file):
    try: 
        f = open(file)
        expresiones = f.readlines()
        
        for i in range(len(expresiones)):
            expresiones[i] = expresiones[i].replace('\n', '')

        leerExpresiones(expresiones)

    finally:
        f.close()

file = input("Ingresa el nombre del archivo: ")

lexerAritmetico(file)
