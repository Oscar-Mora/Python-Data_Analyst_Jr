# Construye un programa que al recibir dos variables T teal y OP entera obtenga el 
# resultado de la siguiente función.
# 𝑓(𝑇) = { 𝑇5
# 𝑠𝑖 𝑂𝑃 = 1 𝑇𝑇
#  𝑠𝑖 𝑂𝑃 = 2 6 (𝑇2) 𝑠𝑖 𝑂𝑃 = 3, 4 1 𝐶𝑢𝑎𝑙𝑞𝑢𝑖𝑒𝑟 𝑜𝑡𝑟𝑜 𝑐𝑎𝑠𝑜
# OBTENER DATOS
def get_T(msj):
    t = int(input(msj))
    return t
    
def get_OP():
    op= int()
    print("Seleccione una OP")
    print("1 - Divide T en 5")
    print("2 - Potencía T a la t")
    print("3 - Hace a 't' medios y multiplíca por 6")
    print("4 - Hace a 't' medios y multiplíca por 6")
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
    else: ###ESTAFALLANDO EL RESULTADO DE ESTA OPCIÓN
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
    imprimir('el resultado de su opción es: ',result)    

if __name__=='__main__':
    run()
