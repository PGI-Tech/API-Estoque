from flask_cors import cross_origin
from app import app
from flask import Flask, jsonify, request
from config.db import *
import datetime
import jwt

@app.route('/auth', methods=['POST'])
#@cross_origin()
def auth():
    # capturar o username inserido pelo usuário
    username = request.json['username']
    senha = request.json['senha']
    user = db.query(Usuario).filter_by(username=username).first()
    # buscamos no banco de dados se existe um usuário cadastrado com o username inserido
    if user == None:
        return jsonify({
            "error": "Suas credênciais estão erradas!"
        }), 403

    # se a senha do usuário não estiver correta, retorna erro
    if not user.verify_password(senha):
        return jsonify({
            "error": "Sua senha está incorreta!"
        }), 403
    
    level_permission = db.query(Permissao).filter_by(id_permissao=user.id_permissao).first()

    payload = {  # dados que serão trafegados via token
        "id": user.id_usuario,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    }

    # para gerar o token, passamos o payload e a chave secreta
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({"token": token,
                    "level": level_permission.descricao})

