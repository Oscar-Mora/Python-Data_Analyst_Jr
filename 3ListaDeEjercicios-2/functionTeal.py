# Construye un programa que al recibir dos variables T teal y OP entera obtenga el 
# resultado de la siguiente funciΓ³n.
# π(π) = { π5
# π π ππ = 1 ππ
#  π π ππ = 2 6 (π2) π π ππ = 3, 4 1 πΆπ’ππππ’πππ ππ‘ππ πππ π
# OBTENER DATOS
def get_T(msj):
    t = int(input(msj))
    return t
    
def get_OP():
    op= int()
    print("Seleccione una OP")
    print("1 - Divide T en 5")
    print("2 - PotencΓ­a T a la t")
    print("3 - Hace a 't' medios y multiplΓ­ca por 6")
    print("4 - Hace a 't' medios y multiplΓ­ca por 6")
    print("# - Averigualo")
    op = int(input())
    return op
    
# PROCESAMIENTO    Cuando hacemos casos en python se usa if selector == 1... y si queremos el valor de resultado se pone return
def funct_solution(t, op):
    if op == 1:
        caso = t/5
        return caso
    elif op == 2:
        caso = t**t
        return caso
    elif op == 3 or 4:
        caso = 6*(t/2)
        return caso
    else: ###ESTAFALLANDO EL RESULTADO DE ESTA OPCIΓN
        caso = '1 :)'
                
        return caso
        
# SALIDAS
def imprimir(msj,result):
    print(msj, result)

# MAIN
def run():
    t = get_T('Indique el valor de T: ')
    op = get_OP()

    result = funct_solution(t,op)
    imprimir('el resultado de su opciΓ³n es: ',result)    

if __name__=='__main__':
    run()
