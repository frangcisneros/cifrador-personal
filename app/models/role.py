# Importa el decorador dataclass desde el módulo dataclasses
from dataclasses import dataclass

# Define una clase llamada Role utilizando el decorador dataclass
@dataclass(init=False, repr=True, eq=True)
class Role:
    # Define los campos de la clase Role
    name: str  # Campo para el nombre del rol (tipo str)
    description: str  # Campo para la descripción del rol (tipo str)
