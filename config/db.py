from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, registry
from werkzeug.security import generate_password_hash, check_password_hash
from app import *

Base = declarative_base()
# Criação das Tabelas do Banco de Dados

# Classe
class Classe(Base):
    __tablename__ = 'classe'

    id_classe = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    classe = Column(String(length=80), index=True)

    agulha = relationship("Agulha", back_populates="classe")
    linha = relationship("Linha", back_populates="classe")
    tecido = relationship("Tecido", back_populates="classe")
    movel = relationship("Movel", back_populates="classe")
    insumo = relationship("Insumo", back_populates="classe")
    maquina = relationship("Maquina", back_populates="classe")

class ClasseSchema(ma.Schema):
    class Meta:
        fields = ('id_classe', 'classe') 
    
classe_share_schema = ClasseSchema()
classes_share_schema = ClasseSchema(many=True)



# Categoria 
class Categoria(Base):
    __tablename__ = 'categoria'

    id_categoria = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    categoria = Column(String(length=80), index=True)

    agulha = relationship("Agulha", back_populates="categoria")
    elastico = relationship("Elastico", back_populates="categoria")
    linha = relationship("Linha", back_populates="categoria")
    tecido = relationship("Tecido", back_populates="categoria")
    movel = relationship("Movel", back_populates="categoria")
    insumo = relationship("Insumo", back_populates="categoria")
    maquina = relationship("Maquina", back_populates="categoria")

class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('id_categoria', 'categoria') 
    
categoria_share_schema = CategoriaSchema()
categorias_share_schema = CategoriaSchema(many=True)



# Maquina Agulha
class Maquina_Agulha(Base):
    __tablename__ = 'maquina_agulha'

    id_maquina_agulha = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    maquina = Column(String(length=80), index=True)

    agulha = relationship("Agulha", back_populates="maquina_agulha")

class MaquinaAgulhaSchema(ma.Schema):
    class Meta:
        fields = ('id_maquina_agulha', 'maquina') 
    
maquina_agulha_share_schema = MaquinaAgulhaSchema()
maquina_agulhas_share_schema = MaquinaAgulhaSchema(many=True)



# Especie Agulha
class Especie_Agulha(Base):
    __tablename__ = 'especie_agulha'

    id_especie_agulha = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    especie = Column(String(length=80), index=True)

    agulha = relationship("Agulha", back_populates="especie_agulha")

class EspecieAgulhaSchema(ma.Schema):
    class Meta:
        fields = ('id_especie_agulha', 'especie') 
    
especie_agulha_share_schema = EspecieAgulhaSchema()
especie_agulhas_share_schema = EspecieAgulhaSchema(many=True)



# Marca Agulha
class Marca_Agulha(Base):
    __tablename__ = 'marca_agulha'

    id_marca_agulha = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    marca = Column(String(length=80), index=True)

    agulha = relationship("Agulha", back_populates="marca_agulha")

class MarcaAgulhaSchema(ma.Schema):
    class Meta:
        fields = ('id_marca_agulha', 'marca') 
    
marca_agulha_share_schema = MarcaAgulhaSchema()
marca_agulhas_share_schema = MarcaAgulhaSchema(many=True)



# Marca Movel
class Marca_Movel(Base):
    __tablename__ = 'marca_movel'

    id_marca_movel = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    marca = Column(String(length=80), index=True)

    movel = relationship("Movel", back_populates="marca_movel")

class MarcaMovelSchema(ma.Schema):
    class Meta:
        fields = ('id_marca_movel', 'marca') 
    
marca_movel_share_schema = MarcaMovelSchema()
marca_moveis_share_schema = MarcaMovelSchema(many=True)



# Marca Insumo
class Marca_Insumo(Base):
    __tablename__ = 'marca_insumo'

    id_marca_insumo = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    insumo = Column(String(length=80), index=True)

    insumo = relationship("Insumo", back_populates="marca_insumo")

class MarcaInsumoSchema(ma.Schema):
    class Meta:
        fields = ('id_marca_insumo', 'insumo') 
    
marca_insumo_share_schema = MarcaInsumoSchema()
marca_insumos_share_schema = MarcaInsumoSchema(many=True)



