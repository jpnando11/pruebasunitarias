class CalculadoraDescuento:
    def __init__(self, precio_original, porcentaje_descuento):
        self.precio_original = precio_original
        self.porcentaje_descuento = porcentaje_descuento

    def validar_precio(self):
        if self.precio_original <= 0:
            raise ValueError("El precio original debe ser mayor que cero.")
    
    def validar_descuento(self):
        if not (0 <= self.porcentaje_descuento <= 100):
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
    
    def calcular_precio_final(self):
        # Validamos los valores antes de calcular
        self.validar_precio()
        self.validar_descuento()
        
        # Calculamos el descuento y el precio final
        descuento = self.precio_original * (self.porcentaje_descuento / 100)
        precio_final = self.precio_original - descuento
        return precio_final
