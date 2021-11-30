from electrodomesticos import Electrodomestico
from lavadora import Lavadora
from television import Television

electrodomestico = ()
electrodomestico = list(electrodomestico)

electrodomestico.insert(-1, Electrodomestico(consumoEnergetico="B", peso=51, color="rojo"))
electrodomestico.insert(-1, Electrodomestico(consumoEnergetico="D", peso=9, precioBase=200))
electrodomestico.insert(-1, Electrodomestico(consumoEnergetico="B", peso=24, color="azul", precioBase=300))
electrodomestico.insert(-1, Electrodomestico(consumoEnergetico="B", peso=81))

electrodomestico.insert(-1, Lavadora(consumoEnergetico="E", peso=39, carga=64, color="gris"))
electrodomestico.insert(-1, Lavadora(consumoEnergetico="B", peso=49, carga=96, precioBase=300))
electrodomestico.insert(-1, Lavadora(consumoEnergetico="E", peso=13, carga=39, color="blanco", precioBase=150))

electrodomestico.insert(-1, Television(peso=20, resolucion=43))
electrodomestico.insert(-1, Television(peso=15, resolucion=40))
electrodomestico.insert(-1, Television(peso=14, resolucion=34))

tv, lava, electrodomestico = 0, 0, 0
i = 0
for ele in electrodomestico:
    i = i+1
    ele.precioFinal()

    if isinstance(ele,Television):
        tv += ele.precioBase
    elif isinstance(ele,Lavadora):
        lava += ele.precioBase
    else:
        electrodomestico += ele.precioBase

print("Total de televisores: " + repr(tv))
print("Total de lavadoras: " + repr(lava))
print("Total de electrodomésticos: " + repr(electrodomestico))

print("Total: " + repr(tv + lava + electrodomestico))