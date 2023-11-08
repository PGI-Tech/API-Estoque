from functools import wraps
import jwt
from flask import request, jsonify, current_app
from app import *
from config.db import *

def jwt_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None
        # verificamos se há um header chamado "authorization" e salvamos o seu valor
        if 'authorization' in request.headers:
            token = request.headers['authorization']

        # se o valor da pego anteriormente foi vazio ou nulo, retorna erro
        if not token:
            return jsonify({
                "error":"Você não tem permissão para acessar essa rota!"
            }), 403
        
        # se não houver o titulo "Bearer" no token, também retorna erro
        if not 'Bearer' in token:
            return jsonify({
                "error":"Token inválido!"
            }), 401

        try:
            token_pure = token.replace('Bearer ', '') # token sem o titulo "Bearer"
            decoded = jwt.decode(token_pure, current_app.config['SECRET_KEY'], algorithms=["HS256"]) # decodificamos o token com a chave secreta
            user = db.query(Usuario).filter_by(id_usuario=int(decoded['id'])).first() # pegamos o ID do Usuario logado no payload do token
            #permissao = db.query(Permissao).filter_by(id_permissao=int(decoded['level'])).first()
            current_user = jsonify(user_share_schema.dump(user))
            #current_level = jsonify(permissao_share_schema.dump(permissao))
        except Exception as e:
            return jsonify({
                "error":"Token inválido!"
            })
        # retornamos o usuario logado
        return f(current_user=current_user, *args, **kwargs)
    return wrapper