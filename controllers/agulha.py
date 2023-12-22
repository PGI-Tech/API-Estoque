from app import app
from flask import Flask, jsonify, request
from config.db import *
from config.authenticate import *

@app.route('/agulha', methods=['GET'])
@jwt_required
def agulha(current_user):
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
    

@app.route('/agulha/<int:id>', methods=['GET'])
@jwt_required
def agulhaID(current_user, id):
    try:
        if request.method == 'GET':
            agulhas = db.query(Agulha).filter_by(id_agulha=id).first()
            if agulhas == None:
                return jsonify({"error": "O ID informado não consta na tabela de Agulha!"})

            agulha = jsonify(agulha_share_schema.dump(agulhas))
            if agulha == []:
                return jsonify({"error": "O ID informado não consta na tabela de Agulha!"})

            return agulha

    except Exception as e:
        return str(e), 500


@app.route('/agulha', methods=['POST'])
@jwt_required
def newAgulha():
    try:
        if request.method == 'POST':
            id_agulha = id_agulha
            id_classe = id_classe
            foto = foto
            id_categoria = id_categoria
            id_maquina_agulha = request.json['id_maquina_agulha']
            id_especie_agulha = request.json['id_especie_agulha']
            fornecedor = request.json['fornecedor']
            id_marca_agulha = request.json['id_marca_agulha']
            ref = request.json['ref']
            num_pedido = request.json['num_pedido']
            qr_code = request.json['qr_code']
            tamanho_tam = request.json['tamanho_tam']
            estoque_cx = request.json['estoque_cx']
            id_unidade = request.json['id_unidade']
            valor = request.json['valor']
            imposto = request.json['imposto']
            preco_final = request.json['preco_final']
            valor_estoque_total = request.json['valor_estoque_total']
            aplicacao = request.json['aplicacao']
            obs = request.json['obs']
            estoque_minimo_cx = request.json['estoque_minimo_cx']
            em_falta = request.json['em_falta']
            data_compra = request.json['data_compra']

            # Cria uma nova instância do modelo Agulha com os dados
            newAgulha = Agulha(
                id_agulha=id_agulha,
                id_classe=id_classe,
                foto=foto,
                id_categoria=id_categoria,
                id_maquina_agulha=id_maquina_agulha,
                id_especie_agulha=id_especie_agulha,
                fornecedor=fornecedor,
                id_marca_agulha=id_marca_agulha,
                ref=ref,
                num_pedido=num_pedido,
                qr_code=qr_code,
                tamanho_tam=tamanho_tam,
                estoque_cx=estoque_cx,
                id_unidade=id_unidade,
                valor=valor,
                imposto=imposto,
                preco_final=preco_final,
                valor_estoque_total=valor_estoque_total,
                aplicacao=aplicacao,
                obs=obs,
                estoque_minimo_cx=estoque_minimo_cx,
                em_falta=em_falta,
                data_compra=data_compra
            )

            db.add(newAgulha)
            db.commit()

            return jsonify({"message": "Nova Agulha criada com sucesso!",
                            "agulha": agulha_share_schema.dump(db.query(Agulha).filter_by(id_agulha=id_agulha).first())})

    except Exception as e:
        return str(e), 500
    

@app.route('/agulha/<int:id>', methods=['PUT'])
@jwt_required
def editAgulha(current_user, id):
    try:
        if request.method == 'PUT':
            agulhas = db.query(Agulha).filter_by(id_agulha=id).first()
            if agulhas == None:
                return jsonify({"error": "O ID informado não consta na tabela de agulha!"})

            agulha = jsonify(agulha_share_schema.dump(agulhas))
            if agulha == []:
                return jsonify({"error": "O ID informado não consta na tabela de agulha!"})

            db.query(Agulha).filter_by(
                id_agulha=id).update(request.json)
            db.commit()

            return jsonify(agulha_share_schema.dump(db.query(Agulha).filter_by(id_agulha=id)))

    except Exception as e:
        return str(e), 500


@app.route('/agulha/<int:id>', methods=['DELETE'])
@jwt_required
def deleteAgulha(current_user, id):
    try:
        if request.method == 'DELETE':
            agulhas = db.query(Agulha).filter_by(id_agulha=id).first()
            if agulhas == None:
                return jsonify({"error": "O ID informado não consta na tabela de agulha!"})

            agulha = jsonify(agulha_share_schema.dump(agulhas))
            if agulha == []:
                return jsonify({"error": "O ID informado não consta na tabela de agulha!"})

            db.query(Agulha).filter_by(id_agulha=id).delete()
            db.commit()

            return jsonify({"message": f"Agulha de ID {id} deletada com sucesso!"})

    except Exception as e:
        return str(e), 500
