from app import app
from flask import Flask, jsonify, request
from config.db import *
from config.authenticate import *


@app.route('/categoria', methods=['GET'])
@jwt_required
def categoria(current_user):
    try:
        if request.method == 'GET':
            categorias = db.query(Categoria).all()
            if (categorias == None) or (len(categorias) == 0):
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            categoria = jsonify(categorias_share_schema.dump(categorias))
            if categoria == []:
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            return categoria

    except Exception as e:
        return str(e), 500


@app.route('/categoria/<int:id>', methods=['GET'])
@jwt_required
def categoriaID(current_user, id):
    try:
        if request.method == 'GET':
            categorias = db.query(Categoria).filter_by(id_categoria=id).first()
            if categorias == None:
                return jsonify({"error": "O ID informado não consta na tabela de Categoria!"})

            categoria = jsonify(categoria_share_schema.dump(categorias))
            if categoria == []:
                return jsonify({"error": "O ID informado não consta na tabela de Categoria!"})

            return categoria

    except Exception as e:
        return str(e), 500


@app.route('/categoria', methods=['POST'])
@jwt_required
def newCategoria(current_user):
    try:
        if request.method == 'POST':
            categoria = request.json['categoria']

            # Cria uma nova instância do modelo Categoria com os dados
            newCategoria = Categoria(
                categoria = categoria
            )

            db.add(newCategoria)
            db.commit()

            return jsonify({"message": "Nova categoria criada com sucesso!",
                            "categoria": categoria_share_schema.dump(db.query(Categoria).filter_by(categoria = categoria).first())})

    except Exception as e:
        return str(e), 500


@app.route('/categoria/<int:id>', methods=['PUT'])
@jwt_required
def editCategoria(current_user, id):
    try:
        if request.method == 'PUT':
            categorias = db.query(Categoria).filter_by(id_categoria=id).first()
            if categorias == None:
                return jsonify({"error": "O ID informado não consta na tabela de categoria!"})

            categoria = jsonify(categoria_share_schema.dump(categorias))
            if categoria == []:
                return jsonify({"error": "O ID informado não consta na tabela de categoria!"})

            db.query(Categoria).filter_by(
                id_categoria=id).update(request.json)
            db.commit()

            return jsonify(categoria_share_schema.dump(db.query(Categoria).filter_by(id_categoria=id)))

    except Exception as e:
        return str(e), 500


@app.route('/categoria/<int:id>', methods=['DELETE'])
@jwt_required
def deleteCategoria(current_user, id):
    try:
        if request.method == 'DELETE':
            categorias = db.query(Categoria).filter_by(id_categoria=id).first()
            if categorias == None:
                return jsonify({"error": "O ID informado não consta na tabela de Categoria!"})

            categoria = jsonify(categoria_share_schema.dump(categorias))
            if categoria == []:
                return jsonify({"error": "O ID informado não consta na tabela de Categoria!"})

            db.query(Categoria).filter_by(id_categoria=id).delete()
            db.commit()

            return jsonify({"message": f"Categoria de ID {id} deletada com sucesso!"})

    except Exception as e:
        return str(e), 500
