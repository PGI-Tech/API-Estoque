from app import app
from flask import Flask, jsonify, request
from config.db import *
from config.authenticate import *


@app.route('/tipo_elastico', methods=['GET'])
@jwt_required
def TipoElastico(current_user):
    try:
        if request.method == 'GET':
            tipo_elasticos = db.query(Tipo_Elastico).all()
            if (tipo_elasticos == None) or (len(tipo_elasticos) == 0):
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            tipo_elastico = jsonify(tipo_elasticos_share_schema.dump(tipo_elasticos))
            if tipo_elastico == []:
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            return tipo_elastico

    except Exception as e:
        return str(e), 500


@app.route('/tipo_elastico/<int:id>', methods=['GET'])
@jwt_required
def TipoElasticoID(current_user, id):
    try:
        if request.method == 'GET':
            tipo_elasticos = db.query(Tipo_Elastico).filter_by(id_tipo_elastico=id).first()
            if tipo_elasticos == None:
                return jsonify({"error": "O ID informado não consta na tabela de tipo_elastico!"})

            tipo_elastico = jsonify(tipo_elastico_share_schema.dump(tipo_elasticos))
            if tipo_elastico == []:
                return jsonify({"error": "O ID informado não consta na tabela de tipo_elastico!"})

            return tipo_elastico

    except Exception as e:
        return str(e), 500


@app.route('/tipo_elastico', methods=['POST'])
@jwt_required
def NewTipoElastico(current_user):
    try:
        if request.method == 'POST':
            tipo_elastico = request.json['tipo_elastico']

            # Cria uma nova instância do modelo tipo_elastico com os dados
            newtipo_elastico = tipo_elastico(
                tipo_elastico = tipo_elastico
            )

            db.add(newtipo_elastico)
            db.commit()

            return jsonify({"message": "Nova tipo_elastico criada com sucesso!",
                            "tipo_elastico": tipo_elastico_share_schema.dump(db.query(Tipo_Elastico).filter_by(tipo_elastico = tipo_elastico).first())})

    except Exception as e:
        return str(e), 500


@app.route('/tipo_elastico/<int:id>', methods=['PUT'])
@jwt_required
def edittipo_elastico(current_user, id):
    try:
        if request.method == 'PUT':
            tipo_elasticos = db.query(Tipo_Elastico).filter_by(id_tipo_elastico=id).first()
            if tipo_elasticos == None:
                return jsonify({"error": "O ID informado não consta na tabela de tipo_elastico!"})

            tipo_elastico = jsonify(tipo_elastico_share_schema.dump(tipo_elasticos))
            if tipo_elastico == []:
                return jsonify({"error": "O ID informado não consta na tabela de tipo_elastico!"})

            db.query(tipo_elastico).filter_by(
                id_tipo_elastico=id).update(request.json)
            db.commit()

            return jsonify(tipo_elastico_share_schema.dump(db.query(tipo_elastico).filter_by(id_tipo_elastico=id)))

    except Exception as e:
        return str(e), 500


@app.route('/tipo_elastico/<int:id>', methods=['DELETE'])
@jwt_required
def deletetipo_elastico(current_user, id):
    try:
        if request.method == 'DELETE':
            tipo_elasticos = db.query(Tipo_Elastico).filter_by(id_tipo_elastico=id).first()
            if tipo_elasticos == None:
                return jsonify({"error": "O ID informado não consta na tabela de tipo_elastico!"})

            tipo_elastico = jsonify(tipo_elastico_share_schema.dump(tipo_elasticos))
            if tipo_elastico == []:
                return jsonify({"error": "O ID informado não consta na tabela de tipo_elastico!"})

            db.query(Tipo_Elastico).filter_by(id_tipo_elastico=id).delete()
            db.commit()

            return jsonify({"message": f"tipo_elastico de ID {id} deletada com sucesso!"})

    except Exception as e:
        return str(e), 500
