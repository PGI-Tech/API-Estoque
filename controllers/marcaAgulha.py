from app import app
from flask import Flask, jsonify, request
from config.db import *
from config.authenticate import *


@app.route('/marca_agulha', methods=['GET'])
@jwt_required
def MarcaAgulha(current_user):
    try:
        if request.method == 'GET':
            marca_agulhas = db.query(Marca_Agulha).all()
            if (marca_agulhas == None) or (len(marca_agulhas) == 0):
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            marca_agulha = jsonify(marca_agulhas_share_schema.dump(marca_agulhas))
            if marca_agulha == []:
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            return marca_agulha

    except Exception as e:
        return str(e), 500


@app.route('/marca_agulha/<int:id>', methods=['GET'])
@jwt_required
def MarcaAgulhaID(current_user, id):
    try:
        if request.method == 'GET':
            marca_agulhas = db.query(Marca_Agulha).filter_by(id_marca_agulha=id).first()
            if marca_agulhas == None:
                return jsonify({"error": "O ID informado não consta na tabela de marca de agulha!"})

            marca_agulha = jsonify(marca_agulha_share_schema.dump(marca_agulhas))
            if marca_agulha == []:
                return jsonify({"error": "O ID informado não consta na tabela de marca de agulha!"})

            return marca_agulha

    except Exception as e:
        return str(e), 500


@app.route('/marca_agulha', methods=['POST'])
@jwt_required
def NewMarcaAgulha(current_user):
    try:
        if request.method == 'POST':
            marca_agulha = request.json['marca_agulha']

            # Cria uma nova instância do modelo maquina_agulha com os dados
            newmarca_agulha = marca_agulha(
                marca_agulha = marca_agulha
            )

            db.add(newmarca_agulha)
            db.commit()

            return jsonify({"message": "Nova marca de agulha criada com sucesso!",
                            "marca_agulha": marca_agulha_share_schema.dump(db.query(Marca_Agulha).filter_by(marca_agulha = marca_agulha).first())})

    except Exception as e:
        return str(e), 500


@app.route('/marca_agulha/<int:id>', methods=['PUT'])
@jwt_required
def editmarca_agulha(current_user, id):
    try:
        if request.method == 'PUT':
            marca_agulhas = db.query(Marca_Agulha).filter_by(id_marca_agulha=id).first()
            if marca_agulhas == None:
                return jsonify({"error": "O ID informado não consta na tabela de marca_agulhas!"})

            marca_agulha = jsonify(marca_agulha_share_schema.dump(marca_agulhas))
            if marca_agulha == []:
                return jsonify({"error": "O ID informado não consta na tabela de marca_agulhas!"})

            db.query(marca_agulha).filter_by(
                id_marca_agulha=id).update(request.json)
            db.commit()

            return jsonify(marca_agulha_share_schema.dump(db.query(marca_agulha).filter_by(id_marca_agulha=id)))

    except Exception as e:
        return str(e), 500


@app.route('/marca_agulha/<int:id>', methods=['DELETE'])
@jwt_required
def deletemarca_agulha(current_user, id):
    try:
        if request.method == 'DELETE':
            marca_agulhas = db.query(Marca_Agulha).filter_by(id_marca_agulha=id).first()
            if marca_agulhas == None:
                return jsonify({"error": "O ID informado não consta na tabela de marca_agulha!"})

            marca_agulha = jsonify(marca_agulha_share_schema.dump(marca_agulhas))
            if marca_agulha == []:
                return jsonify({"error": "O ID informado não consta na tabela de marca_agulhas!"})

            db.query(Marca_Agulha).filter_by(id_marca_agulha=id).delete()
            db.commit()

            return jsonify({"message": f"marca_agulha de ID {id} deletada com sucesso!"})

    except Exception as e:
        return str(e), 500