# Marca Maquina
class Marca_Maquina(Base):
    __tablename__ = 'marca_maquina'

    id_marca_maquina = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    maquina = Column(String(length=80), index=True)

    maquina = relationship("Maquina", back_populates="marca_maquina")

class MarcaMaquinaSchema(ma.Schema):
    class Meta:
        fields = ('id_marca_maquina', 'maquina') 
    
marca_maquina_share_schema = MarcaMaquinaSchema()
marca_maquinas_share_schema = MarcaMaquinaSchema(many=True)



# Unidade
class Unidade(Base):
    __tablename__ = 'unidade'

    id_unidade = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    unidade = Column(String(length=80), index=True)

    agulha = relationship("Agulha", back_populates="unidade")
    elastico = relationship("Elastico", back_populates="unidade")
    linha = relationship("Linha", back_populates="unidade")
    tecido = relationship("Tecido", back_populates="unidade")

class UnidadeSchema(ma.Schema):
    class Meta:
        fields = ('id_unidade', 'unidade') 
    
unidade_share_schema = UnidadeSchema()
unidades_share_schema = UnidadeSchema(many=True)



# Permissões
class Permissao(Base):
    __tablename__ = 'permissao'

    id_permissao = Column(Integer, primary_key=True, index=True, autoincrement=True)
    descricao = Column(String(length=100), unique=True, index=True)

    # Relação entre usuário e produtos (um usuário pode ter vários produtos)
    usuario = relationship("Usuario", back_populates="permissao")

class PermissaoSchema(ma.Schema):
    class Meta:
        fields = ('id_permissao', 'descricao')
    
permissao_share_schema = PermissaoSchema()
permissoes_share_schema = PermissaoSchema(many=True)



# Usuários
class Usuario(Base):
    __tablename__ = 'usuario'
    id_usuario = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(length=50), unique=True, index=True)
    senha = Column(String(length=200), unique=False, index=True)
    id_permissao = Column(Integer, ForeignKey('permissao.id_permissao'))

    # Relação inversa entre produtos e usuário
    permissao = relationship("Permissao", back_populates="usuario")

    def __init__(self, username, senha, id_permissao):
        self.username = username
        self.senha = generate_password_hash(senha)
        self.id_permissao = id_permissao
    
    def verify_password(self, senha):
        return check_password_hash(self.senha, senha)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id_usuario', 'username', 'id_permissao')
    
user_share_schema = UserSchema()
users_share_schema = UserSchema(many=True)



# Tipo Elastico
class Tipo_Elastico(Base):
    __tablename__ = 'tipo_elastico'

    id_tipo_elastico = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    tipo = Column(String(length=80), index=True)

    elastico = relationship("Elastico", back_populates="tipo_elastico")

class TipoElasticoSchema(ma.Schema):
    class Meta:
        fields = ('id_tipo_elastico', 'tipo') 
    
tipo_elastico_share_schema = TipoElasticoSchema()
tipo_elasticos_share_schema = TipoElasticoSchema(many=True)



# Tipo Insumo
class Tipo_Insumo(Base):
    __tablename__ = 'tipo_insumo'

    id_tipo_insumo = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    tipo = Column(String(length=80), index=True)

    insumo = relationship("Insumo", back_populates="tipo_insumo")

class TipoInsumoSchema(ma.Schema):
    class Meta:
        fields = ('id_tipo_insumo', 'tipo') 
    
tipo_insumo_share_schema = TipoInsumoSchema()
tipo_insumos_share_schema = TipoInsumoSchema(many=True)



# Tipo Maquina
class Tipo_Maquina(Base):
    __tablename__ = 'tipo_maquina'

    id_tipo_maquina = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    tipo = Column(String(length=80), index=True)

    maquina = relationship("Maquina", back_populates="tipo_maquina")

class TipoMaquinaSchema(ma.Schema):
    class Meta:
        fields = ('id_tipo_maquina', 'tipo') 
    
tipo_maquina_share_schema = TipoMaquinaSchema()
tipo_maquinas_share_schema = TipoMaquinaSchema(many=True)



# Tipo Movel
class Tipo_Movel(Base):
    __tablename__ = 'tipo_movel'

    id_tipo_movel = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    tipo = Column(String(length=80), index=True)

    movel = relationship("Movel", back_populates="tipo_movel")

