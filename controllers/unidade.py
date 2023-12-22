from app import app
from flask import Flask, jsonify, request
from config.db import *
from config.authenticate import *


@app.route('/unidade', methods=['GET'])
@jwt_required
def unidade(current_user):
    try:
        if request.method == 'GET':
            unidades = db.query(Unidade).all()
            if (unidades == None) or (len(unidades) == 0):
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            unidade = jsonify(unidades_share_schema.dump(unidades))
            if unidade == []:
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            return unidade

    except Exception as e:
        return str(e), 500


@app.route('/unidade/<int:id>', methods=['GET'])
@jwt_required
def unidadeID(current_user, id):
    try:
        if request.method == 'GET':
            unidades = db.query(Unidade).filter_by(id_unidade=id).first()
            if unidades == None:
                return jsonify({"error": "O ID informado não consta na tabela de unidade!"})

            unidade = jsonify(unidade_share_schema.dump(unidades))
            if unidade == []:
                return jsonify({"error": "O ID informado não consta na tabela de unidade!"})

            return unidade

    except Exception as e:
        return str(e), 500


@app.route('/unidade', methods=['POST'])
@jwt_required
def newUnidade(current_user):
    try:
        if request.method == 'POST':
            unidade = request.json['unidade']

            # Cria uma nova instância do modelo unidade com os dados
            newUnidade = Unidade(
                unidade = unidade
            )

            db.add(newUnidade)
            db.commit()

            return jsonify({"message": "Nova unidade criada com sucesso!",
                            "unidade": unidade_share_schema.dump(db.query(Unidade).filter_by(unidade = unidade).first())})

    except Exception as e:
        return str(e), 500


@app.route('/unidade/<int:id>', methods=['PUT'])
@jwt_required
def editUnidade(current_user, id):
    try:
        if request.method == 'PUT':
            unidades = db.query(Unidade).filter_by(id_unidade=id).first()
            if unidades == None:
                return jsonify({"error": "O ID informado não consta na tabela de unidade!"})

            unidade = jsonify(unidade_share_schema.dump(unidades))
            if unidade == []:
                return jsonify({"error": "O ID informado não consta na tabela de unidade!"})

            db.query(Unidade).filter_by(
                id_unidade=id).update(request.json)
            db.commit()

            return jsonify(unidade_share_schema.dump(db.query(Unidade).filter_by(id_unidade=id)))

    except Exception as e:
        return str(e), 500


@app.route('/unidade/<int:id>', methods=['DELETE'])
@jwt_required
def deleteUnidade(current_user, id):
    try:
        if request.method == 'DELETE':
            unidades = db.query(Unidade).filter_by(id_unidade=id).first()
            if unidades == None:
                return jsonify({"error": "O ID informado não consta na tabela de unidade!"})

            unidade = jsonify(unidade_share_schema.dump(unidades))
            if unidade == []:
                return jsonify({"error": "O ID informado não consta na tabela de unidade!"})

            db.query(Unidade).filter_by(id_unidade=id).delete()
            db.commit()

            return jsonify({"message": f"Unidade de ID {id} deletada com sucesso!"})

    except Exception as e:
        return str(e), 500
