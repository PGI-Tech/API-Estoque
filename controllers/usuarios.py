from app import app
from flask import jsonify, request
from config.authenticate import *
from config.db import *
import math

@app.route('/usuarios', methods=['GET'])
@jwt_required
def usuarios(current_user):
    try:
        if request.method == 'GET':
            usuarios = db.query(Usuario).all()
            if (usuarios == None) or (len(usuarios) == 0):
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            users = jsonify(users_share_schema.dump(usuarios))
            if users == []:
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})
    
            return users
    
    except Exception as e:
        return str(e), 500
    

@app.route('/usuarios/<int:id>', methods=['GET'])
@jwt_required
def usuarioID(current_user, id):
    try:
        if request.method == 'GET':
            usuarios = db.query(Usuario).filter_by(id_usuario=id).first()
            if usuarios == None:
                return jsonify({"error":"O ID informado não consta na tabela de Usuarios!"})
            
            users = jsonify(user_share_schema.dump(usuarios))
            if users == []:
                return jsonify({"error":"O ID informado não consta na tabela de Usuarios!"})
            
            return users

    except Exception as e:
        return str(e), 500


@app.route('/usuarios/<int:itens>/<int:page>', methods=['GET'])
@jwt_required
def usuarioPagination(current_user, itens, page):
    try:
        if request.method == 'GET':
            skip = (page - 1) * itens
            totalUsers = db.query(Usuario).count()
            usuarios = db.query(Usuario).limit(itens).offset(skip).all()
            if (usuarios == None) or (len(usuarios) == 0):
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            users = users_share_schema.dump(usuarios)
            if users == []:
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})
    
            return jsonify({
                    "totalUsers":totalUsers,
                    "itens":itens,
                    "totalPages": math.ceil(totalUsers/itens),
                    "data": users})
    
    except Exception as e:
        return str(e), 500


@app.route('/usuarios', methods=['POST'])
#@jwt_required
def newUsuario():
    try: 
        if request.method == 'POST':
            username = request.json['username']
            senha = request.json['senha']
            id_permissao = request.json['id_permissao']

            # Cria uma nova instância do modelo Usuario com os dados
            newUser = Usuario(
                username = username,
                senha = senha,
                id_permissao = id_permissao
            )

            db.add(newUser)
            db.commit()

            return jsonify({"message": "Novo usuário criado com sucesso!",
                            "usuario": user_share_schema.dump(db.query(Usuario).filter_by(username=username).first())})

    except Exception as e:
        if 'violates foreign key constraint "usuario_id_permissao_fkey"' in str(e):
            return jsonify({"error":"O ID da Permissão informado não consta na tabela de Permissão!"})
        return str(e), 500
        

@app.route('/usuarios/<int:id>', methods=['PUT'])
@jwt_required
def editUsuario(current_user, id):
    try:
       if request.method == 'PUT':
            usuarios = db.query(Usuario).filter_by(id_usuario=id).first()
            if usuarios == None:
                return jsonify({"error":"O ID informado não consta na tabela de Usuarios!"})

            # Obtenha os dados JSON da solicitação
            data = request.json

            if 'username' in data:
                usuarios.username = data['username']
            if 'senha' in data:
                usuarios.senha = generate_password_hash(data['senha'])
            if 'id_permissao' in data:
                usuarios.id_permissao = data['id_permissao']

            db.commit()

            return jsonify(user_share_schema.dump(db.query(Usuario).filter_by(id_usuario=id).first()))

    except Exception as e:
        return str(e), 500


@app.route('/usuarios/<int:id>', methods=['DELETE'])
@jwt_required
def deleteUsuario(current_user, id):
    try:
        if request.method == 'DELETE':
            usuarios = db.query(Usuario).filter_by(id_usuario=id).first()
            if usuarios == None:
                return jsonify({"error":"O ID informado não consta na tabela de Usuarios!"})

            users = jsonify(user_share_schema.dump(usuarios))
            if users == []:
                return jsonify({"error":"O ID informado não consta na tabela de Usuarios!"})

            db.query(Usuario).filter_by(id_usuario=id).delete()
            db.commit()

            return jsonify({"message": f"Usuario de ID {id} deletado com sucesso!"})

    except Exception as e:
        return str(e), 500