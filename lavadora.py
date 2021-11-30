from electrodomesticos import Electrodomestico


class Lavadora(Electrodomestico):
    def __init__(self, precioBase=100, color="blanco", consumoEnergetico='F', peso=5, carga=5):
        Electrodomestico.__init__(self, precioBase=precioBase, color=color, consumoEnergetico=consumoEnergetico, peso=peso)
        self.carga=carga

    def precioFinal(self):
        Electrodomestico.precioFinal(self)
        if self.carga > 30:
            self.precioB = self.precioB + 50