from app import app
from flask import Flask, jsonify, request
from config.db import *
from config.authenticate import *


@app.route('/tipo_linha', methods=['GET'])
@jwt_required
def TipoLinha(current_user):
    try:
        if request.method == 'GET':
            tipo_linhas = db.query(Tipo_Linha).all()
            if (tipo_linhas == None) or (len(tipo_linhas) == 0):
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            tipo_linha = jsonify(tipo_linhas_share_schema.dump(tipo_linhas))
            if tipo_linha == []:
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            return tipo_linha

    except Exception as e:
        return str(e), 500


@app.route('/tipo_linha/<int:id>', methods=['GET'])
@jwt_required
def TipoLinhaID(current_user, id):
    try:
        if request.method == 'GET':
            tipo_linhas = db.query(Tipo_Linha).filter_by(id_tipo_linha=id).first()
            if tipo_linhas == None:
                return jsonify({"error": "O ID informado não consta na tabela de tipo_linha!"})

            tipo_linha = jsonify(tipo_linha_share_schema.dump(tipo_linhas))
            if tipo_linha == []:
                return jsonify({"error": "O ID informado não consta na tabela de tipo_linha!"})

            return tipo_linha

    except Exception as e:
        return str(e), 500


@app.route('/tipo_linha', methods=['POST'])
@jwt_required
def NewTipoLinha(current_user):
    try:
        if request.method == 'POST':
            tipo_linha = request.json['tipo_linha']

            # Cria uma nova instância do modelo tipo_linha com os dados
            newtipo_linha = tipo_linha(
                tipo_linha = tipo_linha
            )

            db.add(newtipo_linha)
            db.commit()

            return jsonify({"message": "Nova tipo_linha criada com sucesso!",
                            "tipo_linha": tipo_linha_share_schema.dump(db.query(Tipo_Linha).filter_by(tipo_linha = tipo_linha).first())})

    except Exception as e:
        return str(e), 500


@app.route('/tipo_linha/<int:id>', methods=['PUT'])
@jwt_required
def edittipo_linha(current_user, id):
    try:
        if request.method == 'PUT':
            tipo_linhas = db.query(Tipo_Linha).filter_by(id_tipo_linha=id).first()
            if tipo_linhas == None:
                return jsonify({"error": "O ID informado não consta na tabela de tipo_linha!"})

            tipo_linha = jsonify(tipo_linha_share_schema.dump(tipo_linhas))
            if tipo_linha == []:
                return jsonify({"error": "O ID informado não consta na tabela de tipo_linha!"})

            db.query(tipo_linha).filter_by(
                id_tipo_linha=id).update(request.json)
            db.commit()

            return jsonify(tipo_linha_share_schema.dump(db.query(tipo_linha).filter_by(id_tipo_linha=id)))

    except Exception as e:
        return str(e), 500


@app.route('/tipo_linha/<int:id>', methods=['DELETE'])
@jwt_required
def deletetipo_linha(current_user, id):
    try:
        if request.method == 'DELETE':
            tipo_linhas = db.query(Tipo_Linha).filter_by(id_tipo_linha=id).first()
            if tipo_linhas == None:
                return jsonify({"error": "O ID informado não consta na tabela de tipo_linha!"})

            tipo_linha = jsonify(tipo_linha_share_schema.dump(tipo_linhas))
            if tipo_linha == []:
                return jsonify({"error": "O ID informado não consta na tabela de tipo_linha!"})

            db.query(Tipo_Linha).filter_by(id_tipo_linha=id).delete()
            db.commit()

            return jsonify({"message": f"tipo_linha de ID {id} deletada com sucesso!"})

    except Exception as e:
        return str(e), 500
