# Fórmula: peso(kg) / [estatura(m)]2

# Por debajo de 18.5	Bajo peso
# 18.5 – 24.9	Normal
# 25.0 – 29.9	Sobrepeso
# 30.0 o más	Obesidad

def imc(peso, altura):

    return peso / altura**2


def info(i):
    if i < 18.5:
        return 'Su peso es muy bajo.'
    elif i >= 18.5 and i < 24.9:
        return 'Su peso es normal.'
    elif i >= 24.9 and i < 29.9:
        return 'Usted esta con sobrepeso.'
    elif i >= 29.9:
        return 'Usted esta en estado de obesidad.'
    else:
        return 'Error en calculo'


print("""
      Calcula el indice de masa corporal - IMC -
    """)

peso = float(input('Escriba su peso (Kg): '))
altura = float(input('Escriba su altura (mts): '))

indice = imc(peso, altura)
resultado = info(indice)

print('Su IMC es: {}'.format(indice))
print(resultado)
