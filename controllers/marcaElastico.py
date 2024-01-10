from app import app
from flask import Flask, jsonify, request
from config.db import *
from config.authenticate import *


@app.route('/marca_elastico', methods=['GET'])
@jwt_required
def MaquinaElastico(current_user):
    try:
        if request.method == 'GET':
            marca_elasticos = db.query(Marca_Elastico).all()
            if (marca_elasticos == None) or (len(marca_elasticos) == 0):
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            marca_elastico = jsonify(marca_elasticos_share_schema.dump(marca_elasticos))
            if marca_elastico == []:
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            return marca_elastico

    except Exception as e:
        return str(e), 500


@app.route('/marca_elastico/<int:id>', methods=['GET'])
@jwt_required
def MarcaElasticoID(current_user, id):
    try:
        if request.method == 'GET':
            marca_elasticos = db.query(Marca_Elastico).filter_by(id_marca_elastico=id).first()
            if marca_elasticos == None:
                return jsonify({"error": "O ID informado não consta na tabela de marca de elastico!"})

            marca_elastico = jsonify(marca_elastico_share_schema.dump(marca_elasticos))
            if marca_elastico == []:
                return jsonify({"error": "O ID informado não consta na tabela de marca de elastico!"})

            return marca_elastico

    except Exception as e:
        return str(e), 500


@app.route('/marca_elastico', methods=['POST'])
@jwt_required
def NewMarcaElastico(current_user):
    try:
        if request.method == 'POST':
            marca_elastico = request.json['marca_elastico']

            # Cria uma nova instância do modelo maquina_agulha com os dados
            newmarca_elastico = marca_elastico(
                marca_elastico = marca_elastico
            )

            db.add(newmarca_elastico)
            db.commit()

            return jsonify({"message": "Nova marca de elastico criada com sucesso!",
                            "marca_elastico": marca_elastico_share_schema.dump(db.query(Marca_Elastico).filter_by(marca_elastico = marca_elastico).first())})

    except Exception as e:
        return str(e), 500


@app.route('/marca_elastico/<int:id>', methods=['PUT'])
@jwt_required
def editmarca_elastico(current_user, id):
    try:
        if request.method == 'PUT':
            marca_elasticos = db.query(Marca_Elastico).filter_by(id_marca_elastico=id).first()
            if marca_elasticos == None:
                return jsonify({"error": "O ID informado não consta na tabela de maquina_elastico!"})

            marca_elastico = jsonify(marca_elastico_share_schema.dump(marca_elasticos))
            if marca_elastico == []:
                return jsonify({"error": "O ID informado não consta na tabela de marca_elastico!"})

            db.query(marca_elastico).filter_by(
                id_marca_elasticoa=id).update(request.json)
            db.commit()

            return jsonify(marca_elastico_share_schema.dump(db.query(marca_elastico).filter_by(id_marca_elastico=id)))

    except Exception as e:
        return str(e), 500


@app.route('/marca_elastico/<int:id>', methods=['DELETE'])
@jwt_required
def deletemarca_elastico(current_user, id):
    try:
        if request.method == 'DELETE':
            marca_elasticos = db.query(Marca_Elastico).filter_by(id_marca_elastico=id).first()
            if marca_elasticos == None:
                return jsonify({"error": "O ID informado não consta na tabela de marca_elastico!"})

            marca_elastico = jsonify(marca_elastico_share_schema.dump(marca_elasticos))
            if marca_elastico == []:
                return jsonify({"error": "O ID informado não consta na tabela de marca_elastico!"})

            db.query(Marca_Elastico).filter_by(id_marca_elastico=id).delete()
            db.commit()

            return jsonify({"message": f"marca_elastico de ID {id} deletada com sucesso!"})

    except Exception as e:
        return str(e), 500
