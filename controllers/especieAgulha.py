from app import app
from flask import Flask, jsonify, request
from config.db import *
from config.authenticate import *


@app.route('/especie_agulha', methods=['GET'])
@jwt_required
def EspecieAgulha(current_user):
    try:
        if request.method == 'GET':
            especie_agulhas = db.query(Especie_Agulha).all()
            if (especie_agulhas == None) or (len(especie_agulhas) == 0):
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            especie_agulha = jsonify(especie_agulhas_share_schema.dump(especie_agulhas))
            if especie_agulha == []:
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            return especie_agulha

    except Exception as e:
        return str(e), 500


@app.route('/especie_agulha/<int:id>', methods=['GET'])
@jwt_required
def EspecieAgulhaID(current_user, id):
    try:
        if request.method == 'GET':
            especie_agulhas = db.query(Especie_Agulha).filter_by(id_especie_agulha=id).first()
            if especie_agulhas == None:
                return jsonify({"error": "O ID informado não consta na tabela de especie_agulha!"})

            especie_agulha = jsonify(especie_agulha_share_schema.dump(especie_agulhas))
            if especie_agulha == []:
                return jsonify({"error": "O ID informado não consta na tabela de especie_agulha!"})

            return especie_agulha

    except Exception as e:
        return str(e), 500


@app.route('/especie_agulha', methods=['POST'])
@jwt_required
def NewEspecieAgulha(current_user):
    try:
        if request.method == 'POST':
            especie_agulha = request.json['especie_agulha']

            # Cria uma nova instância do modelo especie_agulha com os dados
            newespecie_agulha = Especie_Agulha(
                especie = especie_agulha
            )

            db.add(newespecie_agulha)
            db.commit()

            return jsonify({"message": "Nova especie_agulha criada com sucesso!",
                            "especie_agulha": especie_agulha_share_schema.dump(db.query(Especie_Agulha).filter_by(especie = especie_agulha).first())})

    except Exception as e:
        return str(e), 500


@app.route('/especie_agulha/<int:id>', methods=['PUT'])
@jwt_required
def editespecie_agulha(current_user, id):
    try:
        if request.method == 'PUT':
            especie_agulhas = db.query(Especie_Agulha).filter_by(id_especie_agulha=id).first()
            if especie_agulhas == None:
                return jsonify({"error": "O ID informado não consta na tabela de especie_agulha!"})

            especie_agulha = jsonify(especie_agulha_share_schema.dump(especie_agulhas))
            if especie_agulha == []:
                return jsonify({"error": "O ID informado não consta na tabela de especie_agulha!"})

            db.query(especie_agulha).filter_by(
                id_especie_agulha=id).update(request.json)
            db.commit()

            return jsonify(especie_agulha_share_schema.dump(db.query(especie_agulha).filter_by(id_especie_agulha=id)))

    except Exception as e:
        return str(e), 500


@app.route('/especie_agulha/<int:id>', methods=['DELETE'])
@jwt_required
def deleteespecie_agulha(current_user, id):
    try:
        if request.method == 'DELETE':
            especie_agulhas = db.query(Especie_Agulha).filter_by(id_especie_agulha=id).first()
            if especie_agulhas == None:
                return jsonify({"error": "O ID informado não consta na tabela de especie_agulha!"})

            especie_agulha = jsonify(especie_agulha_share_schema.dump(especie_agulhas))
            if especie_agulha == []:
                return jsonify({"error": "O ID informado não consta na tabela de especie_agulha!"})

            db.query(Especie_Agulha).filter_by(id_especie_agulha=id).delete()
            db.commit()

            return jsonify({"message": f"especie_agulha de ID {id} deletada com sucesso!"})

    except Exception as e:
        return str(e), 500
