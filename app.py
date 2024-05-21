from flask import Flask,jsonify,request
import mysql.connector
import os
import sys

from avaliacao import avaliacao_bp
from pedido import pedido_bp
from produto import produto_bp
# from fatura import fatura_bp
from flask_restx import Api, Resource
from flasgger import Swagger
from functools import wraps
from db import db_mysql_class






#Criar uma instância do Flask
app = Flask(__name__)
swagger = Swagger(app)
api = Api(app, version='1.0', title='FIAP-FOOD', description='API sobre o entregavel da pós', doc='/swagger/')




app.register_blueprint(produto_bp)
app.register_blueprint(pedido_bp)
app.register_blueprint(avaliacao_bp)





#Iniciar o aplicativo se este arquivo for executado diretamente
if __name__ == '__main__':
    app.run()



