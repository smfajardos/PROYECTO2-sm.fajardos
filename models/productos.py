from db import db
from models.productosingredientes import ProductosIngredientes
import models.funciones as Funciones


class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(), nullable=False)
    precio_publico = db.Column(db.Float(), nullable=False)
    vaso = db.Column(db.String(), nullable=True)
    volumen = db.Column(db.Integer(), nullable=True)

    ingredientes = db.relationship('ProductosIngredientes', backref="ingredientes", lazy=True)

    def __init__(self, nombre: str, precio_publico: float, vaso: str,  volumen: int, ingredientes: list):
        self.nombre = nombre
        self.precio_publico = precio_publico
        self.vaso = vaso
        self.volumen = volumen
        self.lst_ingredientes = ingredientes

    def calcular_calorias(self) -> float:
        lista_calorias = []
        for ingrediente in self.ingredientes:
            lista_calorias.append(ingrediente.calorias)
        if self.vaso is None:
            '''Malteada'''
            return Funciones.contar_calorias_malteada(lista_calorias) + 200
        else:
            '''Copa'''
            return Funciones.contar_calorias_copa(lista_calorias)

    def calcular_costo(self) -> float:
        if self.vaso is None:
            '''Malteada'''
            return Funciones.calcular_costo_producto(self.ingredientes) + 500
        else:
            '''Copa'''
            return Funciones.calcular_costo_producto(self.ingredientes)

    def calcular_rentabilidad(self):
        return Funciones.calcular_rentabilidad_producto(self.precio_publico, self.ingredientes)