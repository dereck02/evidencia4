from laptopp import Laptop
import pytest

#Prueba para encender la laptop
@pytest.mark.parametrize("nivel_bateria, expected", [(50, "La laptop está encendida."),])
def test_encender(nivel_bateria, expected):
    laptop = Laptop(nivel_bateria)
    result = laptop.encender()
    assert result == expected

@pytest.mark.parametrize("nivel_bateria", [5,  0, ])
def test_encender_bateria_baja(nivel_bateria):
    laptop = Laptop(nivel_bateria)
    with pytest.raises(ValueError, match="Batería baja. Conéctela a la corriente para encender."):
        laptop.encender()

#Prueba para cargar la batería
@pytest.mark.parametrize("nivel_bateria, carga, expected", [
    (50, 30, "Batería cargada al 80%"),  #Carga normal
    (80, 50, "Batería cargada al 100%"),  #Batería cargada al máximo
    (90, 20, "Batería cargada al 100%"),  #No puede superar el 100%
])

def test_cargar_bateria(nivel_bateria, carga, expected):
    laptop = Laptop(nivel_bateria)
    result = laptop.cargar_bateria(carga)
    assert result == expected

@pytest.mark.parametrize("nivel_bateria, carga", [
    (50, -10),  #Carga negativa
    ])
def test_cargar_bateria_negativa(nivel_bateria, carga):
    laptop = Laptop(nivel_bateria)
    with pytest.raises(ValueError, match="La cantidad de carga no puede ser negativa."):
        laptop.cargar_bateria(carga)

#Prueba para uso de CPU
@pytest.mark.parametrize("nivel_bateria, porcentaje_uso, is_on, expected", [
    (50, 85, True, "Uso de CPU: 85%"),  # Uso normal de la CPU
    (50, 95, True, "Advertencia: Uso de CPU al límite. Uso de CPU: 95%"),  # Advertencia por uso alto de CPU
])
def test_usar_cpu(nivel_bateria, porcentaje_uso, is_on, expected):
    laptop = Laptop(nivel_bateria)
    if is_on:
        laptop.encender()  # Encender la laptop si es necesario
    result = laptop.usar_cpu(porcentaje_uso)
    assert result == expected

@pytest.mark.parametrize("nivel_bateria, porcentaje_uso", [
    (50, 85),  # Laptop apagada
])
def test_usar_cpu_laptop_apagada(nivel_bateria, porcentaje_uso):
    laptop = Laptop(nivel_bateria)
    with pytest.raises(ValueError, match="La laptop está apagada, no se puede utilizar la CPU."):
        laptop.usar_cpu(porcentaje_uso)

@pytest.mark.parametrize("nivel_bateria, porcentaje_uso", [
    (50, 110),  # Porcentaje de CPU inválido
    (50, -10),  # Porcentaje de CPU negativo
])
def test_usar_cpu_porcentaje_invalido(nivel_bateria, porcentaje_uso):
    laptop = Laptop(nivel_bateria)
    laptop.encender()  # Encender la laptop
    with pytest.raises(ValueError, match="El porcentaje de uso de CPU debe estar entre 0 y 100."):
        laptop.usar_cpu(porcentaje_uso)

# Prueba de estado de la laptop (método __str__)
@pytest.mark.parametrize("nivel_bateria, is_on, expected", [
    (50, True, "Laptop encendida, batería al 50%"),  #Laptop encendida
    (50, False, "Laptop apagada, batería al 50%"),  #Laptop apagada
])
def test_str(nivel_bateria, is_on, expected):
    laptop = Laptop(nivel_bateria)
    if is_on:
        laptop.encender()
    result = str(laptop)
    assert result == expected
