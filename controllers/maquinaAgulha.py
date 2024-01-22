from app import app
from flask import Flask, jsonify, request
from config.db import *
from config.authenticate import *


@app.route('/maquina_agulha', methods=['GET'])
@jwt_required
def MaquinaAgulha(current_user):
    try:
        if request.method == 'GET':
            maquina_agulhas = db.query(Maquina_Agulha).all()
            if (maquina_agulhas == None) or (len(maquina_agulhas) == 0):
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            maquina_agulha = jsonify(maquina_agulhas_share_schema.dump(maquina_agulhas))
            if maquina_agulha == []:
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            return maquina_agulha

    except Exception as e:
        return str(e), 500


@app.route('/maquina_agulha/<int:id>', methods=['GET'])
@jwt_required
def MaquinaAgulhaID(current_user, id):
    try:
        if request.method == 'GET':
            maquina_agulhas = db.query(Maquina_Agulha).filter_by(id_maquina_agulha=id).first()
            if maquina_agulhas == None:
                return jsonify({"error": "O ID informado não consta na tabela de maquina_agulha!"})

            maquina_agulha = jsonify(maquina_agulha_share_schema.dump(maquina_agulhas))
            if maquina_agulha == []:
                return jsonify({"error": "O ID informado não consta na tabela de maquina_agulha!"})

            return maquina_agulha

    except Exception as e:
        return str(e), 500


@app.route('/maquina_agulha', methods=['POST'])
@jwt_required
def NewMaquinaAgulha(current_user):
    try:
        if request.method == 'POST':
            maquina_agulha = request.json['maquina_agulha']

            # Cria uma nova instância do modelo maquina_agulha com os dados
            newmaquina_agulha = Maquina_Agulha(
                maquina = maquina_agulha
            )

            db.add(newmaquina_agulha)
            db.commit()

            return jsonify({"message": "Nova maquina_agulha criada com sucesso!",
                            "maquina_agulha": maquina_agulha_share_schema.dump(db.query(Maquina_Agulha).filter_by(maquina = maquina_agulha).first())})

    except Exception as e:
        return str(e), 500


@app.route('/maquina_agulha/<int:id>', methods=['PUT'])
@jwt_required
def editmaquina_agulha(current_user, id):
    try:
        if request.method == 'PUT':
            maquina_agulhas = db.query(Maquina_Agulha).filter_by(id_maquina_agulha=id).first()
            if maquina_agulhas == None:
                return jsonify({"error": "O ID informado não consta na tabela de maquina_agulha!"})

            maquina_agulha = jsonify(maquina_agulha_share_schema.dump(maquina_agulhas))
            if maquina_agulha == []:
                return jsonify({"error": "O ID informado não consta na tabela de maquina_agulha!"})

            db.query(maquina_agulha).filter_by(
                id_maquina_agulha=id).update(request.json)
            db.commit()

            return jsonify(maquina_agulha_share_schema.dump(db.query(maquina_agulha).filter_by(id_maquina_agulha=id)))

    except Exception as e:
        return str(e), 500


@app.route('/maquina_agulha/<int:id>', methods=['DELETE'])
@jwt_required
def deletemaquina_agulha(current_user, id):
    try:
        if request.method == 'DELETE':
            maquina_agulhas = db.query(Maquina_Agulha).filter_by(id_maquina_agulha=id).first()
            if maquina_agulhas == None:
                return jsonify({"error": "O ID informado não consta na tabela de maquina_agulha!"})

            maquina_agulha = jsonify(maquina_agulha_share_schema.dump(maquina_agulhas))
            if maquina_agulha == []:
                return jsonify({"error": "O ID informado não consta na tabela de maquina_agulha!"})

            db.query(Maquina_Agulha).filter_by(id_maquina_agulha=id).delete()
            db.commit()

            return jsonify({"message": f"maquina_agulha de ID {id} deletada com sucesso!"})

    except Exception as e:
        return str(e), 500
