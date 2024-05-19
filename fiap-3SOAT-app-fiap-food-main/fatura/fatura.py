from flask import Blueprint, jsonify,request
import sys
from db import db_mysql_class
from datetime import datetime
from flasgger import swag_from


fatura_bp = Blueprint('fatura', __name__)



def check(list):
    check = all(i == list[0] for i in list)
    if check:
        return list[0],check
    return 'Erro', check 



# Rota para criar uma nova fatura
@fatura_bp.route('/fatura/cria_fatura', methods=['POST'])
@swag_from('../swagger_yaml/create_fatura.yaml')
def create_fatura():
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor()
    current_datetime = datetime.now()

    try:
        data = request.json
        query = "INSERT INTO fatura (id_pedido, id_cliente, valor, status, data_fatura) VALUES (%s, %s, %s, %s, %s)"
        values = (data['id_pedido'], data.get('id_cliente'), data.get('valor'), data.get('status'),current_datetime)
        cursor.execute(query, values)
        conn.commit()
        return jsonify({"message": "Fatura criado com sucesso"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()




# Rota para recuperar a fatura
@fatura_bp.route('/fatura/consulta_fatura/<int:id>', methods=['GET'])
@swag_from('../swagger_yaml/get_fatura.yaml')
def get_fatura(id):
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = "SELECT * FROM fatura WHERE id_fatura = %s"
        cursor.execute(query, (id,))
        fatura = cursor.fetchone()
        if fatura:
            return jsonify(fatura), 200
        else:
            return jsonify({"message": "fatura não encontrada"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()






# Rota para atualizar um fatura pelo ID
@fatura_bp.route('/fatura/atualiza_fatura/<int:id>', methods=['PUT'])
@swag_from('../swagger_yaml/update_fatura_status.yaml')
def update_fatura_status(id):
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor()
    try:
        data = request.json
        query = "UPDATE fatura SET status = %s  WHERE id_fatura = %s"
        values = (data.get('status'), id)
        cursor.execute(query, values)
        conn.commit()
        return jsonify({"message": "Fatura atualizada com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()


@fatura_bp.route('/fatura/atualiza_fatura_pago/<int:id>', methods=['PUT'])
@swag_from('../swagger_yaml/update_fatura_status_pago.yaml')
def update_fatura_status_pago(id):
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor()
    try:
        # data = request.json
        query = "UPDATE fatura SET status = 2  WHERE id_fatura = %s"
        values = (id,)
        cursor.execute(query, values)
        conn.commit()
        return jsonify({"message": "Fatura atualizada com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()




@fatura_bp.route('/fatura/atualiza_fatura_nao_pago/<int:id>', methods=['PUT'])
@swag_from('../swagger_yaml/update_fatura_status_nao_pago.yaml')
def update_fatura_status_nao_pago(id):
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor()
    try:
        # data = request.json
        query = "UPDATE fatura SET status = 1 WHERE id_fatura = %s"
        values = (id,)
        cursor.execute(query, values)
        conn.commit()
        return jsonify({"message": "Fatura atualizada com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()



@fatura_bp.route('/fatura/atualiza_fatura_cancelado/<int:id>', methods=['PUT'])
@swag_from('../swagger_yaml/update_fatura_status_cancelado.yaml')
def update_fatura_status_cancelado(id):
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor()
    try:
        # data = request.json
        query = "UPDATE fatura SET status = 3  WHERE id_fatura = %s"
        values = (id,)
        cursor.execute(query, values)
        conn.commit()
        return jsonify({"message": "Fatura cancelada com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()







# # Rota para excluir um entregador pelo ID
# @fatura_bp.route('/fatura/deleta_entregador/<int:id>', methods=['DELETE'])
# def delete_fatura(id):
#     db_objt = db_mysql_class()
#     conn = db_objt.get_db_connection()
#     cursor = conn.cursor()
#     try:
#         query = "DELETE FROM entregador WHERE id_entregador = %s"
#         cursor.execute(query, (id,))
#         conn.commit()
#         return jsonify({"message": "Entregador excluído com sucesso"}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400
#     finally:
#         cursor.close()
#         conn.close()










# Rota para recuperar todx consulta_all_fatura
@fatura_bp.route('/fatura/consulta_all/', methods=['GET'])
@swag_from('../swagger_yaml/get_entregador_all.yaml')
def consulta_all_fatura():
    db_objt = db_mysql_class()
    conn = db_objt.get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = "SELECT * FROM fatura"
        cursor.execute(query)
        fatura = cursor.fetchall()
        if fatura:
            return jsonify(fatura), 200
        else:
            return jsonify({"message": "fatura não encontrada"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()