class TipoMovelSchema(ma.Schema):
    class Meta:
        fields = ('id_tipo_movel', 'tipo') 
    
tipo_movel_share_schema = TipoMovelSchema()
tipo_moveis_share_schema = TipoMovelSchema(many=True)



# Composicao 
class Composicao(Base):
    __tablename__ = 'composicao'

    id_composicao = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    composicao = Column(String(length=80), index=True)

    elastico = relationship("Elastico", back_populates="composicao")
    linha = relationship("Linha", back_populates="composicao")
    tecido = relationship("Tecido", back_populates="composicao")
    movel = relationship("Movel", back_populates="composicao")
    insumo = relationship("Insumo", back_populates="composicao")

class ComposicaoSchema(ma.Schema):
    class Meta:
        fields = ('id_composicao', 'composicao') 
    
composicao_share_schema = ComposicaoSchema()
composicoes_share_schema = ComposicaoSchema(many=True)



# Marca Elastico
class Marca_Elastico(Base):
    __tablename__ = 'marca_elastico'

    id_marca_elastico = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    marca = Column(String(length=80), index=True)

    elastico = relationship("Elastico", back_populates="marca_elastico")

class MarcaElasticoSchema(ma.Schema):
    class Meta:
        fields = ('id_marca_elastico', 'marca') 
    
marca_elastico_share_schema = MarcaElasticoSchema()
marca_elasticos_share_schema = MarcaElasticoSchema(many=True)



# Tipo Linha
class Tipo_Linha(Base):
    __tablename__ = 'tipo_linha'

    id_tipo_linha = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    tipo = Column(String(length=80), index=True)

    linha = relationship("Linha", back_populates="tipo_linha")

class TipoLinhaSchema(ma.Schema):
    class Meta:
        fields = ('id_tipo_linha', 'tipo') 
    
tipo_linha_share_schema = TipoLinhaSchema()
tipo_linhas_share_schema = TipoLinhaSchema(many=True)



# Embalagem
class Embalagem(Base):
    __tablename__ = 'embalagem'

    id_embalagem = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    embalagem = Column(String(length=80), index=True)

    tecido = relationship("Tecido", back_populates="embalagem")
    elastico = relationship("Elastico", back_populates="embalagem")
    linha = relationship("Linha", back_populates="embalagem")

class EmbalagemSchema(ma.Schema):
    class Meta:
        fields = ('id_embalagem', 'embalagem') 
    
embalagem_share_schema = EmbalagemSchema()
embalagens_share_schema = EmbalagemSchema(many=True)



# Elastico
class Elastico(Base):
    __tablename__ = 'elastico'

    id_elastico = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    foto = Column(String(length=200), index=True)
    id_categoria = Column(Integer, ForeignKey('categoria.id_categoria')) # sub tabela / lista suspensa / foreign-key
    id_tipo_elastico = Column(Integer, ForeignKey('tipo_elastico.id_tipo_elastico')) # sub tabela / lista suspensa / foreign-key
    nome = Column(String(length=80), index=True)
    id_composicao = Column(Integer, ForeignKey('composicao.id_composicao')) # sub tabela / lista suspensa / foreign-key
    fornecedor = Column(String(length=80), index=True)
    id_marca_elastico = Column(Integer, ForeignKey('marca_elastico.id_marca_elastico')) # sub tabela / foreign-key
    cor = Column(String(length=80), index=True)
    ref = Column(String(length=100), index=True)
    ref_inter = Column(String(length=100), index=True)
    qr_code = Column(String(length=200), index=True)
    largura_mm = Column(Integer, index=True)
    embalagem_m = Column(Integer, ForeignKey('embalagem.id_embalagem')) # sub tabela / foreign-key
    id_unidade = Column(Integer, ForeignKey('unidade.id_unidade')) # sub tabela / foreign-key
    estoque_rolo = Column(Integer, index=True)
    valor = Column(Integer, index=True)
    imposto = Column(Integer, index=True)
    preco_final = Column(Integer, index=True)
    valor_estoque_total = Column(Integer, index=True)
    aplicacao = Column(String(length=100), index=True)
    obs = Column(String(length=100), index=True)
    estoque_minimo_rolo = Column(Integer, index=True)
    em_falta = Column(String(length=3), index=True)
    data_compra = Column(Date, index=True)

    categoria = relationship("Categoria", back_populates="elastico")
    tipo_elastico = relationship("Tipo_Elastico", back_populates="elastico")
    composicao = relationship("Composicao", back_populates="elastico")
    marca_elastico = relationship("Marca_Elastico", back_populates="elastico")
    unidade = relationship("Unidade", back_populates="elastico")
    embalagem = relationship("Embalagem", back_populates="elastico")

