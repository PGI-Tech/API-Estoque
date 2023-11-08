from app import *
from flask import Flask, jsonify, request
from config.db import *
from config.authenticate import *


@app.route('/permissao', methods=['GET'])
@jwt_required
def permissao(current_user):
    try:
        if request.method == 'GET':
            permissoes = db.query(Permissao).all()
            if (permissoes == None) or (len(permissoes) == 0):
                return jsonify({"error": "O ID informado não consta na tabela de Permissões!"})

            acessos = jsonify(permissoes_share_schema.dump(permissoes))
            if acessos == []:
                raise ValueError("Não há nenhum dado cadastrado nessa tabela")

            return acessos

    except Exception as e:
        return str(e), 500


@app.route('/permissao/<int:id>', methods=['GET'])
@jwt_required
def permissaoID(current_user, id):
    try:
        if request.method == 'GET':
            permissoes = db.query(Permissao).filter_by(id_permissao=id).first()
            if permissoes == None:
                return jsonify({"error": "O ID informado não consta na tabela de Permissões!"})

            acessos = jsonify(permissao_share_schema.dump(permissoes))
            if acessos == []:
                return jsonify({"error": "O ID informado não consta na tabela de Permissões!"})

            return acessos

    except Exception as e:
        return str(e), 500


@app.route('/permissao', methods=['POST'])
@jwt_required
def newPermissao(current_user):
    try:
        if request.method == 'POST':
            descricao = request.json['descricao']

            # Cria uma nova instância do modelo Usuario com os dados
            newAcesso = Permissao(
                descricao=descricao
            )

            db.add(newAcesso)
            db.commit()

            return jsonify({"message": "Nova permissão criada com sucesso!",
                            "permissao": permissao_share_schema.dump(db.query(Permissao).filter_by(descricao=descricao).first())})

    except Exception as e:
        return str(e), 500


@app.route('/permissao/<int:id>', methods=['PUT'])
@jwt_required
def editPermissao(current_user, id):
    try:
        if request.method == 'PUT':
            permissoes = db.query(Permissao).filter_by(id_permissao=id).first()
            if permissoes == None:
                return jsonify({"error": "O ID informado não consta na tabela de Permissões!"})

            acessos = jsonify(permissao_share_schema.dump(permissoes))
            if acessos == []:
                return jsonify({"error": "O ID informado não consta na tabela de Permissões!"})

            db.query(Permissao).filter_by(
                id_permissao=id).update(request.json)
            db.commit()

            return jsonify(permissao_share_schema.dump(db.query(Permissao).filter_by(id_permissao=id)))

    except Exception as e:
        return str(e), 500


@app.route('/permissao/<int:id>', methods=['DELETE'])
@jwt_required
def deletePermissao(current_user, id):
    try:
        if request.method == 'DELETE':
            permissoes = db.query(Permissao).filter_by(id_permissao=id).first()
            if permissoes == None:
                return jsonify({"error": "O ID informado não consta na tabela de Permissões!"})

            acessos = jsonify(permissao_share_schema.dump(permissoes))
            if acessos == []:
                return jsonify({"error": "O ID informado não consta na tabela de Permissões!"})

            db.query(Permissao).filter_by(id_permissao=id).delete()
            db.commit()

            return jsonify({"message": f"Permissão de ID {id} deletada com sucesso!"})

    except Exception as e:
        return str(e), 500
