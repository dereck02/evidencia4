class Laptop:
    def __init__(self, nivel_bateria):
        if nivel_bateria < 0 or nivel_bateria > 100:
            raise ValueError("El nivel de batería debe estar entre 0 y 100.")
        self.nivel_bateria = nivel_bateria
        self.is_on = False

    # Encendido
    def encender(self):
        if self.nivel_bateria <= 5:
            raise ValueError("Batería baja. Conéctela a la corriente para encender.")
        self.is_on = True
        return f"La laptop está encendida."

    def __str__(self):
        return f"Laptop {'encendida' if self.is_on else 'apagada'}, batería al {self.nivel_bateria}%"
    
    # Batería Carga
    def cargar_bateria(self, carga):
        if carga < 0:
            raise ValueError("La cantidad de carga no puede ser negativa.")
        self.nivel_bateria = min(100, self.nivel_bateria + carga)
        return f"Batería cargada al {self.nivel_bateria}%"

    # Uso de CPU
    def usar_cpu(self, porcentaje_uso):
        if porcentaje_uso < 0 or porcentaje_uso > 100:
            raise ValueError("El porcentaje de uso de CPU debe estar entre 0 y 100.")
        if not self.is_on:
            raise ValueError("La laptop está apagada, no se puede utilizar la CPU.")
        
        if porcentaje_uso > 90:
            return f"Advertencia: Uso de CPU al límite. Uso de CPU: {porcentaje_uso}%"
        return f"Uso de CPU: {porcentaje_uso}%"