class ElasticoSchema(ma.Schema):
    class Meta:
        fields = ('id_elastico', 'foto', 'id_categoria', 'id_tipo_elastico', 'nome', 'id_composicao', 'fornecedor', 'id_marca_elastico', 'cor', 'ref', 'ref_inter', 'qr_code', 'largura_mm', 'embalagem_m', 'id_unidade', 'estoque_rolo', 'valor', 'imposto', 'preco_final', 'valor_estoque_total', 'aplicacao', 'obs', 'estoque_minimo_rolo', 'em_falta', 'data_compra')

elastico_share_schema = ElasticoSchema()
elasticos_share_schema = ElasticoSchema(many=True)



# Linha
class Linha(Base):
    __tablename__ = 'linha'

    id_linha = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    foto = Column(String(length=200), index=True)
    id_categoria = Column(Integer, ForeignKey('categoria.id_categoria')) # sub tabela / lista suspensa / foreign-key
    id_classe = Column(Integer, ForeignKey('classe.id_classe')) # sub tabela / lista suspensa / foreign-key
    id_tipo_linha = Column(Integer, ForeignKey('tipo_linha.id_tipo_linha')) # sub tabela / lista suspensa / foreign-key
    id_composicao = Column(Integer, ForeignKey('composicao.id_composicao')) # sub tabela / lista suspensa / foreign-key
    fornecedor = Column(String(length=80), index=True)
    marca_linha = Column(String(length=80), index=True)
    cor = Column(String(length=80), index=True)
    ref = Column(String(length=100), index=True)
    num_pedido = Column(Integer, index=True)
    qr_code = Column(String(length=200), index=True)
    tamanho_jardas = Column(Integer, index=True)
    quantidade_pecas_cone = Column(Integer, index=True)
    id_unidade = Column(Integer, ForeignKey('unidade.id_unidade')) # sub tabela / foreign-key
    id_embalagem = Column(Integer, ForeignKey('embalagem.id_embalagem')) # sub tabela / foreign-key
    estoque_cone = Column(Integer, index=True)
    valor = Column(Integer, index=True)
    imposto = Column(Integer, index=True)
    preco_final = Column(Integer, index=True)
    valor_estoque_total = Column(Integer, index=True)
    obs = Column(String(length=100), index=True)
    estoque_minimo_cone = Column(Integer, index=True)
    em_falta = Column(String(length=3), index=True)
    data_compra = Column(Date, index=True)

    categoria = relationship("Categoria", back_populates="linha")
    classe = relationship("Classe", back_populates="linha")
    tipo_linha = relationship("Tipo_Linha", back_populates="linha")
    composicao = relationship("Composicao", back_populates="linha")
    unidade = relationship("Unidade", back_populates="linha")
    embalagem = relationship("Embalagem", back_populates="linha")

class LinhaSchema(ma.Schema):
    class Meta:
        fields = ('id_linha', 'foto', 'id_categoria', 'id_classe', 'id_tipo_linha', 'id_composicao', 'fornecedor', 'marca_linha', 'cor', 'ref', 'num_pedido', 'qr_code', 'tamanho_jardas', 'quantidade_pecas_cone', 'id_unidade', 'id_embalagem', 'estoque_cone', 'valor', 'imposto', 'preco_final', 'valor_estoque_total', 'obs', 'estoque_minimo_cone', 'em_falta', 'data_compra')

linha_share_schema = ElasticoSchema()
linhas_share_schema = ElasticoSchema(many=True)



