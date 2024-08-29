def mostrar_nome():                            # Foi criado um bloco de códigos que não será executado até que o mesmo seja 'chamado'
    print("Olá, Fernando")                      # Visto isso que, foi dado o print e nada aconteceu, pois o código está aguardando para ser 'chamado'

mostrar_nome()
mostrar_nome()

print("*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*")

def somar_numeros(numero_1, numero_2):
    print(numero_1 + numero_2)

somar_numeros(10,20)

def somar_numeros(numero_1, numero_2,numero_3):
    print(numero_1 + numero_2 + numero_3)

somar_numeros(10,20,30)

def somar_numeros(numero_1, numero_2):
    return numero_1 + numero_2

resultado = somar_numeros(30,40)
print(resultado)

print("*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*")

def mostrar_nome(nome):
    print(f"Olá, {nome}")

mostrar_nome("Aristóteles")