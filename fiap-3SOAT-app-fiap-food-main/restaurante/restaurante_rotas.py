from flask import Blueprint, jsonify,request
import sys
from db import db_mysql_class
from flasgger import swag_from


restaurante_bp = Blueprint('restaurante', __name__)


#Rota para criar um novo restaurante
@restaurante_bp.route('/restaurante/cria_restaurante', methods=['POST'])
@swag_from('../swagger_yaml/create_restaurante.yaml')
def create_restaurante():
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor()
    try:
        data = request.json
        query = "INSERT INTO restaurante (nome, rua, numero, bairro, cep, estado, cidade, descricao, categoria, cnpj) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (data['nome'], data['rua'], data['numero'], data['bairro'], data['cep'], data['estado'], data['cidade'], data['descricao'], data['categoria'], data['cnpj'])
        cursor.execute(query, values)
        conn.commit()
        return jsonify({"message": "Restaurante criado com sucesso"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()



# Rota para recuperar todos os restaurantes
@restaurante_bp.route('/restaurante/consulta_restaurante/<int:id>', methods=['GET'])
@swag_from('../swagger_yaml/get_restaurantes.yaml')

def get_restaurantes(id):
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = "SELECT * FROM restaurante WHERE id_restaurante = %s"
        cursor.execute(query, (id,))
        restaurante = cursor.fetchone()
        if restaurante:
            return jsonify(restaurante), 200
        else:
            return jsonify({"message": "restaurante não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()




# Rota para atualizar um restaurante pelo ID
@restaurante_bp.route('/restaurante/atualiza_restaurante/<int:id>', methods=['PUT'])
@swag_from('../swagger_yaml/update_restaurante.yaml')
def update_restaurante(id):
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor()
    try:
        data = request.json
        query = "UPDATE restaurante SET nome = %s, rua = %s, numero = %s, bairro = %s, cep = %s, estado = %s, cidade = %s, descricao = %s, categoria = %s, cnpj = %s  WHERE id_restaurante = %s"
        values = (data['nome'], data['rua'], data['numero'], data['bairro'], data['cep'], data['estado'], data['cidade'], data['descricao'], data['categoria'], data['cnpj'], id)
        cursor.execute(query, values)
        conn.commit()
        return jsonify({"message": "Restaurante atualizado com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()








# Rota para excluir um restaurante pelo ID
@restaurante_bp.route('/restaurante/deleta_restaurante/<int:id>', methods=['DELETE'])
@swag_from('../swagger_yaml/delete_restaurante.yaml')
def delete_restaurante(id):
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor()
    try:
        query = "DELETE FROM restaurante WHERE id_restaurante = %s"
        cursor.execute(query, (id,))
        conn.commit()
        return jsonify({"message": "Restaurante excluído com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()









# Rota para recuperar todos os restaurantes
@restaurante_bp.route('/restaurante/consulta_all/', methods=['GET'])
@swag_from('../swagger_yaml/get_restaurantes_all.yaml')
def get_restaurantes_all():
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = "SELECT * FROM restaurante"
        cursor.execute(query)
        restaurante = cursor.fetchall()
        if restaurante:
            return jsonify(restaurante), 200
        else:
            return jsonify({"message": "restaurante não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()







# Rota para recuperar todos os restaurantes
@restaurante_bp.route('/restaurante/consulta_categoria/<string:categoria>', methods=['GET'])
@swag_from('../swagger_yaml/get_restaurantes_categoria.yaml')
def get_restaurantes_categoria(categoria):
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = "SELECT * FROM restaurante where categoria = %s"
        cursor.execute(query, (categoria,))
        restaurante = cursor.fetchall()
        if restaurante:
            return jsonify(restaurante), 200
        else:
            return jsonify({"message": "restaurante não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()