# Tecido
class Tecido(Base):
    __tablename__ = 'tecido'

    id_tecido = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    foto = Column(String(length=200), index=True)
    id_categoria = Column(Integer, ForeignKey('categoria.id_categoria')) # sub tabela / lista suspensa / foreign-key
    id_classe = Column(Integer, ForeignKey('classe.id_classe')) # sub tabela / lista suspensa / foreign-key
    tipo_tecido = Column(String(length=80), index=True)
    id_composicao = Column(Integer, ForeignKey('composicao.id_composicao')) # sub tabela / lista suspensa / foreign-key
    fornecedor = Column(String(length=80), index=True)
    marca_linha = Column(String(length=80), index=True)
    importado = Column(String(length=3), index=True)
    estampado = Column(String(length=3), index=True)
    cor = Column(String(length=80), index=True)
    estampa = Column(String(length=80), index=True)
    ref = Column(String(length=100), index=True)
    num_pedido = Column(Integer, index=True)
    qr_code = Column(String(length=200), index=True)
    ramado = Column(String(length=3), index=True)
    plano = Column(String(length=3), index=True)
    largura_m = Column(Integer, index=True)
    gramatura_gm2 = Column(Integer, index=True)
    id_unidade = Column(Integer, ForeignKey('unidade.id_unidade')) # sub tabela / foreign-key
    rendimento_mkg = Column(Integer, index=True)
    tamanho_kg = Column(Integer, index=True)
    qantidade_peca = Column(Integer, index=True)
    id_embalagem = Column(Integer, ForeignKey('embalagem.id_embalagem')) # sub tabela / foreign-key
    estoque_kg = Column(Integer, index=True)
    valor = Column(Integer, index=True)
    imposto = Column(Integer, index=True)
    preco_final = Column(Integer, index=True)
    valor_estoque_total = Column(Integer, index=True)
    aplicacao = Column(String(length=100), index=True)
    obs = Column(String(length=100), index=True)
    estoque_minimo_kg = Column(Integer, index=True)
    em_falta = Column(String(length=3), index=True)
    data_compra = Column(Date, index=True)

    categoria = relationship("Categoria", back_populates="tecido")
    classe = relationship("Classe", back_populates="tecido")
    composicao = relationship("Composicao", back_populates="tecido")
    embalagem = relationship("Embalagem", back_populates="tecido")
    unidade = relationship("Unidade", back_populates="tecido")

class TecidoSchema(ma.Schema):
    class Meta:
        fields = ('id_tecido', 'foto', 'id_categoria', 'id_classe', 'tipo_tecido', 'id_composicao', 'fornecedor', 'marca_linha', 'importado', 'estampado', 'cor', 'estampa', 'ref', 'num_pedido', 'qr_code', 'ramado', 'plano', 'largura_m', 'gramatura_gm2', 'id_unidade', 'rendimento_mkg', 'tamanho_kg', 'qantidade_peca', 'id_embalagem', 'estoque_kg', 'valor', 'imposto', 'preco_final', 'valor_estoque_total', 'aplicacao', 'obs', 'estoque_minimo_kg', 'em_falta', 'data_compra')

tecido_share_schema = TecidoSchema()
tecidos_share_schema = TecidoSchema(many=True)



# Agulha
class Agulha(Base):
    __tablename__ = 'agulha'

    id_agulha = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    id_classe = Column(Integer, ForeignKey('classe.id_classe')) # sub tabela / lista suspensa / foreign-key
    foto = Column(String(length=200), index=True)
    id_categoria = Column(Integer, ForeignKey('categoria.id_categoria')) # sub tabela / lista suspensa / foreign-key
    id_maquina_agulha = Column(Integer, ForeignKey('maquina_agulha.id_maquina_agulha')) # sub tabela / lista suspensa / foreign-key
    id_especie_agulha = Column(Integer, ForeignKey('especie_agulha.id_especie_agulha')) # sub tabela / lista suspensa / foreign-key
    fornecedor = Column(String(length=80), index=True)
    id_marca_agulha = Column(Integer, ForeignKey('marca_agulha.id_marca_agulha')) # sub tabela / foreign-key
    ref = Column(String(length=100), index=True)
    num_pedido = Column(Integer, index=True)
    qr_code = Column(String(length=200), index=True)
    tamanho_tam = Column(Integer, index=True)
    estoque_cx = Column(Integer, index=True)
    id_unidade = Column(Integer, ForeignKey('unidade.id_unidade')) # sub tabela / foreign-key
    valor = Column(Integer, index=True)
    imposto = Column(Integer, index=True)
    preco_final = Column(Integer, index=True)
    valor_estoque_total = Column(Integer, index=True)
    aplicacao = Column(String(length=100), index=True)
    obs = Column(String(length=100), index=True)
    estoque_minimo_cx = Column(Integer, index=True)
    em_falta = Column(String(length=3), index=True)
    data_compra = Column(Date, index=True)

    classe = relationship("Classe", back_populates="agulha")
    categoria = relationship("Categoria", back_populates="agulha")
    maquina_agulha = relationship("Maquina_Agulha", back_populates="agulha")
    especie_agulha = relationship("Especie_Agulha", back_populates="agulha")
    marca_agulha = relationship("Marca_Agulha", back_populates="agulha")
    unidade = relationship("Unidade", back_populates="agulha")

