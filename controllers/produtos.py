"""import os
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
            produtos = db.query(Produto).all()
            if (produtos == None) or (len(produtos) == 0):
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})

            prod = jsonify(produtos_share_schema.dump(produtos))
            if prod == []:
                return jsonify({"error": "Não há nenhum dado cadastrado nessa tabela"})
            return prod
    
    except Exception as e:
        return str(e), 500
    

@app.route('/produtos/<int:id>', methods=['GET'])
@jwt_required
def produtoID(current_user, id):
    try:
        if request.method == 'GET':
            produtos = db.query(Produto).filter_by(id_produto=id).first()
            if produtos == None:
                return jsonify({"error":"O ID informado não consta na tabela de Produtos!"})
            
            prod = jsonify(produto_share_schema.dump(produtos))
            if prod == []:
                return jsonify({"error":"O ID informado não consta na tabela de Produtos!"})
            
            return prod

    except Exception as e:
        return str(e), 500


@app.route('/produtos', methods=['POST'])
@jwt_required
def newProduto(current_user):
    try: 
        if request.method == 'POST':
            descricao = request.json['descricao']
            quantidade = request.json['quantidade']
            publico = request.json['publico']
            materia_prima = request.json['materia_prima']

            # Cria uma nova instância do modelo Produto com os dados
            newProd = Produto(
                descricao = descricao,
                quantidade = quantidade,
                publico = publico,
                materia_prima = materia_prima
            )

            db.add(newProd)
            db.commit()

            return jsonify({"message": "Novo produto criado com sucesso!",
                            "produto": produto_share_schema.dump(db.query(Produto).filter_by(descricao = descricao).first())})
    
    except Exception as e:
        return str(e), 500


@app.route('/produtos/<int:id>', methods=['PUT'])
@jwt_required
def editProduto(current_user, id):
    try:
       if request.method == 'PUT':
            produtos = db.query(Produto).filter_by(id_produto=id).first()
            if produtos == None:
                return jsonify({"error":"O ID informado não consta na tabela de Produtos!"})

            prod = jsonify(produto_share_schema.dump(produtos))
            if prod == []:
                return jsonify({"error":"O ID informado não consta na tabela de Produtos!"})

            db.query(Produto).filter_by(
                id_produto=id).update(request.json)
            db.commit()

            return jsonify(produto_share_schema.dump(db.query(Produto).filter_by(id_produto=id).first()))

    except Exception as e:
        return str(e), 500


@app.route('/produtos/<int:id>', methods=['DELETE'])
@jwt_required
def deleteProduto(current_user, id):
    try:
        if request.method == 'DELETE':
            produtos = db.query(Produto).filter_by(id_produto=id).first()
            if produtos == None:
                return jsonify({"error":"O ID informado não consta na tabela de Produtos!"})

            prod = jsonify(produto_share_schema.dump(produtos))
            if prod == []:
                return jsonify({"error":"O ID informado não consta na tabela de Produtos!"})

            db.query(Produto).filter_by(id_produto=id).delete()
            db.commit()

            return jsonify({"message": f"Produto de ID {id} deletado com sucesso!"})

    except Exception as e:
        return str(e), 500
    
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
            })"""