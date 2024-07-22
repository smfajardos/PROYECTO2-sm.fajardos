import os
from flask import Flask, render_template
from flask_restful import Api
#from dotenv import load_dotenv
from db import db
from controller.controllerindex import ControllerIndex
from controller.controllerheladeria import ControllerHeladeria
from controller.controllerproductos import ControllerProductos
from controller.controlleringredientes import ControllerIngredientes
from controller.controllerproductosingredientes import ControllerProductosIngredientes
from models.heladeria import Heladeria

#load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:Samuel0710@localhost/heladeria'
db.init_app(app)
api = Api(app)


@app.route("/")
def main():
    return "Heladería SF"

@app.route("/index")
def menu():
    heladeria = Heladeria("Heladería SF")
    items = heladeria.lista_productos()
    return render_template("index.html", items=items)

@app.route("/ingredientes")
def lst_ingredientes():
    heladeria = Heladeria("Heladería SF")
    items = heladeria.lista_ingredientes()
    return render_template("ingredientes.html", items=items)


api.add_resource(ControllerIndex, '/index')
api.add_resource(ControllerHeladeria, '/heladeria')
api.add_resource(ControllerProductos, '/productos')
api.add_resource(ControllerIngredientes, '/ingredientes')
api.add_resource(ControllerProductosIngredientes, '/productosingredientes')