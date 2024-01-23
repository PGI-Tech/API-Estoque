import os
from app import app
from flask import Flask, jsonify, request, url_for, redirect
from config.authenticate import jwt_required
from config.db import *
from config.authenticate import *
import qrcode
import socket
import base64
from PIL import Image

@app.route('/produtos', methods=['GET'])
@jwt_required
def produto(current_user):
    try:
        if request.method == 'GET':
            agulhas = db.query(Agulha).all()
            if (agulhas == None) or (len(agulhas) == 0):
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            agulha = jsonify(agulhas_share_schema.dump(agulhas))
            if agulha == []:
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            return agulha

    except Exception as e:
        return str(e), 500 

@app.route('/produtos//<int:page>', methods=['GET'])
@jwt_required
def produtoPagination(current_user, page):
    try:
        if request.method == 'GET':
            skip = (page - 1) * 5
            #Agulhas
            totalAgulhas = db.query(Agulha).count()
            agulhas = db.query(Agulha).limit(5).offset(skip).all()
            if (agulhas == None) or (len(agulhas) == 0):
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            agulha = agulhas_share_schema.dump(agulhas)
            if agulha == []:
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})
            
            #Agulhas
            totalAgulhas = db.query(Agulha).count()
            agulhas = db.query(Agulha).limit(5).offset(skip).all()
            if (agulhas == None) or (len(agulhas) == 0):
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            agulha = agulhas_share_schema.dump(agulhas)
            if agulha == []:
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})
    
            return jsonify({
                    "totalAgulhas":totalAgulhas,
                    "itens":5,
                    "totalPages": math.ceil(totalAgulhas/5),
                    "data": agulha})
    
    except Exception as e:
        return str(e), 500
    

@app.route('/produtos/<int:id>', methods=['GET'])
@jwt_required
def produtoID(current_user, id):
    return
    

@app.route('/produtos/qrcode/<int:id>', methods=['GET'])
@jwt_required
def code(current_user, id):
    if request.method == 'GET':
        try:
            # captura o host e a port da aplicação
            host = socket.gethostbyname(socket.gethostname())
            port = 5000

            # cria o código QR como uma imagem e salva na pasta
            qr_code = qrcode.make(f'http://{host}:{port}/produtos/{id}')
            qr_code.save('qrcode.png')

            # converte a imagem salva como base64
            with open('qrcode.png', 'rb') as imagem_arquivo:
                imagem_binario = imagem_arquivo.read()

            imagem_base64 = base64.b64encode(imagem_binario).decode('utf-8')

            # apaga a imagem salva na pasta
            os.remove('qrcode.png')

            # retorna a imagem em base64 como json pro font-end
            return jsonify({
                "qrcod": imagem_base64
            })
        
        except Exception as e:
            return jsonify({
                "error":str(e)
            })