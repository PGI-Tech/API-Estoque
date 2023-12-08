from app import app
from flask import Flask, jsonify, request
from config.db import *
from config.authenticate import *


@app.route('/classe', methods=['GET'])
@jwt_required
def classe(current_user):
    try:
        if request.method == 'GET':
            classes = db.query(Classe).all()
            if (classes == None) or (len(classes) == 0):
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            classe = jsonify(classes_share_schema.dump(classes))
            if classe == []:
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            return classe

    except Exception as e:
        return str(e), 500


@app.route('/classe/<int:id>', methods=['GET'])
@jwt_required
def classeID(current_user, id):
    try:
        if request.method == 'GET':
            classes = db.query(Classe).filter_by(id_classe=id).first()
            if classes == None:
                return jsonify({"error": "O ID informado não consta na tabela de classe!"})

            classe = jsonify(classe_share_schema.dump(classes))
            if classe == []:
                return jsonify({"error": "O ID informado não consta na tabela de classe!"})

            return classe

    except Exception as e:
        return str(e), 500


@app.route('/classe', methods=['POST'])
@jwt_required
def newClasse(current_user):
    try:
        if request.method == 'POST':
            classe = request.json['classe']

            # Cria uma nova instância do modelo classe com os dados
            newClasse = Classe(
                classe = classe
            )

            db.add(newClasse)
            db.commit()

            return jsonify({"message": "Nova classe criada com sucesso!",
                            "classe": classe_share_schema.dump(db.query(Classe).filter_by(classe = classe).first())})

    except Exception as e:
        return str(e), 500


@app.route('/classe/<int:id>', methods=['PUT'])
@jwt_required
def editClasse(current_user, id):
    try:
        if request.method == 'PUT':
            classes = db.query(Classe).filter_by(id_classe=id).first()
            if classes == None:
                return jsonify({"error": "O ID informado não consta na tabela de classe!"})

            classe = jsonify(classe_share_schema.dump(classes))
            if classe == []:
                return jsonify({"error": "O ID informado não consta na tabela de classe!"})

            db.query(Classe).filter_by(
                id_classe=id).update(request.json)
            db.commit()

            return jsonify(classe_share_schema.dump(db.query(Classe).filter_by(id_classe=id)))

    except Exception as e:
        return str(e), 500


@app.route('/classe/<int:id>', methods=['DELETE'])
@jwt_required
def deleteClasse(current_user, id):
    try:
        if request.method == 'DELETE':
            classes = db.query(Classe).filter_by(id_classe=id).first()
            if classes == None:
                return jsonify({"error": "O ID informado não consta na tabela de classe!"})

            classe = jsonify(classe_share_schema.dump(classes))
            if classe == []:
                return jsonify({"error": "O ID informado não consta na tabela de classe!"})

            db.query(Classe).filter_by(id_classe=id).delete()
            db.commit()

            return jsonify({"message": f"Classe de ID {id} deletada com sucesso!"})

    except Exception as e:
        return str(e), 500
