import math
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

@app.route('/produtos/<int:page>', methods=['GET']) # GET
@jwt_required
def produtoPagination(current_user, page):
    try:
        if request.method == 'GET':
            skip = (page - 1) * 5

            # Elastico
            totalElastico = db.query(Elastico).count()
            elasticos = db.query(Elastico).limit(5).offset(skip).all()
            elastico_data = elasticos_share_schema.dump(elasticos)

            # Agulhas
            totalAgulhas = db.query(Agulha).count()
            agulhas = db.query(Agulha).limit(5).offset(skip).all()
            agulha_data = agulhas_share_schema.dump(agulhas)

            # Linha
            totalLinhas = db.query(Linha).count()
            linhas = db.query(Linha).limit(5).offset(skip).all()
            linha_data = linhas_share_schema.dump(linhas)
            
            # Tecido
            totalTecidos = db.query(Tecido).count()
            tecidos = db.query(Tecido).limit(5).offset(skip).all()
            tecido_data = tecidos_share_schema.dump(tecidos)

            totalProdutos = totalAgulhas + totalElastico + totalTecidos + totalLinhas

            if totalProdutos == 0:
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            produtos = [agulha_data + elastico_data + linha_data + tecido_data]

            return jsonify({
                "totalProdutos":  totalProdutos,
                "itens": 5,
                "totalPages": math.ceil(totalProdutos / 5),
                "produtos": produtos
                
            })
    
    except Exception as e:
        return str(e), 500
    

@app.route('/produtos/qrcode/<int:id>/<string:produto>', methods=['GET']) # QR Code
@jwt_required
def code(current_user, id, produto):
    if request.method == 'GET':
        try:
            # captura o host e a port da aplicação
            host = socket.gethostbyname(socket.gethostname())
            port = 5000

            # cria o código QR como uma imagem e salva na pasta
            qr_code = qrcode.make(f'http://{host}:{port}/produtos/?p={produto}&id={id}')
            qr_code.save('qrcode.png')

            # converte a imagem salva como base64
            with open('qrcode.png', 'rb') as imagem_arquivo:
                imagem_binario = imagem_arquivo.read()

            imagem_base64 = base64.b64encode(imagem_binario).decode('utf-8')

            # apaga a imagem salva na pasta
            os.remove('qrcode.png')

            # retorna a imagem em base64 como json pro font-end
            return jsonify({
                "qrcode": imagem_base64
            })
        
        except Exception as e:
            return jsonify({
                "error":str(e)
            })