class AgulhaSchema(ma.Schema):
    class Meta:
        fields = ('id_agulha', 'id_classe', 'foto', 'id_categoria', 'id_maquina_agulha', 'id_especie_agulha', 'fornecedor', 'id_marca_agulha', 'ref', 'num_pedido', 'qr_code', 'tamanho_tam', 'estoque_cx', 'id_unidade', 'valor', 'imposto', 'preco_final', 'valor_estoque_total', 'aplicacao', 'obs', 'estoque_minimo_cx', 'em_falta', 'data_compra') 
    
agulha_share_schema = AgulhaSchema()
agulhas_share_schema = AgulhaSchema(many=True)



# Moveis
class Movel(Base):
    __tablename__ = 'movel'

    id_movel = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    id_classe = Column(Integer, ForeignKey('classe.id_classe')) # sub tabela / lista suspensa / foreign-key
    id_categoria = Column(Integer, ForeignKey('categoria.id_categoria')) # sub tabela / lista suspensa / foreign-key
    id_tipo_movel = Column(Integer, ForeignKey('tipo_movel.id_tipo_movel'))
    id_composicao = Column(Integer, ForeignKey('composicao.id_composicao')) # sub tabela / lista suspensa / foreign-key
    fornecedor = Column(String(length=80), index=True)
    id_marca_movel = Column(Integer, ForeignKey('marca_movel.id_marca_movel'))
    cor = Column(String(length=80), index=True)
    estoque_cx = Column(Integer, index=True)
    valor = Column(Integer, index=True)
    imposto = Column(Integer, index=True)
    preco_final = Column(Integer, index=True)
    valor_estoque_total = Column(Integer, index=True)
    aplicacao = Column(String(length=100), index=True)
    obs = Column(String(length=100), index=True)
    estoque_minimo_cx = Column(Integer, index=True)
    em_falta = Column(String(length=3), index=True)
    data_compra = Column(Date, index=True)

    classe = relationship("Classe", back_populates="movel")
    categoria = relationship("Categoria", back_populates="movel")
    composicao = relationship("Composicao", back_populates="movel")
    tipo_movel = relationship("Tipo_Movel", back_populates="movel")
    marca_movel = relationship("Marca_Movel", back_populates="movel")

class MovelSchema(ma.Schema):
    class Meta:
        fields = ('id_movel', 'id_classe', 'id_categoria','id_tipo_movel', 'id_composicao', 'fornecedor', 'id_marca_movel', 'cor', 'estoque_cx', 'valor', 'imposto', 'preco_final', 'valor_estoque_total', 'aplicacao', 'obs', 'estoque_minimo_cx', 'em_falta', 'data_compra') 
    
movel_share_schema = MovelSchema()
moveis_share_schema = MovelSchema(many=True)



