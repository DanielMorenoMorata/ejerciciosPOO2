class Electrodomestico:
    def __init__(self, precioBase=100, color="blanco", consumoEnergetico='F', peso=5):
        if color in ("blanco", "negro", "rojo", "azul", "gris"):
            self.color=color
        self.precioB = precioBase
        self.comprobarConsumoEnergetico(consumoEnergetico)
        self.peso = peso

    def comprobarConsumoEnergetico(self, letra):
        if letra in ("A", "B", "C", "D", "E", "F"):
            self.consumo = letra

    def precioFinal(self):
        if self.consumo == 'A':
            self.precioB = self.precioB + 100
        elif self.consumo == 'B':
            self.precioB = self.precioB + 80
        elif self.consumo == 'C':
            self.precioB = self.precioB + 60
        elif self.consumo == 'D':
            self.precioB = self.precioB + 50
        elif self.consumo == 'E':
            self.precioB = self.precioB + 30
        elif self.consumo == 'F':
            self.precioB = self.precioB + 10

        if 0 < self.peso < 20:
            self.precioB = self.precioB + 10
        elif 20 < self.peso < 49:
            self.precioB = self.precioB + 50
        elif 50 < self.peso < 79:
            self.precioB = self.precioB + 80
        elif self.peso < 80:
            self.precioB = self.precioB + 100

