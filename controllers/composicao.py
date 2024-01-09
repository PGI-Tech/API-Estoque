from app import app
from flask import Flask, jsonify, request
from config.db import *
from config.authenticate import *

@app.route('/composicao', methods=['GET'])
@jwt_required
def composicao(current_user):
    try:
        if request.method == 'GET':
            composicoes = db.query(Composicao).all()
            if (composicoes == None) or (len(composicoes) == 0):
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            composicao = jsonify(composicoes_share_schema.dump(composicoes))
            if composicao == []:
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            return composicao

    except Exception as e:
        return str(e), 500


@app.route('/composicao/<int:id>', methods=['GET'])
@jwt_required
def composicaoID(current_user, id):
    try:
        if request.method == 'GET':
            composicoes = db.query(Composicao).filter_by(id_composicao=id).first()
            if composicoes == None:
                return jsonify({"error": "O ID informado não consta na tabela de composicao!"})

            composicao = jsonify(composicoes_share_schema.dump(composicoes))
            if composicao == []:
                return jsonify({"error": "O ID informado não consta na tabela de composicao!"})

            return composicao

    except Exception as e:
        return str(e), 500


@app.route('/composicao', methods=['POST'])
@jwt_required
def newComposicao(current_user):
    try:
        if request.method == 'POST':
            composicao = request.json['composicao']

            # Cria uma nova instância do modelo composicao com os dados
            newcomposicao = composicao(
                composicao = composicao
            )

            db.add(newcomposicao)
            db.commit()

            return jsonify({"message": "Nova composicao criada com sucesso!",
                            "composicao": composicao_share_schema.dump(db.query(Composicao).filter_by(composicao = composicao).first())})

    except Exception as e:
        return str(e), 500


@app.route('/composicao/<int:id>', methods=['PUT'])
@jwt_required
def editcomposicao(current_user, id):
    try:
        if request.method == 'PUT':
            composicoes = db.query(Composicao).filter_by(id_composicao=id).first()
            if composicoes == None:
                return jsonify({"error": "O ID informado não consta na tabela de composicao!"})

            composicao = jsonify(composicao_share_schema.dump(composicoes))
            if composicao == []:
                return jsonify({"error": "O ID informado não consta na tabela de composicao!"})

            db.query(composicao).filter_by(
                id_composicao=id).update(request.json)
            db.commit()

            return jsonify(composicao_share_schema.dump(db.query(composicao).filter_by(id_composicao=id)))

    except Exception as e:
        return str(e), 500


@app.route('/composicao/<int:id>', methods=['DELETE'])
@jwt_required
def deleteComposicao(current_user, id):
    try:
        if request.method == 'DELETE':
            composicoes = db.query(Composicao).filter_by(id_composicao=id).first()
            if composicoes == None:
                return jsonify({"error": "O ID informado não consta na tabela de composicao!"})

            composicao = jsonify(composicao_share_schema.dump(composicoes))
            if composicao == []:
                return jsonify({"error": "O ID informado não consta na tabela de composicao!"})

            db.query(Composicao).filter_by(id_composicao=id).delete()
            db.commit()

            return jsonify({"message": f"composicao de ID {id} deletada com sucesso!"})

    except Exception as e:
        return str(e), 500