# Insumo
class Insumo(Base):
    __tablename__ = 'insumo'

    id_insumo = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    id_classe = Column(Integer, ForeignKey('classe.id_classe')) # sub tabela / lista suspensa / foreign-key
    id_categoria = Column(Integer, ForeignKey('categoria.id_categoria')) # sub tabela / lista suspensa / foreign-key
    id_tipo_insumo = Column(Integer, ForeignKey('tipo_insumo.id_tipo_insumo'))
    id_composicao = Column(Integer, ForeignKey('composicao.id_composicao')) # sub tabela / lista suspensa / foreign-key
    fornecedor = Column(String(length=80), index=True)
    id_marca_insumo = Column(Integer, ForeignKey('marca_insumo.id_marca_insumo'))
    cor = Column(String(length=80), index=True)
    ref = Column(String(length=100), index=True)
    ref_inter = Column(String(length=100), index=True)
    qr_code = Column(String(length=200), index=True)
    tamanho_tam = Column(String(length=80), index=True)
    quantidade_pecas = Column(Integer, index=True)
    embalagem = Column(String(length=80), index=True)
    estoque = Column(String(length=80), index=True)
    valor = Column(Integer, index=True)
    imposto = Column(Integer, index=True)
    preco_final = Column(Integer, index=True)
    valor_estoque_total = Column(Integer, index=True)
    aplicacao = Column(String(length=100), index=True)
    obs = Column(String(length=100), index=True)
    estoque_minimo = Column(String(length=80), index=True)
    em_falta = Column(String(length=3), index=True)
    data_compra = Column(Date, index=True)

    classe = relationship("Classe", back_populates="insumo")
    categoria = relationship("Categoria", back_populates="insumo")
    composicao = relationship("Composicao", back_populates="insumo")
    tipo_insumo = relationship("Tipo_Insumo", back_populates="insumo")
    marca_insumo = relationship("Marca_Insumo", back_populates="insumo")

class InsumoSchema(ma.Schema):
    class Meta:
        fields = ('id_insumo', 'id_classe', 'id_categoria','id_tipo_insumo', 'id_composicao', 'fornecedor', 'id_marca_insumo', 'cor','ref', 'ref_inter', 'qr_code', 'tamanho_tam', 'quantidade_pecas', 'embalagem', 'estoque', 'valor', 'imposto', 'preco_final', 'valor_estoque_total', 'aplicacao', 'obs', 'estoque_minimo', 'em_falta', 'data_compra') 
    
insumo_share_schema = InsumoSchema()
insumos_share_schema = InsumoSchema(many=True)



# Maquina
class Maquina(Base):
    __tablename__ = 'maquina'

    id_maquina = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    id_classe = Column(Integer, ForeignKey('classe.id_classe')) # sub tabela / lista suspensa / foreign-key
    id_categoria = Column(Integer, ForeignKey('categoria.id_categoria')) # sub tabela / lista suspensa / foreign-key
    id_tipo_maquina = Column(Integer, ForeignKey('tipo_maquina.id_tipo_maquina'))
    fornecedor = Column(String(length=80), index=True)
    id_marca_maquina = Column(Integer, ForeignKey('marca_maquina.id_marca_maquina'))
    cor = Column(String(length=80), index=True)
    ref = Column(String(length=100), index=True)
    ref_inter = Column(String(length=100), index=True)
    qr_code = Column(String(length=200), index=True)
    estoque = Column(String(length=80), index=True)
    valor = Column(Integer, index=True)
    imposto = Column(Integer, index=True)
    preco_final = Column(Integer, index=True)
    valor_estoque_total = Column(Integer, index=True)
    aplicacao = Column(String(length=100), index=True)
    obs = Column(String(length=100), index=True)
    estoque_minimo_cx = Column(Integer, index=True)
    em_falta = Column(String(length=3), index=True)
    data_compra = Column(Date, index=True)

    classe = relationship("Classe", back_populates="maquina")
    categoria = relationship("Categoria", back_populates="maquina")
    tipo_maquina = relationship("Tipo_Maquina", back_populates="maquina")
    marca_maquina = relationship("Marca_Maquina", back_populates="maquina")

class MaquinaSchema(ma.Schema):
    class Meta:
        fields = ('id_maquina', 'id_classe', 'id_categoria','id_tipo_maquina', 'fornecedor', 'id_marca_maquina', 'cor', 'ref', 'ref_inter', 'qr_code', 'estoque', 'valor', 'imposto', 'preco_final', 'valor_estoque_total', 'aplicacao', 'obs', 'estoque_minimo_cx', 'em_falta', 'data_compra') 
    
maquina_share_schema = MaquinaSchema()
maquinas_share_schema = MaquinaSchema(many=True)



# Configurar o banco de dados
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

# Crie as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Criar uma sessão para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()
